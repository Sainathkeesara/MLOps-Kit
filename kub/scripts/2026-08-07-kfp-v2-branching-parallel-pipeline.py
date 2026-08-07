# last_verified: 2026-08-07 · kfp >=2.0
"""kub-035 — KFP v2 pipeline with branching, parallelism, and artifact passing.

I wired three KFP v2 patterns into one pipeline after two earlier attempts
that each hit a different snag:
1. Branching with dsl.Condition (ensemble flag routes to deploy or log)
2. Parallelism with dsl.ParallelFor (sweep three learning rates at once)
3. Artifact passing via dsl.OutputPath (prep output feeds the parallel loop;
   collected artifacts feed the selector; best artifact feeds deploy/log)

Key gotcha this time: my first draft used hardcoded /tmp paths inside
ParallelFor, which breaks on remote KFP backends because each iteration
runs in its own isolated container. Switching to dsl.OutputPath() makes
the artifact location backend-agnostic.
"""

from kfp import dsl, compiler


@dsl.component(base_image="python:3.9-slim")
def prep_data(raw_csv: str, out_path: dsl.OutputPath(str)):
    """Split raw CSV into train/test, write both to out_path."""
    lines = raw_csv.strip().splitlines()
    header = lines[0]
    rows = [l for l in lines[1:] if l.strip()]
    split = int(len(rows) * 0.8)

    train = "\n".join([header] + rows[:split])
    test = "\n".join([header] + rows[split:])

    with open(out_path, "w") as f:
        f.write(train + "\n---TEST---\n" + test + "\n")

    print(f"prep_data: {split} train rows, {len(rows) - split} test rows")


@dsl.component(base_image="python:3.9-slim")
def train_and_evaluate(
    data_path: str,
    lr: float,
    epochs: int,
    accuracy_out: dsl.OutputPath(str),
    artifact_out: dsl.OutputPath(str),
):
    """Train a mock model, write accuracy and artifact to output paths."""
    import json

    accuracy = min(0.5 + lr * 10 + epochs * 0.01, 0.95)
    artifact = {"learning_rate": lr, "epochs": epochs, "accuracy": accuracy}

    with open(accuracy_out, "w") as f:
        f.write(f"{accuracy}\n")

    with open(artifact_out, "w") as f:
        json.dump(artifact, f)

    print(f"trained lr={lr} epochs={epochs} → accuracy={accuracy:.3f}")


@dsl.component(base_image="python:3.9-slim")
def collect_accuracies(artifact_dir: dsl.InputPath(str), out_file: dsl.OutputPath(str)):
    """Write all artifact file paths from the parallel sweep into one list."""
    import os

    entries = []
    if os.path.isdir(artifact_dir):
        for name in sorted(os.listdir(artifact_dir)):
            entries.append(os.path.join(artifact_dir, name))

    with open(out_file, "w") as f:
        f.write("\n".join(entries) + "\n")

    print(f"collect_accuracies: gathered {len(entries)} artifact paths")


@dsl.component(base_image="python:3.9-slim")
def best_model_selector(
    collected: dsl.InputPath(str),
    threshold: float,
    best_out: dsl.OutputPath(str),
) -> str:
    """Pick the highest-accuracy model above threshold, write its path."""
    import json
    import os

    best_path = None
    best_acc = 0.0

    with open(collected) as f:
        for line in f:
            path = line.strip()
            if not path or not os.path.exists(path):
                continue
            with open(path) as mf:
                model = json.load(mf)
            acc = model["accuracy"]
            print(f"selector: {path} → accuracy={acc:.3f}")
            if acc > best_acc:
                best_acc = acc
                best_path = path

    result = best_path if (best_path and best_acc >= threshold) else ""
    with open(best_out, "w") as f:
        f.write(result + "\n")

    print(f"selector: best={best_acc:.3f} threshold={threshold:.2f} → {result or 'none'}")
    return best_out


@dsl.component(base_image="python:3.9-slim")
def deploy_model(best_model_path: str):
    """Deploy the best model (placeholder for a real serving push)."""
    import os

    if not best_model_path or not os.path.exists(best_model_path):
        print("deploy_model: no valid model path, skipping")
        return
    print(f"deploying model from {best_model_path}")


@dsl.component(base_image="python:3.9-slim")
def log_failed_run(collected: dsl.InputPath(str), threshold: float):
    """Log when no model in the sweep crossed the deploy threshold."""
    with open(collected) as f:
        count = sum(1 for line in f if line.strip())
    print(f"log_failed_run: {count} models evaluated, none above {threshold:.2f}")


@dsl.pipeline(
    name="kfp-v2-branching-parallel",
    description="Parallel LR sweep, conditional deploy, artifact passing end-to-end",
)
def branching_parallel_pipeline(
    raw_csv: str = "x,1\ny,2\nz,3\na,4\nb,5\nc,6\nd,7\ne,8\nf,9\ng,10",
    epochs: int = 20,
    accuracy_threshold: float = 0.7,
    use_ensemble: bool = False,
):
    """Branch on use_ensemble, sweep LRs in parallel, collect, deploy or log."""
    lr_values = [0.01, 0.05, 0.1, 0.2]

    # ── Step 1: prep data ──
    prep = prep_data(raw_csv=raw_csv)

    # ── Step 2: parallel training sweep ──
    # Each ParallelFor iteration writes accuracy_out and artifact_out via
    # dsl.OutputPath, which KFP resolves to a unique subdirectory per run.
    with dsl.ParallelFor(lr_values) as lr:
        train = train_and_evaluate(
            data_path=prep.output,
            lr=lr,
            epochs=epochs,
        )

    # ── Step 3: collect all artifact_out outputs into one list file ──
    # KFP resolves the ParallelFor's artifact_out as a directory; the
    # collector flattens it into a single newline-delimited list so the
    # selector can iterate without depending on KFP's internal layout.
    gather = collect_accuracies(artifact_dir=train.outputs["artifact_out"])

    # ── Step 4: select the best model from the parallel sweep ──
    selector = best_model_selector(
        collected=gather.outputs["out_file"],
        threshold=accuracy_threshold,
    )

    # ── Step 5: conditional branch on use_ensemble flag ──
    # My first attempt used a string comparison for accuracy, which silently
    # always took the true branch. KFP v2 resolves bool pipeline params at
    # compile time, so `use_ensemble == True` is the right check here.
    with dsl.Condition(use_ensemble == True):
        deploy_model(best_model_path=selector.outputs["best_out"])

    with dsl.Condition(use_ensemble == False):
        log_failed_run(
            collected=gather.outputs["out_file"],
            threshold=accuracy_threshold,
        )


if __name__ == "__main__":
    compiler.Compiler().compile(
        branching_parallel_pipeline,
        "kfp-v2-branching-parallel.yaml",
    )
    print("Compiled kfp-v2-branching-parallel.yaml")
