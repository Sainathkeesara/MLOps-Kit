import mlflow
import random

mlflow.set_experiment("demo-metrics")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("batch_size", 32)
    for step in range(10):
        acc = 0.5 + step * 0.05 + random.uniform(-0.02, 0.02)
        mlflow.log_metric("accuracy", acc, step=step)
