"""mflow-012 — Install MLflow and log my first run.

Installed with `pip install mlflow`. Then logged some fake
training params and metrics to see the Tracking API work.
"""

import mlflow

# Started with `mlflow ui` in another terminal
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("mflow-012-first-run")

with mlflow.start_run(run_name="install-test") as run:
    mlflow.log_param("lr", 0.01)
    mlflow.log_param("epochs", 10)
    for step in range(3):
        mlflow.log_metric("loss", 0.5 - step * 0.1, step=step)

print(f"Done. Run: {run.info.run_id} — http://localhost:5000")
