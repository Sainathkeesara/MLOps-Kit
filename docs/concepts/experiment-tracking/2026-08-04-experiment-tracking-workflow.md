---
last_verified: 2026-08-04
tool_version: 3.15.1
sources:
  - https://mlflow.org/docs/latest/self-hosting/troubleshooting/
---

# Experiment tracking workflow — logging params, metrics, and artifacts end-to-end

> Following the MLflow quickstart, here is how I wired up experiment tracking from scratch.

## What is it?

Experiment tracking is the practice of recording every detail of a training run — what hyperparameters I chose, what metrics I got, and which model artifacts I produced — so I can compare runs later and reproduce results. It is like keeping a lab notebook, but automated and searchable. MLflow is the most common tool for this in the Python ML ecosystem.

## Why does it matter?

Before experiment tracking, I used to rename folders like `run_final_v2` and lose track of which config produced which result. With experiment tracking, every run is logged with a unique ID, and I can query runs by metric value, parameter, or tag. This matters because I cannot improve what I cannot measure, and I cannot reproduce what I cannot trace.

## Key terminology

- **Run** — a single execution of a training script. Example: `mlflow.start_run()` opens a run and all subsequent log calls attach to it.
- **Parameter** — an input knob I set before training. Example: `mlflow.log_param("lr", 0.001)` records the learning rate.
- **Metric** — a numeric measurement I record during or after training. Example: `mlflow.log_metric("accuracy", 0.95)` records the final accuracy.
- **Artifact** — a file produced by a run, like a saved model or a plot. Example: `mlflow.log_artifact("model.pkl")` uploads the pickled model.
- **Experiment** — a container that groups related runs. Example: `mlflow.set_experiment("churn-prediction")` directs all runs into one bucket.

## A concrete example

I wrote a small script that logs a parameter, a metric, and an artifact in one run:

```python
import mlflow

mlflow.set_experiment("demo")
with mlflow.start_run():
    mlflow.log_param("lr", 0.01)
    mlflow.log_metric("accuracy", 0.92)
    mlflow.log_artifact("model.pkl")
```

This shows the core loop: set the experiment, start a run, log the three things, and close the run.

## How this connects to what's next

Once I can log runs consistently, the next step is to compare them side by side in the MLflow UI and to automate the comparison across multiple hyperparameter configurations. The MLflow Model Registry then lets me promote the best run's model from staging to a deployed serving endpoint.
