---
last_verified: 2026-08-11
tool_version: n/a
---

# Installing W&B and logging my first run

First go at getting Weights & Biases running. Kept it to the bare minimum — install, login, one run.

**What I did**

```bash
pip install wandb
wandb login
```

`wandb login` asked for an API key. I grabbed it from the account page and pasted it in — it said the key was saved, no further setup needed.

Then a tiny script:

```python
import wandb

wandb.init(project="hello-first-run")
wandb.log({"loss": 0.5})
wandb.finish()
```

**What surprised me**

- `wandb.init(project=...)` created the project automatically — I didn't have to make it in the UI first.
- After `wandb.finish()` the terminal printed a link to the run page, and the metric showed up on the dashboard almost immediately.
- If I forget `wandb.finish()`, the run shows as crashed. Easy to trip on.

**What I'll try next**

Loop a few training epochs and log loss each step so the chart actually curves instead of a single point.