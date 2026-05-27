import wandb
import random

wandb.init(project="mlops-kit-first-run")
wandb.config.learning_rate = 0.01
wandb.config.epochs = 10

for epoch in range(10):
    loss = random.uniform(0.1, 1.0) / (epoch + 1)
    acc = 1.0 - loss
    wandb.log({"epoch": epoch, "loss": loss, "acc": acc})

wandb.finish()
