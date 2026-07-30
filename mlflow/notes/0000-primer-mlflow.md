---
last_verified: 2026-07-30
tool_version: 3.14.0
sources:
  - https://mlflow.org/releases
---

# MLflow — quick primer

> First-day notes for someone who's never used MLflow. Personal voice, plain language.

## What is it?

MLflow tracks machine learning experiments. I juggle datasets, hyperparameters, library versions, and metrics when training. Without one I just print to the console and save CSV files. MLflow gives me one place to log, track, and compare training runs and model outputs.

## What does it do?

Three main things: **Tracking** (log parameters, metrics, and artifacts for each run), **Projects** (package ML code so anyone can reproduce it), and **Models** (save and version trained models). The Tracking piece is the one I reach for most — I can log a learning rate and an accuracy score and then pull a UI to compare runs.

## Why does it exist?

Before MLflow, ML teams versioned their experiments with spreadsheets, shared drives, and copy-pasted cells. It was messy and nobody could reliably reproduce someone else's experiment. MLflow addresses that by making tracking automated and queryable.

## Key terminology

- **Experiment** — A named container for related runs. Example: `iris-classifier`.
- **Run** — A single execution of training code. Example: one training loop = one run.
- **Parameter** — A configurable value like learning rate. Example: `lr = 0.01`.
- **Metric** — A measured value like accuracy or loss. Example: `accuracy = 0.94`.
- **Artifact** — Any file produced by a run, like a model file. Example: `model.pkl`.

## A tiny example

```python
import mlflow

mlflow.set_experiment("my-first-experiment")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.94)
```

This creates one run and logs a parameter and a metric I can see in the UI after starting the server.

## What I'll cover next

I'll start the MLflow UI locally, run through a quick end-to-end workflow, and write a script that trains a tiny model and logs everything properly.
