# Running through the official W&B quickstart — what worked and what tripped me

Wrote this after following `docs.wandb.ai/quickstart` on 2026-06-06. Nothing fancy, just the real-world friction.

## What worked

The install was smooth:

```bash
pip install wandb
wandb login
```

I pasted my API key from the UI and it said "App key saved." 

The 5-line script in the quickstart ran as-is:

```python
import wandb
wandb.init(project="quickstart-demo")
wandb.log({"acc": 0.9, "loss": 0.4})
```

Yep, 2 runs showed up in the web UI within ~30 seconds of finishing.

## Where I got stuck

1. **JupyterNotebook environment.** I started in a notebook instead of the CLI prompt. `wandb.init()` without `reinit=True` on a kernel restart threw `Error: W&B run has already been initialized`. The quickstart doesn't warn you about restart loops.

2. **Sweep frequency parameter.** I tried `count=50` on `wandb.agent()` and got `TypeError: sweep() got an unexpected keyword argument 'count'`. The API is `wandb.agent(sweep_id, function, count=50)` but I passed `count` to `wandb.sweep()` by mistake. Easy once I re-read the signature.

3. **Logging inside `__main__`.** When I moved the example into a `wandb_quickstart.py` script, `wandb.init()` hung for ~5s on the first run because it spun up the service. Inside a notebook it's silent. Inside a script it prints `wandb: Using wandb service as W&B processes cannot set group permissions in this environment.` Should have expected that, but it's in the quiet font so I missed it.

4. **Config vs. simple `wandb.config`.** I tried to access `wandb.config.lr` before setting it. Quickstart says to use `wandb.config` but doesn't clarify that `config` is a dict-like namespace — individual keys don't exist unless you set them or pass a config dict to `init`.

## What I'd try next

- Use `wandb.init(project="x", entity="team")` to log to a shared project so I can see the team view
- Wire the sweep into a one-line bash script so I can cancel it mid-flight and resume
- Turn on `wandb.log(commit=False)` to understand log-step semantics

---

Quickstart is genuinely good. The snags above are on me for skipping docs, not the tutorial. Recommend reading it once all the way through instead of copy-pasting during the first run as I did.
