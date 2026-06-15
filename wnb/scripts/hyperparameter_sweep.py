"""Build a hyperparameter sweep with W&B from scratch.

Defines a sweep config, a training function that reports metrics back to W&B,
and CLI commands to create, launch, and analyze sweeps.
"""

import argparse
import sys

import wandb
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split


SWEEP_CONFIG = {
    "method": "bayes",
    "metric": {"name": "accuracy", "goal": "maximize"},
    "parameters": {
        "n_estimators": {"values": [50, 100, 200]},
        "max_depth": {"values": [3, 5, 7, None]},
        "min_samples_split": {"min": 2, "max": 10},
        "min_samples_leaf": {"min": 1, "max": 5},
    },
    "early_terminate": {"type": "hyperband", "min_iter": 3},
}


def train() -> None:
    """Training function called by the W&B agent for each sweep run."""
    with wandb.init() as run:
        config = run.config

        X, y = load_iris(return_X_y=True)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = RandomForestClassifier(
            n_estimators=config.get("n_estimators", 100),
            max_depth=config.get("max_depth"),
            min_samples_split=config.get("min_samples_split", 2),
            min_samples_leaf=config.get("min_samples_leaf", 1),
            random_state=42,
        )
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        accuracy = accuracy_score(y_test, preds)
        precision = precision_score(y_test, preds, average="weighted")
        recall = recall_score(y_test, preds, average="weighted")

        wandb.log({
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
        })


def create_sweep(project: str) -> str:
    """Register the sweep config and return a sweep ID."""
    sweep_id = wandb.sweep(SWEEP_CONFIG, project=project)
    print(f"Created sweep: {sweep_id}")
    return sweep_id


def launch_agent(sweep_id: str, project: str, count: int) -> None:
    """Start the sweep agent for a given sweep ID."""
    wandb.agent(sweep_id, function=train, count=count, project=project)


def analyze_sweep(entity: str, project: str, sweep_id: str) -> None:
    """Query the W&B API for sweep results and print the best run."""
    api = wandb.Api()
    sweep_path = f"{entity}/{project}/{sweep_id}"
    sweep = api.sweep(sweep_path)

    runs = sorted(
        sweep.runs,
        key=lambda r: r.summary.get("accuracy", 0),
        reverse=True,
    )

    if not runs:
        print("No runs found for this sweep.")
        return

    best = runs[0]
    print(f"Total runs:    {len(runs)}")
    print(f"Best run ID:   {best.id}")
    print(f"Accuracy:      {best.summary.get('accuracy', 'N/A'):.4f}")
    print(f"Precision:     {best.summary.get('precision', 'N/A'):.4f}")
    print(f"Recall:        {best.summary.get('recall', 'N/A'):.4f}")
    print(f"Parameters:    {dict(best.config)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="W&B hyperparameter sweep")
    parser.add_argument("--entity", type=str, default="my-entity", help="W&B entity name")
    parser.add_argument("--project", type=str, default="hyperparam-sweep-demo")
    parser.add_argument("--count", type=int, default=10, help="Number of sweep runs")

    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("create", help="Register a new sweep config")
    launch_parser = sub.add_parser("launch", help="Launch the sweep agent")
    launch_parser.add_argument("sweep_id", type=str, help="Sweep ID to run")
    analyze_parser = sub.add_parser("analyze", help="Print best run from a sweep")
    analyze_parser.add_argument("sweep_id", type=str, help="Sweep ID to analyze")

    args = parser.parse_args()

    if args.command == "create":
        create_sweep(args.project)
    elif args.command == "launch":
        launch_agent(args.sweep_id, args.project, args.count)
    elif args.command == "analyze":
        analyze_sweep(args.entity, args.project, args.sweep_id)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
