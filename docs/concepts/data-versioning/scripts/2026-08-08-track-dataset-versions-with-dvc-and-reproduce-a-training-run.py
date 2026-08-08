# last_verified: 2026-08-08 · DVC 3.67.1

"""
con-087 — Practice: track dataset versions with DVC and reproduce a training run (L2)

Following the DVC quickstart, I built a small end-to-end demo that tracks
a dataset, mutates it, and then restores the original version to prove
the training run is reproducible. I kept the CLI surface because the
pointer-file model is easier to see when you run the commands yourself.

DVC 3.67.1 [source: https://github.com/treeverse/dvc/releases/tag/3.67.1]
  requires a Git repo before `dvc init` [source: https://doc.dvc.org/install]
  and a `dvc checkout` after `git checkout` to sync pointer files
  [source: https://tildalice.io/dvc-basics-track-ml-dataset-3-commands/].
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SAMPLE_CSV = "sample_data.csv"
TRAIN_SCRIPT = "train.py"


def run(cmd: list[str], cwd: Path) -> None:
    print(f"$ {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.rstrip())
    if result.returncode != 0:
        print(result.stderr.rstrip(), file=sys.stderr)
        raise RuntimeError(f"command failed: {' '.join(cmd)}")


def write_sample(path: Path) -> None:
    v1 = "id,value\n1,10\n2,20\n3,30\n"
    path.write_text(v1)


def write_train_script(path: Path) -> None:
    path.write_text(
        "import csv\n"
        'data = csv.DictReader(open("sample_data.csv"))\n'
        "rows = list(data)\n"
        "total = sum(int(r['value']) for r in rows)\n"
        'open("model_metric.txt", "w").write(str(total))\n'
    )


def read_metric(path: Path) -> str:
    return path.read_text().strip() if path.exists() else "missing"


def main() -> None:
    if shutil.which("dvc") is None:
        print("DVC is not installed. Run: pip install dvc", file=sys.stderr)
        sys.exit(1)

    workspace = Path(tempfile.mkdtemp(prefix="dvc_demo_"))
    print(f"Workspace: {workspace}\n")

    # 1. initialise git first — DVC needs a git repo
    run(["git", "init"], workspace)
    run(["git", "config", "user.email", "learner@example.com"], workspace)
    run(["git", "config", "user.name", "Learner"], workspace)

    # 2. initialise DVC
    run(["dvc", "init"], workspace)

    # 3. create a sample dataset and train
    data = workspace / SAMPLE_CSV
    write_sample(data)
    train = workspace / TRAIN_SCRIPT
    write_train_script(train)

    print("── v1: first training run ──")
    run(["python", TRAIN_SCRIPT], workspace)
    metric_v1 = read_metric(workspace / "model_metric.txt")
    print(f"metric after v1 training: {metric_v1}\n")

    # 4. version the dataset with DVC
    run(["dvc", "add", SAMPLE_CSV], workspace)
    run(["git", "add", ".", ".dvc"], workspace)
    run(["git", "commit", "-m", "v1: track sample_data.csv"], workspace)

    # 5. simulate a data update — someone added a fourth row
    data.write_text("id,value\n1,10\n2,20\n3,30\n4,40\n")
    run(["python", TRAIN_SCRIPT], workspace)
    metric_updated = read_metric(workspace / "model_metric.txt")
    print(f"metric after data update (before re-tracking): {metric_updated}\n")

    # 6. re-track the updated file and commit
    run(["dvc", "add", SAMPLE_CSV], workspace)
    run(["git", "add", ".", ".dvc"], workspace)
    run(["git", "commit", "-m", "v2: updated sample_data.csv"], workspace)

    # 7. restore v1 and reproduce the original training run
    print("── restore v1 and re-train ──")
    run(["git", "checkout", "HEAD~1", "--", "sample_data.csv.dvc"], workspace)
    run(["dvc", "checkout"], workspace)
    run(["python", TRAIN_SCRIPT], workspace)
    metric_restored = read_metric(workspace / "model_metric.txt")
    print(f"metric after restoring v1 data: {metric_restored}\n")

    # 8. confirm we got the original value back
    assert metric_v1 == metric_restored, (
        f"reproduction failed: {metric_v1} != {metric_restored}"
    )
    print("✓ Reproduced the original training result (sum=60).")

    shutil.rmtree(workspace)


if __name__ == "__main__":
    main()
