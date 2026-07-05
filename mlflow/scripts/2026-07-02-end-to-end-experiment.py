# last_verified: 2026-07-05 · mlflow 2.14.0

"""End-to-end MLflow experiment: train, log, register, and promote models.

Purpose: Demonstrate full experiment lifecycle with tracking server, model
logging via autolog, and Model Registry registration with stage transitions.

Steps:
  1. Connect to tracking server and create/get experiment
  2. Enable sklearn autologging for automatic params/metrics capture
  3. Train multiple models, compare performance
  4. Register best model to Model Registry
  5. Promote through Staging to Production stages

Verify: Run this script after starting tracking server, check UI for logged runs
and registered model versions.
"""

import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

TRACKING_URI = "http://localhost:5000"
EXPERIMENT_NAME = "wine-classification-experiment"
MODEL_NAME = "WineClassifier"


def train_and_log(model_cls, name, params, X_train, X_test, y_train, y_test):
    """Train a model and log it to MLflow with autologging."""
    with mlflow.start_run(run_name=name):
        model = model_cls(**params)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        mlflow.log_metrics({"test_accuracy": acc})
        return {"name": name, "accuracy": acc, "run_id": mlflow.active_run().info.run_id}


def main():
    mlflow.set_tracking_uri(TRACKING_URI)
    mlflow.set_experiment(EXPERIMENT_NAME)

    # Enable autologging before training
    mlflow.sklearn.autolog(log_models=True)

    X, y = load_wine(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    candidates = [
        (RandomForestClassifier, "random-forest", {"n_estimators": 50}),
        (LogisticRegression, "logistic-regression", {"max_iter": 300}),
    ]

    results = [
        train_and_log(cls, name, params, X_train, X_test, y_train, y_test)
        for cls, name, params in candidates
    ]

    best = max(results, key=lambda r: r["accuracy"])
    print(f"Best model: {best['name']} (accuracy={best['accuracy']:.3f})")

    # Register to Model Registry
    client = MlflowClient()
    model_uri = f"runs:/{best['run_id']}/model"
    try:
        reg = mlflow.register_model(model_uri, MODEL_NAME)
        print(f"Registered as version {reg.version}")
        # Transition to Staging
        client.transition_model_version_stage(
            name=MODEL_NAME,
            version=reg.version,
            stage="Staging",
            archive_existing_versions=True,
        )
        print(f"Transitioned to Staging")
    except Exception as e:
        print(f"Registration error: {e}")

    # Print summary
    runs = client.search_runs(
        experiment_ids=[mlflow.get_experiment_by_name(EXPERIMENT_NAME).experiment_id],
        order_by=["metrics.test_accuracy DESC"],
    )
    for run in runs:
        print(f"  {run.data.tags.get('mlflow.runName', '?')}: acc={run.data.metrics.get('test_accuracy', '?')}")


if __name__ == "__main__":
    main()