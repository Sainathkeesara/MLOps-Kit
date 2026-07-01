import wandb
import random

# first run — passing config as a dict to wandb.init
wandb.init(
    project="mlops-kit-first-run",
    config={"learning_rate": 0.01, "batch_size": 32, "epochs": 5},
)

for step in range(5):
    loss = random.uniform(0.1, 0.9) / (step + 1)
    acc = 1.0 - loss
    wandb.log({"step": step, "loss": loss, "acc": acc})

wandb.finish()
