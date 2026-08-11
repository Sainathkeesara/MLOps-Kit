# last_verified: 2026-08-11 · wandb n/a
import wandb

wandb.init(project="first-metric")

for step in range(5):
    wandb.log({"loss": 1.0 / (step + 1)})

wandb.finish()