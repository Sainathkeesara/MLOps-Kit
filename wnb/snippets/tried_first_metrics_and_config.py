import wandb

wandb.init(project="mlops-kit-first-metrics")
wandb.config.learning_rate = 0.01
wandb.config.batch_size = 32

for i in range(5):
    wandb.log({"loss": 0.5 - i * 0.1, "accuracy": 0.5 + i * 0.1})

wandb.finish()
