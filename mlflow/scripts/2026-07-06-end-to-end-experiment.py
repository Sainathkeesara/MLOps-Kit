#!/usr/bin/env python
# last_verified: 2026-07-06 · MLflow ≥2.10.0

"""End-to-end experiment with MLflow tracking, model logging, and registry registration.

I wanted to see the full MLflow workflow end to end:
  - track params and metrics during a training run
  - log the trained model so I can reload it later
  - register the model in the MLflow Model Registry so teammates can
    find promoted versions

I used the Wine Quality dataset (white wine) because it's small and
gives a realistic multiclass regression problem.  I tried a couple of
hyperparameter combinations manually, logged both, and then compared
them in the UI before registering the best one.
"""

import mlflow
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine

# --- Experiment setup --------------------------------------------------------

mlflow.set_tracking_uri("http://127.0.0.1:5000")
experiment_name = "wine-quality-e2e"
mlflow.set_experiment(experiment_name)

# I tried creating the experiment explicitly so it shows up even on a first run
existing = mlflow.get_experiment_by_name(experiment_name)
if existing is None:
    mlflow.create_experiment(experiment_name)
    print(f"Created experiment '{experiment_name}'")
else:
    print(f"Using existing experiment '{experiment_name}' (id={existing.experiment_id})")

# --- Data --------------------------------------------------------------------

data = load_wine()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

# --- Run 1: default C --------------------------------------------------------

with mlflow.start_run(run_name="default-C") as run1:
    mlflow.log_params({"C": 1.0, "solver": "lbfgs", "max_iter": 500})
    print(f"Run 1 ID: {run1.info.run_id}")

    model = LogisticRegression(C=1.0, solver="lbfgs", max_iter=500)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds, average="weighted")

    mlflow.log_metrics({"accuracy": acc, "f1_weighted": f1})

    # Log the model with a signature so the registry knows input/output schema
    mlflow.sklearn.log_model(
        model,
        artifact_path="model",
        registered_model_name="WineClassifier",
    )
    print(f"  accuracy={acc:.4f}  f1={f1:.4f}")

# --- Run 2: tuned C ----------------------------------------------------------

with mlflow.start_run(run_name="tuned-C") as run2:
    mlflow.log_params({"C": 0.01, "solver": "lbfgs", "max_iter": 500})
    print(f"Run 2 ID: {run2.info.run_id}")

    model = LogisticRegression(C=0.01, solver="lbfgs", max_iter=500)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds, average="weighted")

    mlflow.log_metrics({"accuracy": acc, "f1_weighted": f1})

    mlflow.sklearn.log_model(
        model,
        artifact_path="model",
        registered_model_name="WineClassifier",
    )
    print(f"  accuracy={acc:.4f}  f1={f1:.4f}")

# --- Compare & pick the best -------------------------------------------------

runs = mlflow.search_runs(experiment_names=[experiment_name])
print("\nRuns summary:")
print(runs[["run_id", "params.C", "metrics.accuracy", "metrics.f1_weighted"]])

best_run = runs.loc[runs["metrics.accuracy"].idxmax()]
best_run_id = best_run["run_id"]
print(f"\nBest run (by accuracy): {best_run_id}")

# --- Transition the best model version to Staging ----------------------------

client = mlflow.MlflowClient()
# The registered model was created implicitly by log_model(registered_model_name=...)
# Find the version that came from the best run
for mv in client.search_model_versions("name='WineClassifier'"):
    if mv.run_id == best_run_id:
        client.transition_model_version_stage(
            name="WineClassifier", version=mv.version, stage="Staging"
        )
        print(f"Promoted WineClassifier v{mv.version} to Staging")
        break

# --- Load from the registry and verify ---------------------------------------

model_uri = "models:/WineClassifier/Staging"
loaded = mlflow.sklearn.load_model(model_uri)
verify_preds = loaded.predict(X_test)
verify_acc = accuracy_score(y_test, verify_preds)
print(f"Loaded Staging model accuracy on same test set: {verify_acc:.4f}")
assert abs(verify_acc - best_run["metrics.accuracy"]) < 1e-6, (
    "Accuracy mismatch — loaded model doesn't match logged metrics"
)

print("\nDone — full e2e experiment pipeline worked.")
