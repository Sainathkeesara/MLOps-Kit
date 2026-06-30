"""pip install mlflow then log my first experiment."""

import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("first-experiment")

with mlflow.start_run(run_name="install-test-run") as run:
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("batch_size", 32)
    mlflow.log_metric("train_loss", 0.42)
    mlflow.log_metric("val_acc", 0.88)

print(f"Run logged: {run.info.run_id}")
print("View at http://127.0.0.1:5000")
