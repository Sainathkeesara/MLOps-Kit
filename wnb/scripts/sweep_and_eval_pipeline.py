"""Reusable sweep + evaluation pipeline with W&B Python SDK.

Modular pipeline that defines a hyperparameter sweep, runs it through a
W&B agent, collects results, and evaluates the best configuration against
a held-out test set. Works with any sklearn-compatible estimator.

Usage:
    python sweep_and_eval_pipeline.py create --project my-project
    python sweep_and_eval_pipeline.py launch <sweep_id> --project my-project --count 20
    python sweep_and_eval_pipeline.py evaluate <sweep_id> --entity my-entity --project my-project
    python sweep_and_eval_pipeline.py run --project my-project --count 20
"""

import argparse
import sys
from typing import Any, Dict, Optional

import wandb
from sklearn.datasets import load_breast_cancer, load_diabetes
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    mean_squared_error,
    precision_score,
    r2_score,
    recall_score,
)
from sklearn.model_selection import train_test_split


TASK_MAP = {
    "classification": {
        "loader": load_breast_cancer,
        "estimator": RandomForestClassifier,
        "metrics": {"accuracy": accuracy_score, "f1": f1_score, "precision": precision_score, "recall": recall_score},
    },
    "regression": {
        "loader": load_diabetes,
        "estimator": RandomForestRegressor,
        "metrics": {"mse": mean_squared_error, "r2": r2_score},
    },
}


def build_sweep_config(
    method: str = "bayes",
    metric_name: str = "accuracy",
    metric_goal: str = "maximize",
    n_estimators: Optional[list] = None,
    max_depth: Optional[list] = None,
    min_samples_split: Optional[Dict[str, int]] = None,
    min_samples_leaf: Optional[Dict[str, int]] = None,
) -> Dict[str, Any]:
    """Return a sweep configuration dict with sensible defaults."""
    config: Dict[str, Any] = {
        "method": method,
        "metric": {"name": metric_name, "goal": metric_goal},
        "parameters": {
            "n_estimators": {"values": n_estimators or [50, 100, 200]},
            "max_depth": {"values": max_depth or [3, 5, 7, None]},
            "min_samples_split": {"min": min_samples_split["min"], "max": min_samples_split["max"]}
            if min_samples_split
            else {"min": 2, "max": 10},
            "min_samples_leaf": {"min": min_samples_leaf["min"], "max": min_samples_leaf["max"]}
            if min_samples_leaf
            else {"min": 1, "max": 5},
        },
    }
    return config


def load_data(task_type: str):
    """Load dataset and split into train/test.

    This is one way to wire it; the docs also suggest loading data outside
    the training function and passing it via a closure if the dataset is large.
    """
    loader_info = TASK_MAP.get(task_type)
    if loader_info is None:
        raise ValueError(f"Unsupported task type: {task_type}. Choose from {list(TASK_MAP.keys())}")
    X, y = loader_info["loader"](return_X_y=True)
    return train_test_split(X, y, test_size=0.2, random_state=42)


def train() -> None:
    """Training function called by the W&B agent for each sweep run."""
    with wandb.init() as run:
        config = run.config

        task_type = config.get("task_type", "classification")
        X_train, X_test, y_train, y_test = load_data(task_type)
        estimator_cls = TASK_MAP[task_type]["estimator"]

        kwargs: Dict[str, Any] = {"random_state": 42}
        if task_type == "classification":
            kwargs["n_estimators"] = config.get("n_estimators", 100)
            kwargs["max_depth"] = config.get("max_depth")
            kwargs["min_samples_split"] = config.get("min_samples_split", 2)
            kwargs["min_samples_leaf"] = config.get("min_samples_leaf", 1)
        else:
            kwargs["n_estimators"] = config.get("n_estimators", 100)
            kwargs["max_depth"] = config.get("max_depth")

        model = estimator_cls(**{k: v for k, v in kwargs.items() if v is not None})
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        for name, metric_fn in TASK_MAP[task_type]["metrics"].items():
            wandb.log({name: metric_fn(y_test, preds)})


def create_sweep(project: str, task_type: str, sweep_config: Optional[Dict[str, Any]] = None) -> str:
    """Register the sweep config and return a sweep ID."""
    if sweep_config is None:
        sweep_config = build_sweep_config()
    sweep_config["parameters"]["task_type"] = {"value": task_type}
    sweep_id = wandb.sweep(sweep_config, project=project)
    print(f"Created sweep: {sweep_id}")
    return sweep_id


def launch_agent(sweep_id: str, project: str, count: int) -> None:
    """Start the sweep agent for a given sweep ID."""
    wandb.agent(sweep_id, function=train, count=count, project=project)


def evaluate_sweep(entity: str, project: str, sweep_id: str) -> None:
    """Query the W&B API for sweep results and print the best run."""
    api = wandb.Api()
    sweep = api.sweep(f"{entity}/{project}/{sweep_id}")

    metric_name = sweep.config.get("metric", {}).get("name", "accuracy")
    goal = sweep.config.get("metric", {}).get("goal", "maximize")

    runs = sorted(
        sweep.runs,
        key=lambda r: r.summary.get(metric_name, 0),
        reverse=(goal == "maximize"),
    )

    if not runs:
        print("No runs found for this sweep.")
        return

    best = runs[0]
    print(f"Sweep ID:      {sweep_id}")
    print(f"Total runs:    {len(runs)}")
    print(f"Best run ID:   {best.id}")
    for key in TASK_MAP.get(sweep.config.get("parameters", {}).get("task_type", {}).get("value", "classification"), {}).get("metrics", {}):
        val = best.summary.get(key)
        if val is not None:
            print(f"{key:14s} {val:.4f}")
    print(f"Parameters:    {dict(best.config)}")


def run_full_pipeline(project: str, task_type: str, count: int) -> None:
    """Create a sweep, launch the agent, and print evaluation results."""
    sweep_config = build_sweep_config()
    sweep_id = create_sweep(project, task_type, sweep_config)
    launch_agent(sweep_id, project, count)
    evaluate_sweep(wandb.Api().default_entity, project, sweep_id)


def main() -> None:
    parser = argparse.ArgumentParser(description="W&B sweep + evaluation pipeline")
    parser.add_argument("--project", default="sweep-eval-demo", help="W&B project name")

    sub = parser.add_subparsers(dest="command", required=True)

    create_parser = sub.add_parser("create", help="Register a new sweep config")
    create_parser.add_argument("--task", choices=["classification", "regression"], default="classification")

    launch_parser = sub.add_parser("launch", help="Launch the sweep agent")
    launch_parser.add_argument("sweep_id", help="Sweep ID to run")
    launch_parser.add_argument("--count", type=int, default=10, help="Number of sweep runs")

    eval_parser = sub.add_parser("evaluate", help="Print best run from a sweep")
    eval_parser.add_argument("sweep_id", help="Sweep ID to analyze")
    eval_parser.add_argument("--entity", default="my-entity", help="W&B entity name")

    run_parser = sub.add_parser("run", help="Create, launch, and evaluate in one command")
    run_parser.add_argument("--task", choices=["classification", "regression"], default="classification")
    run_parser.add_argument("--count", type=int, default=10, help="Number of sweep runs")

    args = parser.parse_args()

    if args.command == "create":
        create_sweep(args.project, args.task)
    elif args.command == "launch":
        launch_agent(args.sweep_id, args.project, args.count)
    elif args.command == "evaluate":
        evaluate_sweep(args.entity, args.project, args.sweep_id)
    elif args.command == "run":
        run_full_pipeline(args.project, args.task, args.count)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
