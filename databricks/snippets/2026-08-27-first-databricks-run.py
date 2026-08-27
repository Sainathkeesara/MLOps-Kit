# last_verified: 2026-08-27 · databricks n/a

import mlflow

# Point the MLflow client at the managed tracking server in the Databricks workspace.
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Users/me/first-databricks-run")

with mlflow.start_run():
    mlflow.log_param("model_type", "sentiment_classifier")
    mlflow.log_param("max_depth", 7)

    mlflow.log_metric("train_accuracy", 0.94)
    mlflow.log_metric("val_accuracy", 0.91)

print("Run logged — open the Experiments tab in the workspace to see it.")
