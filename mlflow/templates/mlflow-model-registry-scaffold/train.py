#!/usr/bin/env python
# last_verified: 2026-07-24 · MLflow n/a

import argparse
import logging

import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def train(
    tracking_uri: str,
    experiment_name: str,
    n_estimators: int,
    max_depth: int,
    test_size: float,
    random_state: int,
) -> str:
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(experiment_name)

    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    with mlflow.start_run() as run:
        mlflow.log_params({
            "n_estimators": n_estimators,
            "max_depth": max_depth,
            "test_size": test_size,
            "random_state": random_state,
        })

        model = RandomForestClassifier(
            n_estimators=n_estimators, max_depth=max_depth, random_state=random_state
        )
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred, average="weighted"),
            "recall": recall_score(y_test, y_pred, average="weighted"),
            "f1": f1_score(y_test, y_pred, average="weighted"),
        }
        mlflow.log_metrics(metrics)

        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",
            registered_model_name="IrisClassifier",
        )

        logger.info("Run %s — accuracy: %.4f", run.info.run_id, metrics["accuracy"])
        return run.info.run_id


def main():
    parser = argparse.ArgumentParser(description="Train a model and log to MLflow")
    parser.add_argument("--tracking-uri", default="http://localhost:5000")
    parser.add_argument("--experiment-name", default="model-registry-demo")
    parser.add_argument("--n-estimators", type=int, default=100)
    parser.add_argument("--max-depth", type=int, default=5)
    parser.add_argument("--test-size", type=float, default=0.2)
    parser.add_argument("--random-state", type=int, default=42)
    args = parser.parse_args()

    try:
        run_id = train(
            tracking_uri=args.tracking_uri,
            experiment_name=args.experiment_name,
            n_estimators=args.n_estimators,
            max_depth=args.max_depth,
            test_size=args.test_size,
            random_state=args.random_state,
        )
        print(f"Training complete. Run ID: {run_id}")
    except Exception as exc:
        logger.error("Training failed: %s", exc)
        raise


if __name__ == "__main__":
    main()
