"""Minimal experiment tracking with W&B SDK — log metrics and artifacts."""

import wandb
import random
import tempfile
import os

# Start a W&B run — grouping runs under one project keeps the dashboard clean
wandb.init(project="mlops-kit-demo", name="first-snippet-run")

try:
    # Simulate a training loop, logging per-epoch metrics
    # In a real model you'd track loss, accuracy, etc.
    for epoch in range(5):
        loss = random.uniform(0.1, 1.0)
        accuracy = random.uniform(0.7, 0.95)

        wandb.log({"epoch": epoch, "loss": loss, "accuracy": accuracy})

    # Log a summary text as an artifact — this is how you'd store a model file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("Tiny model — 2 layers, 64 units each\nTrained on synthetic data")
        temp_path = f.name

    artifact = wandb.Artifact(name="model-summary", type="model")
    artifact.add_file(temp_path)
    wandb.log_artifact(artifact)
finally:
    wandb.finish()
    os.unlink(temp_path)
