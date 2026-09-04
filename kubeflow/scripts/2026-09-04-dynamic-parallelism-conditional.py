# last_verified: 2026-09-04 · kub n/a
"""kub-043 — KFP v2 pipeline with dynamic parallelism and conditional execution.

This pipeline demonstrates the two patterns I kept running into when
building real KFP v2 workflows:

1. Dynamic parallelism — the ParallelFor loop items come from a
   component's runtime output, not a hardcoded Python list. A
   generate_splits component produces JSON-encoded fold configs, and
   a parse_folds component converts them into the list that
   ParallelFor iterates over.

2. Conditional execution — after training, dsl.Condition branches
   on accuracy: deploy if above threshold, log failure otherwise.

I initially tried passing the raw string output of generate_splits
directly into ParallelFor, but KFP v2 needs the items to be a list
type at compile time. Wrapping the parse step in a separate component
that returns List[str] fixes the type mismatch.
"""

import json
import tempfile
import os

from kfp import dsl, compiler


@dsl.component(base_image="python:3.9-slim")
def generate_splits(raw_csv: str, n_folds: int) -> str:
    """Split raw CSV data into N cross-validation folds.

    Returns a JSON-encoded list of fold configurations, each containing
    the train/test split indices and the fold number.
    """
    lines = raw_csv.strip().splitlines()
    header = lines[0]
    rows = [l for l in lines[1:] if l.strip()]
    fold_size = len(rows) // n_folds

    folds = []
    for i in range(n_folds):
        start = i * fold_size
        end = start + fold_size if i < n_folds - 1 else len(rows)
        folds.append({
            "fold": i,
            "train_start": 0,
            "train_end": start,
            "test_start": start,
            "test_end": end,
            "header": header,
            "total_rows": len(rows),
        })

    print(f"Generated {len(folds)} folds from {len(rows)} rows")
    return json.dumps(folds)


@dsl.component(base_image="python:3.9-slim")
def parse_folds(folds_json: str) -> list:
    """Parse the JSON-encoded fold list into a Python list for ParallelFor.

    This step exists because KFP v2's ParallelFor needs a List[str] type
    at compile time, but generate_splits returns a str. Without this
    intermediate parse, the compiler raises a type error on the
    ParallelFor items argument.
    """
    folds = json.loads(folds_json)
    print(f"Parsed {len(folds)} folds for parallel training")
    return folds


@dsl.component(base_image="python:3.9-slim")
def train_on_fold(fold_config: str, raw_csv: str, learning_rate: float, n_estimators: int) -> str:
    """Train a model on one cross-validation fold and return the accuracy.

    The fold_config is a JSON string containing split indices. This
    component reads the raw CSV, extracts the train/test split, trains
    a mock sklearn-style model, and returns a JSON artifact with the
    fold number and accuracy.
    """
    import json as _json

    config = _json.loads(fold_config)
    lines = raw_csv.strip().splitlines()
    header = lines[0]
    rows = [l for l in lines[1:] if l.strip()]

    train_rows = rows[config["train_start"]:config["train_end"]]
    test_rows = rows[config["test_start"]:config["test_end"]]

    # Mock training — in a real pipeline this would fit a model.
    # The accuracy is a function of the fold size and hyperparameters
    # so the conditional branch has something meaningful to evaluate.
    fold = config["fold"]
    train_pct = len(train_rows) / config["total_rows"] if config["total_rows"] > 0 else 0
    accuracy = min(0.5 + train_pct * 0.3 + learning_rate * 2 + n_estimators * 0.001, 0.98)

    result = {
        "fold": fold,
        "accuracy": round(accuracy, 4),
        "train_rows": len(train_rows),
        "test_rows": len(test_rows),
    }
    print(f"Fold {fold}: accuracy={accuracy:.4f} (train={len(train_rows)}, test={len(test_rows)})")
    return _json.dumps(result)


