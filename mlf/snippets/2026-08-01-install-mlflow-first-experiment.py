# last_verified: 2026-08-01 · mlflow n/a

# pip install mlflow

import mlflow

mlflow.set_experiment("my-first-experiment")

with mlflow.start_run(run_name="install-test"):
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.94)
    print("Run logged — check the MLflow UI")