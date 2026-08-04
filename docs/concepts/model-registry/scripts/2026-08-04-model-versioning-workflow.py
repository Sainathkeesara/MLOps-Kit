# last_verified: 2026-08-04 · model-registry

# I wrote this script to practice model versioning and promotion with MLflow Model Registry
# Source: https://mlflow.org/docs/latest/self-hosting/troubleshooting/

import mlflow

client = mlflow.tracking.MlflowClient()

experiment = client.get_experiment_by_name("demo")
run = client.search_runs(experiment.experiment_id, order_by=["metrics.accuracy DESC"])[0]

model_uri = f"runs:/{run.info.run_id}/model"
client.create_model_version(
    name="churn-model",
    source=model_uri,
    run_id=run.info.run_id,
)

client.transition_model_version_stage(
    name="churn-model",
    version=1,
    stage="Staging",
)

print("Model registered and promoted to Staging")
