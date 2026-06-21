"""
Evaluation script for selecting best model from W&B sweep.

Queries the W&B API for sweep runs, identifies the best performing run
by F1 score, and downloads the associated model artifact.
"""

import argparse
import pickle

import wandb


def main():
    parser = argparse.ArgumentParser(description="Evaluate best model from sweep")
    parser.add_argument("--sweep-id", required=True, help="W&B sweep ID")
    parser.add_argument("--entity", required=True, help="W&B entity")
    parser.add_argument("--project", required=True, help="W&B project")
    parser.add_argument("--threshold", type=float, default=0.9, help="Min F1 threshold")
    args = parser.parse_args()

    api = wandb.Api()
    sweep = api.sweep(f"{args.entity}/{args.project}/{args.sweep_id}")

    runs = sorted(
        sweep.runs,
        key=lambda r: r.summary.get("f1", 0),
        reverse=True,
    )

    if not runs:
        print("No runs found in sweep")
        return

    best_run = runs[0]
    best_f1 = best_run.summary.get("f1", 0)

    print(f"Best run: {best_run.id}")
    print(f"F1 score: {best_f1:.4f}")
    print(f"Params: {best_run.config}")

    if best_f1 >= args.threshold:
        artifacts = best_run.logged_artifacts()
        for artifact in artifacts:
            if artifact.type == "model":
                download_path = artifact.download()
                print(f"Downloaded model to: {download_path}")
                break


if __name__ == "__main__":
    main()