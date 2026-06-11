"""Minimal W&B artifact logging — saving model files and datasets.

Trying out wandb.Artifact to store model checkpoints and track
them across runs the way the docs show.
"""

import wandb
import tempfile
import os
import random

wandb.init(project="mlops-kit-demo", name="artifact-logging-try")

try:
    # train a fake model and save it to disk
    model_data = f"lr={0.01},epochs=3,acc={random.uniform(0.8, 0.95):.3f}"

    with tempfile.NamedTemporaryFile(mode="w", suffix=".pkl", delete=False) as f:
        f.write(model_data)
        model_path = f.name

    # log it as an artifact — type="model" groups it in the UI
    artifact = wandb.Artifact(name="toy-classifier", type="model")
    artifact.add_file(model_path)
    wandb.log_artifact(artifact)
    print(f"Logged artifact 'toy-classifier' from {model_path}")

    # also log a small dataset artifact to see how multiple artifacts look
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("feature_a,feature_b,label\n0.1,0.2,0\n0.5,0.3,1\n")
        data_path = f.name

    data_artifact = wandb.Artifact(name="toy-dataset", type="dataset")
    data_artifact.add_file(data_path)
    wandb.log_artifact(data_artifact)
    print(f"Logged artifact 'toy-dataset' from {data_path}")

finally:
    wandb.finish()
    os.unlink(model_path)
    os.unlink(data_path)