@dsl.component(base_image="python:3.9-slim")
def deploy_model(accuracy_results: list, threshold: float):
    """Deploy the model if the mean accuracy exceeds the threshold.

    In a real pipeline this would push to a model registry or apply a
    Kubernetes manifest. Here it prints the decision for verification.
    """
    import json as _json

    results = [_json.loads(r) for r in accuracy_results]
    mean_acc = sum(r["accuracy"] for r in results) / len(results)
    print(f"Mean accuracy: {mean_acc:.4f} (threshold: {threshold})")
    if mean_acc >= threshold:
        print(f"DEPLOY — mean accuracy {mean_acc:.4f} >= {threshold}")
    else:
        print(f"SKIP — mean accuracy {mean_acc:.4f} < {threshold}")


@dsl.component(base_image="python:3.9-slim")
def log_failure(accuracy_results: list, threshold: float):
    """Log failed folds when accuracy is below threshold."""
    import json as _json

    results = [_json.loads(r) for r in accuracy_results]
    mean_acc = sum(r["accuracy"] for r in results) / len(results)
    below = [r for r in results if r["accuracy"] < threshold]
    print(f"Mean accuracy {mean_acc:.4f} below threshold {threshold}")
    for r in below:
        print(f"  Fold {r['fold']}: {r['accuracy']:.4f}")


@dsl.pipeline(
    name="kfp-v2-dynamic-parallelism",
    description="Cross-validation with dynamic fold generation, parallel training, and conditional deployment",
    pipeline_root="s3://my-bucket/kfp-pipelines",
)
def dynamic_parallelism_pipeline(
    raw_csv: str = "x,1\ny,2\nz,3\na,4\nb,5\nc,6\nd,7\ne,8\nf,9\ng,10\nh,11\ni,12\nj,13",
    n_folds: int = 3,
    learning_rate: float = 0.05,
    n_estimators: int = 100,
    accuracy_threshold: float = 0.7,
):
    # ── Step 1: generate cross-validation folds dynamically ──
    # The fold count comes from a pipeline parameter, not a hardcoded
    # list — this is the "dynamic" part of dynamic parallelism.
    splits = generate_splits(raw_csv=raw_csv, n_folds=n_folds)

    # ── Step 2: parse folds into a list for ParallelFor ──
    # KFP v2's ParallelFor needs a List[str] type at compile time, but
    # generate_splits returns a str. This intermediate component
    # bridges the type gap.
    folds = parse_folds(folds_json=splits.output)

    # ── Step 3: train on each fold in parallel ──
    # ParallelFor iterates over the dynamically generated fold list.
    # Each iteration trains independently; results are collected as a
    # list of artifacts that downstream components consume.
    with dsl.ParallelFor(items=folds.output) as fold_config:
        train_result = train_on_fold(
            fold_config=fold_config,
            raw_csv=raw_csv,
            learning_rate=learning_rate,
            n_estimators=n_estimators,
        )

    # ── Step 4: conditional deployment ──
    # After all folds complete, check if mean accuracy passes the
    # threshold. The dsl.Condition branch fires only on success.
    with dsl.Condition(train_result.output > accuracy_threshold):
        deploy_model(
            accuracy_results=[train_result.output],
            threshold=accuracy_threshold,
        )

    with dsl.Condition(train_result.output <= accuracy_threshold):
        log_failure(
            accuracy_results=[train_result.output],
            threshold=accuracy_threshold,
        )


if __name__ == "__main__":
    compiler.Compiler().compile(
        dynamic_parallelism_pipeline,
        "kfp-v2-dynamic-parallelism.yaml",
    )
    print("Compiled kfp-v2-dynamic-parallelism.yaml")

    # To run locally, port-forward the KFP service first:
    #   kubectl port-forward -n kubeflow svc/ml-pipeline 8080:80
    # Then uncomment:
    # from kfp import Client
    # client = Client(host="http://localhost:8080")
    # run = client.create_run_from_pipeline_func(
    #     dynamic_parallelism_pipeline,
    #     arguments={
    #         "raw_csv": "x,1\ny,2\nz,3",
    #         "n_folds": 3,
    #         "learning_rate": 0.05,
    #         "n_estimators": 100,
    #         "accuracy_threshold": 0.7,
    #     },
    #     experiment_name="kub-043-test",
    # )
    # print(f"Submitted run: {run.run_id}")
