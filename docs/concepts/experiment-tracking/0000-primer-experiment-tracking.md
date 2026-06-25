# Experiment Tracking — quick primer

> First-day notes on Experiment Tracking. What it is, why it matters, and the key ideas to know.

## What is it?

Experiment tracking is the practice of recording what you did during an ML training run so you can look it up later and compare it against other runs. It's like git for your experiments: instead of just saving model files, you log the hyperparameters, the dataset version, the metrics (accuracy, loss, etc.), and the artifacts (model weights, plots, configs) — all tied to a single run ID.

I think of it as a lab notebook for ML. Before tools like MLflow or Weights & Biases existed, people would copy-paste training scripts into a Google Doc or keep a text file with param values. That works until you have twenty runs and can't remember which one used the learning rate of 0.001 vs 0.0001.

## Why does it matter for MLOps?

Without experiment tracking, you can't know what changed between a model that scored 85% and one that scored 92%. You end up re-running things, guessing, or — worse — shipping a model that you can't reproduce.

In an MLOps workflow, experiment tracking is the foundation everything else builds on:
- It gives you a searchable history of every run across the team.
- It lets you compare runs side-by-side (this param setup vs that one).
- It feeds the model registry — you register a winning run, not a loose file on disk.
- It makes failures debug-able: you can see what metrics looked like at step 100 vs step 500.

Every tool in the MLOps ecosystem assumes you have experiment tracking in place. If you skip it, you're working blind.

## Key terminology

- **Run** — A single execution of a training script, logged under a unique ID. Example: training a classifier on 10 epochs with learning rate 0.01 — that's one run.
- **Parameter (or hyperparameter)** — A configuration value you set before training. Example: `learning_rate=0.001`, `batch_size=32`.
- **Metric** — A numeric value computed during or after training. Example: `accuracy=0.92`, `loss=0.35` logged per epoch.
- **Artifact** — A file produced by a run: model weights, plots, dataset snapshots, config files. Example: the `.pth` file saved after the last epoch.
- **Run ID** — A unique identifier for each run (often a UUID or timestamp). Example: `exp_2026_06_23_abc123`.
- **Experiment** — A collection of related runs that share a goal. Example: "hyperparameter sweep for the fraud model" is one experiment containing 50 runs.
- **Dashboard** — The UI where you browse runs, compare curves, and search by metric or parameter.

## A concrete example

```python
# Pseudo-code showing what experiment tracking captures
import mlflow  # or wandb, or any tracker

mlflow.start_run(run_name="lr-0-001")
mlflow.log_param("learning_rate", 0.001)
mlflow.log_param("model_type", "random_forest")

for epoch in range(10):
    acc = train_one_epoch(epoch)
    mlflow.log_metric("accuracy", acc, step=epoch)

mlflow.log_artifact("model.pkl")
mlflow.end_run()
```

This logs two params, a per-epoch accuracy curve, and a model file — all linked under one run ID so I can find it later.

## How this connects to what's next

Experiment tracking unlocks the model registry (you need to know which run produced the best model before you can register it) and makes collaboration possible across a team. Once you have tracking in place, you're ready to move into pipeline orchestration and automated retraining.
