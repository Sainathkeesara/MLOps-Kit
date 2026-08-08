# last_verified: 2026-08-08 · wnb n/a

"""Hyperparameter sweep runner for W&B with PyTorch.

Loads sweep configuration from a YAML file and runs the training
script inside a W&B sweep agent context.
"""

import argparse
import yaml

import wandb
from train import main as train_main


def load_sweep_config(config_path):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def run_sweep(sweep_id, config_path):
    config = load_sweep_config(config_path)
    wandb.agent(sweep_id, function=train_main, count=config.get("count", 10))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a W&B hyperparameter sweep")
    parser.add_argument("--sweep-id", required=True, help="W&B sweep ID from the sweep config")
    parser.add_argument("--config", default="configs/sweep-config.yaml", help="Path to sweep config YAML")
    args = parser.parse_args()

    run_sweep(args.sweep_id, args.config)
