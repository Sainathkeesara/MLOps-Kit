#!/usr/bin/env python
# last_verified: 2026-07-05 · MLflow 2.16.0
# mfl-028 — End-to-end experiment with MLflow tracking, model logging, and registry registration (L2)
# I wanted to see the full flow end-to-end: track a run, log the model, get it into the registry.

import mlflow
from mlflow.models import infer_signature
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("iris-classifier")

# starting a run — need this block for everything else
with mlflow.start_run(run_name="rf-baseline") as run:
    run_id = run.info.run_id
    print(f"Run ID: {run_id}")

    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    params = {"n_estimators": 100, "max_depth": 5, "random_state": 42}
    mlflow.log_params(params)

    clf = RandomForestClassifier(**params)
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(y_test, preds),
        "precision": precision_score(y_test, preds, average="weighted"),
        "recall": recall_score(y_test, preds, average="weighted"),
    }
    mlflow.log_metrics(metrics)

    # infer_signature saves the input/output schema so the served model knows what to expect
    signature = infer_signature(X_test, preds)
    model_info = mlflow.sklearn.log_model(
        sk_model=clf,
        artifact_path="model",
        signature=signature,
        registered_model_name="IrisRandomForest",
    )
    print(f"Model logged at: {model_info.model_uri}")

    # separate call to register — I tried passing registered_model_name alone first
    # but it didn't put the model in the registry, just tagged the run artifact
    model_version = mlflow.register_model(
        model_uri=f"runs:/{run_id}/model",
        name="IrisRandomForest",
    )
    print(f"Registered version: {model_version.version}")

    client = mlflow.MlflowClient()
    client.transition_model_version_stage(
        name="IrisRandomForest",
        version=model_version.version,
        stage="Staging",
    )
    print("Moved to Staging — ready for validation")
