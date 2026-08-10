# last_verified: 2026-08-10 · model-registry n/a

"""Automated model versioning and promotion workflow (L3).

This script demonstrates a pipeline that trains a model, logs it to an
experiment run, registers it in the model registry, evaluates the staging
version against a configurable metric threshold, and automatically transitions
it to Production when the threshold is met.

The automation layer — the threshold check and the conditional stage
transition — is the part that would be embedded in a CI job. The registry
client calls are written for MLflow's MlflowClient API; other registries
expose equivalent methods, so only the client layer changes.

Usage:
    python automated-model-promotion-workflow.py
    python automated-model-promotion-workflow.py --threshold 0.90
    python automated-model-promotion-workflow.py --no-promote
"""

from __future__ import annotations

import argparse
import sys

import mlflow
import mlflow.sklearn
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

MODEL_NAME = "automated-demo-model"
ARTIFACT_PATH = "model"


def train_and_log_sample() -> dict:
    """Train a small classifier and log it to a new MLflow run."""
    X, y = make_classification(
        n_samples=400, n_features=8, n_classes=2, random_state=42
    )
    X_tr, X_val, y_tr, y_val = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    model = RandomForestClassifier(n_estimators=30, random_state=42)
    model.fit(X_tr, y_tr)
    val_accuracy = accuracy_score(y_val, model.predict(X_val))

    with mlflow.start_run(run_name="auto-promote-run") as run:
        mlflow.log_metric("val_accuracy", val_accuracy)
        mlflow.sklearn.log_model(model, artifact_path=ARTIFACT_PATH)
        run_id = run.info.run_id

    return {"run_id": run_id, "val_accuracy": val_accuracy}


def register_new_version(run_info: dict) -> int:
    """Register the logged model as a new version and move it to Staging."""
    client = mlflow.tracking.MlflowClient()
    model_uri = f"runs:/{run_info['run_id']}/{ARTIFACT_PATH}"

    mv = client.create_model_version(
        name=MODEL_NAME, source=model_uri, run_id=run_info["run_id"]
    )
    version = int(mv.version)

    client.transition_model_version_stage(
        name=MODEL_NAME, version=str(version), stage="Staging"
    )
    return version


def evaluate_staging_model() -> dict:
    """Load the current Staging model and score it on fresh synthetic data.

    In a real pipeline the validation set would be a held-out slice of the
    training data or a dedicated validation table. A synthetic sample is
    used here so the script is self-contained.
    """
    model = mlflow.sklearn.load_model(f"models:/{MODEL_NAME}/Staging")

    X, y = make_classification(
        n_samples=100, n_features=8, n_classes=2, random_state=99
    )
    val_accuracy = accuracy_score(y, model.predict(X))

    return {"metric": "val_accuracy", "score": val_accuracy}


def meets_promotion_gate(metrics: dict, threshold: float) -> bool:
    """Return True when the staging model's metric clears the threshold."""
    return metrics["score"] >= threshold


def promote_to_production(version: int) -> None:
    """Transition a Staging version to Production, archiving the prior one.

    ``archive_existing_versions`` ensures only one model holds the Production
    stage at any time, which is the safer default for automated pipelines.
    """
    client = mlflow.tracking.MlflowClient()
    client.transition_model_version_stage(
        name=MODEL_NAME,
        version=str(version),
        stage="Production",
        archive_existing_versions=True,
    )


def run_pipeline(threshold: float, auto_promote: bool) -> int:
    """Execute the full train → register → evaluate → promote pipeline."""
    print("Step 1: train and log a model")
    run_info = train_and_log_sample()
    print(f"  run {run_info['run_id']} — val_accuracy={run_info['val_accuracy']:.4f}")

    print("Step 2: register as a new model version")
    version = register_new_version(run_info)
    print(f"  version {version} → Staging")

    print("Step 3: evaluate the Staging model")
    metrics = evaluate_staging_model()
    print(f"  {metrics['metric']}={metrics['score']:.4f} (threshold={threshold})")

    if auto_promote and meets_promotion_gate(metrics, threshold):
        print("Step 4: auto-promote to Production")
        promote_to_production(version)
        print(f"  version {version} → Production (archived prior)")
        return 0

    status = "threshold met" if metrics["score"] >= threshold else "threshold not met"
    print(f"  version {version} stays in Staging ({status})")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Automated model versioning + promotion workflow"
    )
    parser.add_argument(
        "--threshold", type=float, default=0.85,
        help="Minimum staging metric value required for Production promotion",
    )
    parser.add_argument(
        "--no-promote", action="store_true",
        help="Train and register only; skip the auto-promotion step",
    )
    args = parser.parse_args()

    try:
        return run_pipeline(
            threshold=args.threshold,
            auto_promote=not args.no_promote,
        )
    except Exception as exc:
        print(f"Pipeline failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
