# MLflow — quick primer

> First-day notes for someone who's never used MLflow. Personal voice, plain language.

## What is it?

MLflow is a tool for keeping track of machine learning experiments. When I train models, I typically juggle a bunch of things: different datasets, hyperparameter settings, library versions, and generated metrics. Without a system, I just print stuff to the console and maybe save a CSV file. MLflow fixes that — it gives me one place to log, track, and compare all of my training runs and model outputs.

## What does it do?

Three main things: **Tracking** (log parameters, metrics, and artifacts for each run), **Projects** (package ML code so anyone can reproduce it), and **Models** (save and version trained models in a standard format). The Tracking piece is the one I reach for most — I can log a learning rate, an accuracy score, and a model file with a few lines of Python and then pull a UI to compare runs.

## Why does it exist?

Before MLflow, ML teams versioned their runs with ad hoc spreadsheets, shared drives full of model folders, and copy-pasted Jupyter cells. It was messy and nobody could reliably reproduce someone else's experiment. MLflow addresses that gap by making the tracking part automated and queryable.

## Key terminology

- **Experiment** — A named container for related runs. Example: create an experiment called `iris-classifier` to hold all runs for that model.
- **Run** — A single execution of training code. Example: one training loop with specific settings = one run.
- **Parameter** — A configurable value like learning rate. Example: `learning_rate = 0.01`.
- **Metric** — A measured value like accuracy or loss. Example: `accuracy = 0.94`.
- **Artifact** — Any file produced by a run, like a model file or plot. Example: `model.pkl`.
- **Tracking Server** — The backend service that stores runs remotely so the whole team can see them. Example: start it with `mlflow ui`.

## A tiny example

```python
import mlflow

mlflow.set_experiment("my-first-experiment")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.94)
```

This creates one run under `my-first-experiment` and logs a parameter and a metric. I'll see it in the UI after starting the server.

## What I'll cover next

After this primer I plan to start the MLflow UI locally, run through a quick end-to-end workflow, and write a short script that actually trains a tiny model and logs everything properly.
