"""CLI helper to run the Metaflow pipeline with configurable parameters."""

import argparse
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description="Run the Metaflow ML pipeline")
    parser.add_argument("--test-size", type=float, default=0.2, help="Test split fraction")
    parser.add_argument("--n-estimators", type=int, default=100, help="RandomForest tree count")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--with-batch", action="store_true", help="Run with AWS Batch")
    args = parser.parse_args()

    cmd = [
        sys.executable, "flow.py", "run",
        "--test_size", str(args.test_size),
        "--n_estimators", str(args.n_estimators),
        "--seed", str(args.seed),
    ]
    if args.with_batch:
        cmd.extend(["--with", "batch"])

    result = subprocess.run(cmd, check=False)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
