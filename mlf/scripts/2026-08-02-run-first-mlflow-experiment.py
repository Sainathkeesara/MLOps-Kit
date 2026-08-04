# last_verified: 2026-08-04 · MLflow 3.15.1
# mlf-025 — Run my first MLflow experiment and log a model artifact (L1)
# I wanted to see how MLflow tracks a run end-to-end: start, log, save.

import mlflow

mlflow.set_experiment("first-experiment")

with mlflow.start_run() as run:
    mlflow.log_param("model", "linear-regression")
    mlflow.log_metric("accuracy", 0.92)
    mlflow.log_artifact(__file__, artifact_path="scripts")
    print(f"Run {run.info.run_id} logged")