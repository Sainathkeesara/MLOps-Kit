---
last_verified: 2026-07-11
tool_version: n/a
sources:
  - https://docs.wandb.ai/guides/configure
  - https://docs.wandb.ai/guides/track/launch
  - https://docs.wandb.ai/guides/technical-issues/offline-mode
  - https://docs.wandb.ai/guides/integrations/pytorch
  - https://docs.wandb.ai/guides/sweeps
---

# Running through the official W&B quickstart — what worked and what tripped me

Wrote this after following `docs.wandb.ai/quickstart` on 2026-07-11. Nothing fancy, just the real-world friction.

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

## Got stuck on

### 1. API key hygiene

`wandb login` stores the key in `~/.netrc`. I initially copy-pasted the key into a notebook cell and committed it to a scratch repo. The quickstart doesn't warn you about this. Lesson: add `.netrc` and `.env` to `.gitignore` immediately.

### 2. Project vs run hierarchy

I called `wandb.init()` with no project and ended up with runs scattered across a default " Uncategorized" project. Comparison was impossible. The fix is `wandb.init(project="my-project")` — but the quickstart shows this inline without explaining the hierarchy, so beginners miss it.

### 3. Offline mode silently buffers

I set `WANDB_MODE=offline` while debugging on a train with no wifi. Runs saved locally fine. But I almost deleted the `wandb` folder thinking it was stale cache — that would have nuked the history. The quickstart mentions offline mode but doesn't emphasize that data is kept for later sync.

### 4. `wandb.watch()` duplicates metrics

I called `wandb.watch(model)` inside my training loop by accident. Each call adds another logger, so metrics got logged 3x per step. Moved it outside the loop and added a guard flag. The quickstart doesn't show `wandb.watch()` at all, so I had to find this in the integrations docs.

### 5. Sweep config needs `metric` and `goal`

I wrote a sweep config and forgot the `goal` field. Got `ValueError: Invalid sweep config`. The quickstart's sweep example includes it, but when I adapted it for my own metric name I dropped it by accident.

## What I'd try next

- Use `wandb.init(project="x", entity="team")` to log to a shared project so I can see the team view
- Wire the sweep into a one-line bash script so I can cancel it mid-flight and resume
