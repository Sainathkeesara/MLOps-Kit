"""Minimal model training with MLflow autologging.

L2 — I tried enabling sklearn autolog and training a single classifier
to see what gets captured automatically. Keeping it simple on purpose:
no model registry, no experiment comparison, just autolog + verify.
"""

import mlflow
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def main():
    # Use a local SQLite tracking server so I can inspect runs later
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("autolog-minimal")

    # Must call autolog BEFORE importing sklearn estimators — I learned
    # this the hard way in an earlier run where nothing got logged
    mlflow.sklearn.autolog(log_models=True, log_datasets=True)

    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    with mlflow.start_run(run_name="iris-rf-default"):
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        # autolog already logged params, metrics, and the model artifact
        # I'm logging one extra metric manually to confirm I can mix both
        mlflow.log_metric("test_accuracy", score)

    # Quick verification — fetch the run and print a summary
    run = mlflow.last_active_run()
    if run:
        print(f"Run ID: {run.info.run_id}")
        print(f"Params captured: {list(run.data.params.keys())}")
        print(f"Metrics captured: {list(run.data.metrics.keys())}")
        print(f"Model artifact: {run.info.artifact_uri}/model")
    print("Done — check mlflow.db with: mlflow ui --backend-store-uri sqlite:///mlflow.db")


if __name__ == "__main__":
    main()
