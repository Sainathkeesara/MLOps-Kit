---
last_verified: 2026-07-19
tool_version: n/a
sources:
  - https://docs.metaflow.org/metaflow/introduction
  - https://docs.metaflow.org/metaflow/basics
---

# How I wired Metaflow with Weights & Biases for real-time metric tracking across parallel steps

> This is one way to wire Metaflow foreach branches to W&B so that metrics from each parallel step appear in the dashboard during flow execution — not just after all branches finish.

## Purpose

Metaflow's `foreach` fans out a step across multiple values, and each branch runs in its own process. If you init W&B once before the fan-out, only the parent process can log — the branches have no access. If each branch shares a single W&B run ID, they fight over the same network socket and metrics get interleaved or dropped.

The pattern here gives each branch its own W&B run. Metrics appear in the dashboard in real time as each branch executes, and the join step collects the run IDs so you can trace back from the parent flow to each child.

## Steps

### 1. Define a flow with foreach

The outer flow fans out over a list of hyperparameter values. Each branch trains with its own value.

```python
from metaflow import FlowSpec, step

class ParallelWandbFlow(FlowSpec):
    @step
    def start(self):
        self.hparams = [0.001, 0.01, 0.1]
        self.next(self.train_branch, foreach="hparams")

    @step
    def join(self, inputs):
        self.next(self.end)

    @step
    def end(self):
        pass
```

### 2. Initialize a per-branch W&B run

Inside the branch step, each process calls `wandb.init` with a unique run name so the dashboard shows one run per branch.

```python
import wandb
from metaflow import FlowSpec, step, current

class ParallelWandbFlow(FlowSpec):
    @step
    def start(self):
        self.hparams = [0.001, 0.01, 0.1]
        self.next(self.train_branch, foreach="hparams")

    @step
    def train_branch(self):
        lr = self.input
        run = wandb.init(
            project="metaflow-foreach-demo",
            config={"learning_rate": lr},
            name=f"train-lr-{lr}-{current.run_id}"
        )
        for epoch in range(10):
            loss = 1.0 / (epoch + 1) - lr * epoch
            wandb.log({"epoch": epoch, "loss": loss})
        run.finish()
        self.wandb_run_id = run.id
        self.next(self.join)

    @step
    def join(self, inputs):
        self.wandb_run_ids = [inp.wandb_run_id for inp in inputs]
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == "__main__":
    ParallelWandbFlow()
```

Key details:
- `wandb.init` is called fresh inside each branch — no shared run ID.
- The run `name` includes the learning rate and the Metaflow run ID so you can identify which flow + branch produced it.
- `run.finish()` ensures the run is closed cleanly when the branch completes.
- The join step collects all child run IDs into `self.wandb_run_ids`.

### 3. Run it

```bash
python parallel_wandb_flow.py run
```

The flow fans out to three branches. Each branch starts a W&B run and logs per-epoch loss. Open the W&B project page while the flow is still running — metrics appear branch by branch as they finish.

## Verify

1. Run the flow and open the W&B project `metaflow-foreach-demo`.
2. Confirm three runs appear, named `train-lr-0.001-<run_id>`, `train-lr-0.01-<run_id>`, and `train-lr-0.1-<run_id>`.
3. Click into each run and confirm the `loss` metric has 10 data points (epochs 0–9).
4. After the flow completes, check that the join step's `wandb_run_ids` artifact contains the three run IDs. You can inspect it with `python parallel_wandb_flow.py dump` or via the Metaflow UI.

## What tripped me up

- **Shared run ID across branches** — My first attempt passed the same `wandb.run.id` from the start step to all branches using `resume="must"`. This caused `UsageError` because the SDK tried to sync from multiple processes to the same run endpoint. Giving each branch its own run solved it.
- **W&B not available under `@conda`** — If your flow uses `@conda`, you need to add `wandb` to the `libraries` dict explicitly. I switched to `@pypi` which uses pip and installs wandb without the conda overhead:

  ```python
  from metaflow import pypi

  @pypi(packages=["wandb"])
  @step
  def train_branch(self):
      ...
  ```

- **Run names not showing in dashboard** — If you forget `run.finish()`, the run stays in a "running" state in W&B. Metrics still log, but the run won't appear in the project's default view until it finishes or times out.

## What I'd try next

- Add a join-step artifact that logs all child run names and final metrics as a single W&B table so the parent run becomes a summary dashboard.
- Wire the `@environment` decorator with `WANDB_API_KEY` instead of hardcoding the login, so the flow works in CI without interactive auth.
- Try the Metaflow `spin` command for faster iteration on the branch logic without re-running from start each time.
