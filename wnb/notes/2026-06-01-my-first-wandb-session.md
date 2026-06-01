# wnb-004 — my first W&B tracking session

I already read the wnb-002 primer, so I had the basics down before touching the keyboard. Today I installed W&B for real and ran a tracking session end to end.

**install & auth**

1. `pip install wandb`
2. `wandb login` — it printed a URL and asked for an API key. I opened the URL, signed in on WandB, grabbed the key from the page, and pasted it into the terminal.
3. Once the key was accepted, W&B printed a confirmation. That's all the auth I needed — no separate server, no OAuth beyond that key.

**first script**

I wrote a minimal Python script:

```python
import wandb

wandb.init(
    project="wnb-004-session",
    config={
        "learning_rate": 0.001,
        "epochs": 5,
    },
)

for epoch in range(config.epochs):
    loss = 0.5 * (0.9 ** epoch)
    accuracy = 0.5 + 0.1 * epoch
    wandb.log({"loss": loss, "accuracy": accuracy})

wandb.finish()
```

**result**

When the script finished, W&B printed a direct URL to the run page. Clicking it opened the dashboard with my metrics charted across epochs. Runs tab showed both runs from today. I was surprised that the free tier already supports unlimited personal projects, so I could iterate without worrying about quotas mid-learning.

**what I'll try next**

I'd like to log an artifact — a saved model file — so I can learn the full versioning loop: log, download, and compare across runs.