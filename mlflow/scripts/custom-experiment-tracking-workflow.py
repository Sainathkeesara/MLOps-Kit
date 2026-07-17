#!/usr/bin/env python
# last_verified: 2026-07-17 · MLflow n/a
"""Custom MLflow experiment tracking workflow with artifact logging.

Purpose: demonstrate a reusable experiment workflow that spans multiple
runs, logs parameters/metrics/artifacts, compares results, and promotes
the best model — all from a single script.

Steps:
  1. Set up tracking URI and experiment.
  2. Train several model configurations in separate runs.
  3. Log parameters, metrics, and artifacts (feature importance plot).
  4. Query runs via search API and select the best.
  5. Register the best model in the Model Registry.

Verify: run the script with a local MLflow server (mlflow ui); the
final assertion confirms the best model is registered in Production.
"""

import argparse
import os
import tempfile
from typing import Any

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import mlflow
from mlflow.entities import Run
from mlflow.tracking import MlflowClient
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Custom MLflow experiment tracking workflow"
    )
    parser.add_argument(
        "--tracking-uri",
        default="http://127.0.0.1:5000",
        help="MLflow tracking server URI (default: http://127.0.0.1:5000)",
    )
    parser.add_argument(
        "--experiment-name",
        default="custom-experiment-workflow",
        help="MLflow experiment name (default: custom-experiment-workflow)",
    )
    return parser.parse_args()


def setup_experiment(experiment_name: str) -> str:
    experiment = mlflow.get_experiment_by_name(experiment_name)
    if experiment is None:
        experiment_id = mlflow.create_experiment(experiment_name)
        print(f"Created experiment '{experiment_name}' (id={experiment_id})")
    else:
        experiment_id = experiment.experiment_id
        print(f"Using existing experiment '{experiment_name}' (id={experiment_id})")
    mlflow.set_experiment(experiment_name)
    return experiment_id


def train_configs(
    X_train: Any, X_test: Any, y_train: Any, y_test: Any
) -> dict[str, Run]:
    """Train three RandomForest configurations and log each as a run."""
    configs = [
        {"n_estimators": 50, "max_depth": 3, "min_samples_leaf": 2},
        {"n_estimators": 100, "max_depth": 5, "min_samples_leaf": 1},
        {"n_estimators": 200, "max_depth": 7, "min_samples_leaf": 1},
    ]

    runs: dict[str, Run] = {}
    for i, params in enumerate(configs):
        run_name = f"rf-config-{i+1}"
        with mlflow.start_run(run_name=run_name) as run:
            mlflow.log_params(params)

            clf = RandomForestClassifier(**params, random_state=42)
            clf.fit(X_train, y_train)
            preds = clf.predict(X_test)

            acc = accuracy_score(y_test, preds)
            mlflow.log_metric("accuracy", acc)

            _log_feature_importance_artifact(clf, X_train.shape[1])

            model_info = mlflow.sklearn.log_model(
                sk_model=clf,
                artifact_path="model",
                registered_model_name="IrisRandomForest",
            )
            print(
                f"  [{run_name}] accuracy={acc:.4f}, "
                f"model_uri={model_info.model_uri}"
            )
            runs[run_name] = run
    return runs


def _log_feature_importance_artifact(
    model: RandomForestClassifier, n_features: int
) -> None:
    """Generate a feature importance bar chart and log it as an artifact.

    Saves to a temporary directory so it doesn't pollute the working tree.
    """
    importances = model.feature_importances_
    feature_labels = [f"feature_{i}" for i in range(n_features)]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(feature_labels, importances)
    ax.set_xlabel("Importance")
    ax.set_title("Random Forest Feature Importance")

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "feature_importance.png")
        fig.savefig(path, bbox_inches="tight")
        plt.close(fig)
        mlflow.log_artifact(path, artifact_path="plots")


def select_best_run(
    experiment_id: str, metric: str = "accuracy"
) -> Run | None:
    """Query all runs in the experiment and return the best by metric."""
    client = MlflowClient()
    runs = client.search_runs(
        experiment_ids=[experiment_id],
        order_by=[f"metrics.{metric} DESC"],
        max_results=1,
    )
    if not runs:
        return None
    best = runs[0]
    print(
        f"Best run: {best.info.run_name} "
        f"(run_id={best.info.run_id}, {metric}={best.data.metrics.get(metric):.4f})"
    )
    return best


def register_best_model(best_run: Run) -> None:
    """Register the best run's model and promote to Production."""
    client = MlflowClient()
    run_id = best_run.info.run_id
    model_uri = f"runs:/{run_id}/model"

    try:
        mv = client.get_latest_versions("IrisRandomForest", stages=["None"])
        current_stage = mv[0].current_stage if mv else None
    except Exception:
        current_stage = None

    if current_stage != "Production":
        result = mlflow.register_model(model_uri=model_uri, name="IrisRandomForest")
        client.transition_model_version_stage(
            name="IrisRandomForest",
            version=result.version,
            stage="Production",
            archive_existing_versions=True,
        )
        print(
            f"Registered and promoted version {result.version} to Production"
        )
    else:
        print("Best model is already in Production — skipping registration")


def verify(best_run: Run | None) -> None:
    assert best_run is not None, "No runs found — training may have failed"
    run_id = best_run.info.run_id
    loaded = mlflow.pyfunc.load_model(f"runs:/{run_id}/model")
    X, y = load_iris(return_X_y=True)
    preds = loaded.predict(X)
    acc = accuracy_score(y, preds)
    print(f"Verify: loaded model accuracy = {acc:.4f}")
    assert acc > 0.8, f"Model accuracy {acc:.4f} is below threshold"


def main() -> None:
    args = parse_args()

    mlflow.set_tracking_uri(args.tracking_uri)
    experiment_id = setup_experiment(args.experiment_name)

    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    runs = train_configs(X_train, X_test, y_train, y_test)

    best = select_best_run(experiment_id)

    if best:
        register_best_model(best)
        verify(best)
    else:
        print("No runs found — cannot select or register a model")


if __name__ == "__main__":
    main()
