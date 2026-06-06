"""Minimal experiment tracking with Weights & Biases Python API (first cut)."""

import wandb
import random

# logging metrics only — I kept it dead simple to make sure `wandb.log()` works
wandb.init(project="mlops-kit-demo", name="minimal-tracking")
try:
    for step in range(20):
        wandb.log({"train/accuracy": random.random(), "train/loss": random.random()})
finally:
    wandb.finish()
