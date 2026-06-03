import wandb
import random

# not sure if this is the right pattern yet but it works
wandb.init(project="first-snippet", config={"lr": 0.01, "epochs": 5})

for i in range(5):
    loss = random.random()
    acc = random.random()
    wandb.log({"epoch": i, "loss": loss, "accuracy": acc})

wandb.finish()
