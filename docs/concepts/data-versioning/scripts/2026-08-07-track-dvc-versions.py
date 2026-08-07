# last_verified: 2026-08-07 · dvc 3.67.1

"""
con-087 — Practice: track dataset versions with DVC and reproduce a training run (L2)

This script uses the actual `dvc` CLI to version a dataset, make a
modification, and restore the original version to reproduce the same
training run. I chose DVC's CLI over its Python SDK because the CLI
is what most tutorials show and it keeps the pointer-file concept
visible on disk.

The script runs entirely in a temp workspace so it won't touch your
real project files. It needs `dvc` installed (`pip install dvc`) and
a working git user.name/email in the environment.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SAMPLE_CSV = "sample_data.csv"
TRAIN_SCRIPT = "train.py"
DVC_DIR = ".dvc"


# ── Helpers ───────────────────────────────────────────────────────────────


def run(cmd: list[str], cwd: Path) -> None:
    """Run a shell command, printing it so the learner can follow along."""
    print(f"$ {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.rstrip())
    if result.returncode != 0:
        # surface the error so the learner can see what went wrong
        print(result.stderr.rstrip(), file=sys.stderr)
        raise RuntimeError(f"command failed: {' '.join(cmd)}")


def write_sample(path: Path) -> None:
    """Write a small CSV with two versions so we can see the diff."""
    v1 = "id,value\n1,10\n2,20\n3,30\n"
    path.write_text(v1)


def write_train_script(path: Path) -> None:
    """A tiny training stand-in that logs the data version it sees."""
    path.write_text(
        "import csv, sys\n"
        'data = csv.DictReader(open("sample_data.csv"))\n'
        "rows = list(data)\n"
        "total = sum(int(r['value']) for r in rows)\n"
        "print(f\"Training on {len(rows)} rows, sum={total}\")\n"
        'open("model_metric.txt", "w").write(str(total))\n'
    )


def read_metric(path: Path) -> str:
    return path.read_text().strip() if path.exists() else "missing"


# ── Main workflow ─────────────────────────────────────────────────────────


def main() -> None:
    if shutil.which("dvc") is None:
        print("DVC is not installed. Run: pip install dvc", file=sys.stderr)
        sys.exit(1)

    # run everything inside a temp directory so nothing leaks out
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
    train_after_update = workspace / "model_metric_after_update.txt"
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

    # cleanup temp workspace
    shutil.rmtree(workspace)


if __name__ == "__main__":
    main()
