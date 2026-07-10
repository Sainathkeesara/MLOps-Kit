# last_verified: 2026-07-10 · wandb n/a

"""
Minimal hyperparameter sweep with W&B.

Follows the sweep tutorial from the quickstart. I kept it to a single file
so I could iterate fast — the sweep agent calls train() once per trial.
"""

import wandb

SWEEP_CONFIG = {
    "method": "bayes",
    "metric": {"name": "val_acc", "goal": "maximize"},
    "parameters": {
        "lr": {"min": 0.0001, "max": 0.01},
        "batch_size": {"values": [16, 32, 64]},
    },
}

sweep_id = wandb.sweep(SWEEP_CONFIG, project="minimal-sweep")
print(f"Sweep created: {sweep_id}")


def train():
    with wandb.init() as run:
        # using the sweep-suggested params
        lr = wandb.config.lr
        batch_size = wandb.config.batch_size

        # dummy training — real pipeline would load data and train here
        val_acc = 0.5 + 0.4 * (lr / 0.01) - 0.1 * (batch_size / 64)

        wandb.log({"val_acc": val_acc, "lr": lr, "batch_size": batch_size})
        print(f"  trial: lr={lr:.5f}  batch_size={batch_size}  val_acc={val_acc:.3f}")


# runs 5 trials synchronously — I used count=5 for quick feedback
wandb.agent(sweep_id, function=train, count=5)
print("Sweep done — check the dashboard for the parallel coordinates plot")
