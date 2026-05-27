# Weights & Biases — first experiment tracking

Installed wandb with `pip install wandb`. Ran `wandb login` and pasted my API key from https://wandb.ai/authorize.

Wrote a quick training script — just a loop that pretends to train on random data. Added `wandb.init()` at the top and `wandb.log({"loss": loss, "acc": acc})` inside the loop. When it finished I opened the link wandb printed and saw the run in the UI.

Stuff that tripped me up:
- Forgot to call `wandb.finish()` — the run kept showing as "running" in the dashboard. Adding it at the end fixed it.
- First run crashed because I passed `project="my-project"` but hadn't created the project first. Turns out wandb creates it automatically — no need to pre-create.

The UI is clean. I can see the loss curve, toggle between runs, and download the raw data as CSV. No server to configure — it just works over the public SaaS.
