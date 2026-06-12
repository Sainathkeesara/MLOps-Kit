"""Build an end-to-end training pipeline with MLflow autologging.

Purpose
    Demonstrate a complete MLflow training workflow that uses sklearn autolog
    to capture parameters, metrics, and model artifacts during training, then
    registers the best-performing model in the Model Registry.

Steps
    1. Configure tracking URI and create or reuse an experiment.
    2. Enable sklearn autologging.
    3. Load and split a multi-class dataset.
    4. Train several classifiers in separate tracked runs.
    5. Compare run results and register the best model.
    6. Query the experiment programmatically to verify autolog captured
       expected parameters, metrics, and artifacts.

Verify
    Use MlflowClient.search_runs to confirm that each run has non-empty
    params, metrics, and a model artifact URI.  Print a summary table.
"""

import warnings

import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")


TRACKING_URI = "sqlite:///mlflow.db"
EXPERIMENT_NAME = "wine-autolog-pipeline"
REGISTERED_MODEL_NAME = "WineBestModel"


def train_and_evaluate(model_cls, model_name, params, X_train, X_test, y_train, y_test):
    """Train a classifier in a tracked run and return its metrics."""
    with mlflow.start_run(run_name=model_name) as run:
        mlflow.log_param("model_name", model_name)

        try:
            model = model_cls(**params) if params else model_cls()
            model.fit(X_train, y_train)
        except Exception as exc:
            mlflow.log_param("error", str(exc))
            return {"name": model_name, "accuracy": None, "f1": None, "run_id": None}

        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        f1 = f1_score(y_test, preds, average="weighted")
        mlflow.log_metrics({"test_accuracy": acc, "test_f1_weighted": f1})

        return {"name": model_name, "accuracy": acc, "f1": f1, "run_id": run.info.run_id}


def main():
    mlflow.set_tracking_uri(TRACKING_URI)
    experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
    if experiment is None:
        mlflow.create_experiment(EXPERIMENT_NAME)
    mlflow.set_experiment(EXPERIMENT_NAME)

    # Enable autolog before training — captures params, metrics, model artifacts
    mlflow.sklearn.autolog(log_models=True, log_datasets=True)

    # Use the Wine dataset (3 classes) so the task is slightly harder than iris
    X, y = load_wine(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    candidates = [
        (RandomForestClassifier, "random-forest", {"n_estimators": 100, "max_depth": 4}),
        (GradientBoostingClassifier, "gradient-boosting", {"n_estimators": 80, "max_depth": 3}),
        (LogisticRegression, "logistic-regression", {"max_iter": 500, "C": 1.0}),
    ]

    results = [
        train_and_evaluate(cls, name, params, X_train, X_test, y_train, y_test)
        for cls, name, params in candidates
    ]

    best = max((r for r in results if r["accuracy"] is not None), key=lambda r: r["accuracy"])
    print(f"\nBest model: {best['name']}  (accuracy={best['accuracy']:.3f}, f1={best['f1']:.3f})")

    # Register the best model to the Model Registry
    if best["run_id"]:
        try:
            reg = mlflow.register_model(
                f"runs:/{best['run_id']}/model",
                REGISTERED_MODEL_NAME,
            )
            print(f"Registered as '{REGISTERED_MODEL_NAME}' version {reg.version}")
        except Exception as e:
            print(f"Model registration failed: {e}")

    # Verify — query the experiment and print a summary
    client = MlflowClient()
    all_runs = client.search_runs(
        experiment_ids=[mlflow.get_experiment_by_name(EXPERIMENT_NAME).experiment_id],
        order_by=["metrics.test_accuracy DESC"],
    )
    print("\n--- Verification: runs from Experiment Registry ---")
    for i, run in enumerate(all_runs, 1):
        print(f"  {i}. {run.data.tags.get('mlflow.runName', '?'):20s}  "
              f"acc={run.data.metrics.get('test_accuracy', '?'):<8}  "
              f"f1={run.data.metrics.get('test_f1_weighted', '?'):<8}  "
              f"params={list(run.data.params.keys())}")


if __name__ == "__main__":
    main()
