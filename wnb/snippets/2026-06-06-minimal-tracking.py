"""Minimal experiment tracking with Weights & Biases Python API.

Following the W&B quickstart — logging params, metrics, and keeping track of runs.
"""

import wandb
import random
import math

# start a run with some config — wandb.init() picks up defaults from env if available
wandb.init(
    project="mlops-kit-demo",
    config={
        "learning_rate": 0.01,
        "batch_size": 32,
        "epochs": 5,
    },
)

try:
    for epoch in range(wandb.config["epochs"]):
        # fake training loop — real data would go in here
        loss = 1.0 / (epoch + 1) + random.uniform(-0.05, 0.05)
        accuracy = 1.0 - math.exp(-(epoch + 1) / 2) + random.uniform(-0.02, 0.02)

        # log scalar metrics per step — wandb auto-plots them in the UI
        wandb.log({"epoch": epoch, "train/loss": loss, "train/accuracy": accuracy})

        # try logging a histogram too — saw it in the docs and wanted to test
        if epoch == 0:
            wandb.log({"gradients": wandb.Histogram([random.gauss(0, 1) for _ in range(100)])})
finally:
    wandb.finish()
