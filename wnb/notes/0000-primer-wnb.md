# Weights & Biases — quick primer

> First-day notes for someone who's never used W&B. Personal voice, plain language.

## What is it?

Weights & Biases (W&B) is a platform for tracking machine learning experiments. I think of it like MLflow but with a stronger web UI and more built-in collaboration features. Where MLflow gives you a local server you run yourself, W&B is a hosted service (or self-hosted) that shows you experiment results in a browser dashboard with pretty charts out of the box.

## What does it do?

It logs hyperparameters, training metrics, model outputs, and system metrics (GPU utilization, memory) from your training code and displays them in a real-time dashboard. You can compare runs side by side, group runs into projects, and share links with teammates.

## Why does it exist?

Before platforms like W&B, teams tracked experiments in spreadsheets or just memory. You'd train a model, write down the accuracy somewhere, and with any luck you'd remember which hyperparameters produced it. W&B makes the logging automatic — you add a couple lines of Python to your training loop and everything shows up in the UI instantly. Practitioners reach for it when they need to iterate fast and compare many runs without writing logging infrastructure themselves.

## Key terminology

- **Run** — A single execution of training code. Example: `wandb.init()` starts a run; when the script finishes, the run ends.
- **Project** — A container for related runs. Example: a project called `mnist-classifier` holds all runs for that model family.
- **Config** — Hyperparameters you set before training. Example: `wandb.config.learning_rate = 0.001`.
- **Metrics** — Values logged during training like loss or accuracy. Example: `wandb.log({"accuracy": 0.92})`.
- **Artifact** — A versioned file or dataset produced by a run. Example: save a trained model checkpoint as an artifact.
- **Sweep** — Automated hyperparameter search across many runs. Example: tell W&B to try 50 learning rates between 1e-4 and 1e-1.
- **Dashboard** — The web UI where you see runs, charts, and comparisons.

## A tiny example

```python
import wandb

wandb.init(project="hello-wandb")
wandb.config.learning_rate = 0.01

for epoch in range(5):
    acc = 0.5 + epoch * 0.08
    wandb.log({"epoch": epoch, "accuracy": acc})

wandb.finish()
```

This logs a small run with one config key and 5 metric steps. After running it, I can open the W&B dashboard and see the accuracy curve.

## What I'll cover next

After this primer I want to install the library, run a real training script with W&B tracking, and get comfortable navigating the dashboard.
