#!/usr/bin/env python
# last_verified: 2026-07-05 · MLflow n/a
# mfl-028 — End-to-end experiment with MLflow tracking, model logging, and registry registration (L2)
# Walked through the official tutorial but a few things tripped me up — noting them inline.

import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# First gotcha: if you don't set the tracking URI, MLflow logs to a local
# `mlruns` directory by default. That's fine for this experiment, but I
# initially expected it to connect to a server — the docs mention the
# tracking URI but it's easy to miss.
mlflow.set_tracking_uri("")

# Set up the experiment — runs show up under this name in the UI.
mlflow.set_experiment("diabetes-end-to-end")

data = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

with mlflow.start_run(run_name="rf-with-registry") as run:
    params = {
        "n_estimators": 100,
        "max_depth": 6,
        "min_samples_split": 5,
        "random_state": 42,
    }
    mlflow.log_params(params)

    rf = RandomForestRegressor(**params)
    rf.fit(X_train, y_train)

    preds = rf.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    mlflow.log_metrics({"mse": mse, "r2": r2})

    # Registering the model inline during the run. MLflow creates a new
    # version in the Model Registry unless one already exists with the
    # same name, in which case it auto-increments the version number.
    # I tripped on this: you need `registered_model_name=` inside
    # log_model — separate mlflow.register_model() also works but
    # requires the run ID.
    mlflow.sklearn.log_model(
        rf,
        artifact_path="model",
        registered_model_name="DiabetesRandomForest",
    )

    print(f"Run ID: {run.info.run_id}")
    print(f"MSE: {mse:.3f}, R2: {r2:.3f}")
    print("Model 'DiabetesRandomForest' registered — check the UI")
