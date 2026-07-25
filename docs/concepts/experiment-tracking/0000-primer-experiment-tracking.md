---
last_verified: 2026-07-25
tool_version: n/a
sources: []
---

# Experiment Tracking — quick primer

> First-day notes on Experiment Tracking. What it is, why it matters, and the key ideas to know.

## What is it?

I just learned that experiment tracking is basically a lab notebook for ML work. When you train a model you change a bunch of things — the learning rate, the number of layers, which dataset you used — and after a few runs you can't remember which combination gave you the best result. Experiment tracking is the practice of recording every run's inputs and outputs so you can look them up later. It's like git for your training attempts.

## Why does it matter for MLOps?

When I'm doing ML work, I run experiments constantly. Without tracking, I'd be copy-pasting results into a spreadsheet or, worse, relying on memory. Here's why it matters day-to-day for an MLOps practitioner:

- I can compare runs side by side (this hyperparameter setup vs that one) to see what actually works.
- I know exactly which data version and code state produced a given model, so I can reproduce it later if needed.
- When something goes wrong — like accuracy dropping after a code change — I can trace back through runs to figure out what changed.
- It feeds the model registry later on, because I need to know which run produced the best model before I can register it.

## Key terminology

- **Run** — One execution of a training script, logged with a unique ID. Example: I ran `train.py` with learning rate 0.01 for 10 epochs — that's one run.
- **Parameter** — A value I set before training starts. Example: `learning_rate=0.001`, `batch_size=32`, `optimizer=adam`.
- **Metric** — A number that gets computed during or after training, like accuracy or loss. Example: `accuracy=0.92` at the end of a run.
- **Artifact** — A file that a run produces — model weights, a plot, a config file. Example: the `model.pkl` I save after training finishes.
- **Experiment** — A group of related runs that share a goal. Example: "hyperparameter sweep for the credit model" is one experiment containing dozens of runs.
- **Tracking URI** — Where the tracking tool stores its data (a local folder, a database, or a server address). Example: a local server address like `127.0.0.1:5000` for a local MLflow server.

## A concrete example

Here's what a minimal experiment-tracking session looks like in Python:

```python
import mlflow

mlflow.start_run(run_name="lr-0-001")
mlflow.log_param("learning_rate", 0.001)
mlflow.log_param("model_type", "random_forest")

acc = train_and_evaluate()
mlflow.log_metric("accuracy", acc)
mlflow.log_artifact("model.pkl")
mlflow.end_run()
```

This logs two parameters, one metric, and one model file — all tied to a single run so I can find it in the UI later.

## How this connects to what's next

Experiment tracking unlocks the model registry (you need the run ID to link back to the training details) and makes team collaboration possible (everyone can see what everyone else tried). Next I'll want to practice logging multiple metrics per run and comparing them in a UI.