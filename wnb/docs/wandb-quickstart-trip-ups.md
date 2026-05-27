# wnb-001 — Following the W&B quickstart: what tripped me up

I went through the official W&B quickstart (`docs.wandb.ai/quickstart`) to log a training run, view a dashboard, and try a sweep. I'd already done a basic `wandb.init()` + `wandb.log()` in the primer phase, so this was about going deeper.

## Steps I followed

1. **Installed wandb** — `pip install wandb` (already had it from before, but I upgraded).
2. **Logged in** — `wandb login` with my API key.
3. **Ran the quickstart script** — a PyTorch training loop that logs loss and accuracy per epoch. W&B captured everything: config, metrics, system stats.
4. **Opened the dashboard** — the terminal prints a direct link to the run page. Charts were rendered instantly.
5. **Set up a simple sweep** — defined a `sweep-config.yaml` with a `grid` search over learning rate and batch size, then launched the sweep agent.

## Where I got stuck

**Stuck 1: The quickstart script uses PyTorch, but I didn't have a GPU.** W&B reported GPU stats as 0 / N/A, which was fine — but the system metrics panel kept showing an empty GPU section that looked broken. Quickstart doesn't mention that the system metrics auto-detect is harmless but ugly if you're CPU-only.

**Stuck 2: Sweep config YAML structure was picky.** My first sweep definition had `metric: "loss"` but the quickstart example used a nested key:

```yaml
metric:
  goal: minimize
  name: loss
```

I used `metric: loss` as a plain string and the sweep creation silently accepted it — but the agent logged no runs. The YAML validation printed a warning buried in debug output. Took me three tries to match the expected shape.

**Stuck 3: Sweep agent needed the project name.** Running `wandb sweep sweep-config.yaml` created the sweep and printed a sweep ID. But `wandb agent <sweep_id>` failed with "no project specified". I expected the sweep to remember the project from the training script's `wandb.init(project="...")`, but the agent needs `wandb agent --project <name> <sweep_id>` explicitly.

**Stuck 4: Offline mode exists but isn't mentioned.** If you're not logged in, `wandb.init()` errors out. The quickstart assumes you're online. I found `wandb.init(mode="offline")` later — handy for testing scripts without API keys, but it's not in the quickstart.

## What I'd try next

- Set up a W&B Artifact to version a trained model checkpoint.
- Try the W&B Panels to build a custom dashboard comparing 10+ sweeps.
- Look into the W&B REST API to query run data programmatically from a notebook.
