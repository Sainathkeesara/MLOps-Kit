# last_verified: 2026-07-04
# wnb-032 — Log my first experiment with W&B Python SDK (L1)

import wandb
import random

# not sure if I'm doing this right but wandb.init() sets up the run
wandb.init(project="hello-wandb", config={"lr": 0.01, "epochs": 5})

for step in range(5):
    loss = 1.0 / (step + 1) + random.uniform(-0.05, 0.05)
    wandb.log({"step": step, "train_loss": loss})

wandb.finish()
