# W&B: first team experiment setup

I already had `wandb` installed (from earlier sessions). This time I wanted to set up a team experiment — configure project settings and get a shared experiment going.

First I logged in with `wandb login` — same API key dance as before. Then I created a team on the W&B web UI (Settings > Teams > Create team). Invited a colleague by email.

For the project config, I set up `wandb/settings` in my repo with a default project and entity:

```python
import wandb
wandb.init(project="team-demo", entity="my-team")
```

Ran a simple training script with `wandb.log()` for loss and accuracy. Teammate could see the runs in the team dashboard right away.

What I noticed: by default W&B creates a new run every time you run the script. For team experiments, I set `wandb.init(reinit=False)` and used `run_id` to resume — that way teammates can pick up where someone left off.

The W&B dashboard for teams shows all runs from all members in one view. The "Sweeps" tab is where hyperparameter tuning lives. I configured a grid search sweep with a YAML config and launched it with `wandb sweep sweep.yaml` then `wandb agent <sweep-id>`. It distributed runs across my machine.

I'm still figuring out the artifact system — attaching datasets to runs seems useful for reproducibility but the API is a bit verbose. Might dig into that next.
