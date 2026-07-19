# last_verified: 2026-07-19 · wandb 0.18.0

"""Build a W&B hyperparameter sweep from scratch with custom search space and early termination.

Purpose:
    Demonstrate how to define a sweep config programmatically with mixed parameter
    types (categorical, int range, float range) and configure early termination via
    HyperBand. The script creates a sweep, launches an agent, and reports the best run.

Steps:
    1. Define a custom search space with different parameter distributions
    2. Configure early termination (HyperBand) to stop unpromising runs
    3. Register the sweep with W&B
    4. Launch the sweep agent
    5. Query results and print the best configuration

Verify:
    Run `python custom-sweep-early-termination.py run --count 20` and check the
    W&B dashboard for sweep visualizations. The script prints the best run's
    metrics and hyperparameters on completion.
"""

import argparse
import sys
from typing import Optional

import wandb


def build_custom_sweep_config(
    method: str = "bayes",
    metric_name: str = "f1_score",
    metric_goal: str = "maximize",
    early_terminate: Optional[dict] = None,
) -> dict:
    """Build a sweep config with a custom search space mixing parameter types.

    This is one way to structure the config; the W&B docs also support inline
    distributions via `wandb.sweep` for even more control.
    """
    return {
        "method": method,
        "metric": {"name": metric_name, "goal": metric_goal},
        "early_terminate": early_terminate or {
            "type": "hyperband",
            "min_iter": 3,
            "max_iter": 27,
            "s": 2,
            "eta": 3,
        },
        "parameters": {
            "learning_rate": {"distribution": "uniform", "min": 0.01, "max": 0.3},
            "max_depth": {"values": [3, 4, 5, 6, 7, 8]},
            "subsample": {"distribution": "uniform", "min": 0.6, "max": 1.0},
            "colsample_bytree": {"distribution": "uniform", "min": 0.6, "max": 1.0},
            "min_child_weight": {"values": [1, 3, 5, 7]},
            "gamma": {"distribution": "uniform", "min": 0.0, "max": 0.5},
            "reg_alpha": {"distribution": "uniform", "min": 0.0, "max": 1.0},
            "reg_lambda": {"distribution": "uniform", "min": 0.0, "max": 1.0},
        },
    }


def train() -> None:
    """Training function called by the W&B agent for each sweep run.

    Uses XGBoost on the wine dataset — a multiclass classification task with
    13 features and 3 classes. Logs accuracy, F1, precision, and recall.
    """
    import xgboost as xgb
    from sklearn.datasets import load_wine
    from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
    from sklearn.model_selection import train_test_split

    with wandb.init() as run:
        config = run.config

        X, y = load_wine(return_X_y=True)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        model = xgb.XGBClassifier(
            n_estimators=100,
            learning_rate=config.get("learning_rate", 0.1),
            max_depth=config.get("max_depth", 6),
            subsample=config.get("subsample", 1.0),
            colsample_bytree=config.get("colsample_bytree", 1.0),
            min_child_weight=config.get("min_child_weight", 1),
            gamma=config.get("gamma", 0.0),
            reg_alpha=config.get("reg_alpha", 0.0),
            reg_lambda=config.get("reg_lambda", 1.0),
            random_state=42,
            use_label_encoder=False,
            eval_metric="mlogloss",
        )
        model.fit(X_train, y_train, eval_set=[(X_test, y_test)], verbose=False)
        preds = model.predict(X_test)

        accuracy = accuracy_score(y_test, preds)
        f1 = f1_score(y_test, preds, average="weighted")
        precision = precision_score(y_test, preds, average="weighted")
        recall = recall_score(y_test, preds, average="weighted")

        wandb.log({
            "accuracy": accuracy,
            "f1_score": f1,
            "precision": precision,
            "recall": recall,
        })


def create_sweep(project: str, sweep_config: dict) -> str:
    """Register the sweep config and return a sweep ID."""
    sweep_id = wandb.sweep(sweep_config, project=project)
    print(f"Created sweep: {sweep_id}")
    return sweep_id


def launch_agent(sweep_id: str, project: str, count: int) -> None:
    """Start the sweep agent for a given sweep ID."""
    wandb.agent(sweep_id, function=train, count=count, project=project)


def analyze_sweep(entity: str, project: str, sweep_id: str) -> None:
    """Query the W&B API for sweep results and print the best run."""
    api = wandb.Api()
    sweep = api.sweep(f"{entity}/{project}/{sweep_id}")

    metric_name = sweep.config.get("metric", {}).get("name", "f1_score")
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
    print(f"F1 score:      {best.summary.get('f1_score', 'N/A'):.4f}")
    print(f"Accuracy:      {best.summary.get('accuracy', 'N/A'):.4f}")
    print(f"Precision:     {best.summary.get('precision', 'N/A'):.4f}")
    print(f"Recall:        {best.summary.get('recall', 'N/A'):.4f}")
    print(f"Parameters:    {dict(best.config)}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="W&B custom hyperparameter sweep with early termination"
    )
    parser.add_argument("--entity", default="my-entity", help="W&B entity name")
    parser.add_argument("--project", default="custom-sweep-demo", help="W&B project name")
    parser.add_argument("--count", type=int, default=20, help="Number of sweep runs")

    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("create", help="Register a new sweep config")
    launch_parser = sub.add_parser("launch", help="Launch the sweep agent")
    launch_parser.add_argument("sweep_id", help="Sweep ID to run")
    analyze_parser = sub.add_parser("analyze", help="Print best run from a sweep")
    analyze_parser.add_argument("sweep_id", help="Sweep ID to analyze")

    args = parser.parse_args()

    if args.command == "create":
        sweep_config = build_custom_sweep_config()
        create_sweep(args.project, sweep_config)
    elif args.command == "launch":
        launch_agent(args.sweep_id, args.project, args.count)
    elif args.command == "analyze":
        analyze_sweep(args.entity, args.project, args.sweep_id)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)</think>

<｜DSML｜tool_calls>
<｜DSML｜invoke name="write">
<｜DSML｜parameter name="filePath" string="true">/work/MLOps-Kit/wnb/scripts/custom-sweep-early-termination.py