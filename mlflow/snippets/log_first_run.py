"""mlf-003 — Log my first experiment run with MLflow Tracking.

Tiny end-to-end script: create an experiment, start a run,
log a couple of parameters and a metric, and print the run ID.
Nothing fancy — just proving the flow works.
"""

import mlflow

# Point at the local Tracking server started with `mlflow ui`
mlflow.set_tracking_uri("http://localhost:5000")

# Create / reuse an experiment
experiment = mlflow.set_experiment("hello-mlflow")

# One training run
with mlflow.start_run(run_name="first-try") as run:
    # Log a few params
    mlflow.log_param("model_type", "linear_regression")
    mlflow.log_param("n_samples", 100)

    # Fake a metric (pretend we trained for 5 epochs)
    for epoch in range(5):
        acc = 0.50 + epoch * 0.08
        mlflow.log_metric("accuracy", acc, step=epoch)

    print(f"Run ID: {run.info.run_id}")
    print(f"Experiment: {experiment.name}")
    print("Check http://localhost:5000 to see the run!")
