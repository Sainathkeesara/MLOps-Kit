# last_verified: 2026-08-04 · metaflow 2.10.0
"""CLI entrypoint for the Metaflow project scaffold with @project, @schedule, and event-triggered flows."""

import argparse
import subprocess
import sys


def run_flow(flow_name, **kwargs):
    """Run a named Metaflow flow with the given parameters."""
    cmd = [sys.executable, "flow.py", flow_name, "--with", "metadata=local"]
    for key, val in kwargs.items():
        cmd.extend([f"--{key.replace('_', '-')}", str(val)])
    result = subprocess.run(cmd, check=False)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(
        description="Run Metaflow flows from the scaffold"
    )
    parser.add_argument(
        "flow",
        choices=[
            "project",
            "scheduled",
            "event",
        ],
        help="Which flow variant to run",
    )
    parser.add_argument("--dataset", default="iris", help="Dataset name for project flow")
    parser.add_argument("--threshold", type=float, default=0.5, help="Decision threshold")
    parser.add_argument("--commit-sha", default="", help="Commit SHA for event-triggered flow")
    parser.add_argument("--with-batch", action="store_true", help="Run with AWS Batch")
    args = parser.parse_args()

    flow_map = {
        "project": ("ProjectMetadataFlow", {"dataset": args.dataset}),
        "scheduled": ("ScheduledDailyFlow", {"threshold": args.threshold}),
        "event": ("EventTriggeredFlow", {"commit_sha": args.commit_sha}),
    }

    flow_name, params = flow_map[args.flow]
    return run_flow(flow_name, **params)


if __name__ == "__main__":
    sys.exit(main())