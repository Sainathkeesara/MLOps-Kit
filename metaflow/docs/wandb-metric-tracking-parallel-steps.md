---
last_verified: 2026-07-19
tool_version: n/a
sources:
  - https://docs.metaflow.org/metaflow/introduction
  - https://docs.metaflow.org/metaflow/basics
---

# Metaflow + W&B real-time metric tracking across parallel steps

> How to wire Metaflow `foreach` branches to Weights & Biases so that metrics from each parallel step appear in the dashboard during flow execution, not only after all branches finish.

## Purpose

Metaflow's `foreach` decorator fans a step out across a list of values, and each branch runs as its own process with an independent `current.step_task_id`. A W&B run initialized once in the parent step is not visible to the branches, so sharing a single run ID across all branches causes the SDK to write to the same network endpoint from multiple processes, interleaving or dropping metrics.

The pattern below gives each branch its own W&B run. Metrics stream to the dashboard in real time as each branch executes, and the `join` step collects the per-branch run IDs so a reader can trace from the parent flow to each child run. This is one way to do it; the Metaflow basics docs also describe the single-run-per-step approach for non-parallel flows.

## When to use

| Scenario | Approach |
|---|---|
| Single step logs metrics | Initialize W&B inside the step and call `run.finish()` at the end |
| `foreach` fan-out, per-branch metrics | Initialize a fresh W&B run inside the branch step; collect run IDs in `join` |
| Shared run across sequential steps | Pass a run ID through `self` and re-init with `resume` |
| Branch metrics need flow context | Embed `current.run_id` in the run `name` |

## Prerequisites

- Metaflow installed (`pip install metaflow`)
- `wandb` Python SDK installed (`pip install wandb`)
- W&B account with an API key (`wandb login` or `WANDB_API_KEY` set)
- If using `@conda`/`@pypi`, ensure `wandb` is declared in the branch step's environment

## Steps

### 1. Define a flow with a foreach fan-out

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

Inside the branch step, each process calls `wandb.init` with a unique run name so the dashboard shows one run per branch. Embedding `current.run_id` ties each run back to the originating Metaflow run.

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
- The run `name` includes the learning rate and the Metaflow run ID so the reader can identify which flow and branch produced it.
- `run.finish()` closes the run cleanly when the branch completes.
- The `join` step collects all child run IDs into `self.wandb_run_ids`.

### 3. Run the flow

```bash
python parallel_wandb_flow.py run
```

The flow fans out to three branches. Each branch starts a W&B run and logs per-epoch loss. With the W&B project page open during the run, metrics appear branch by branch as the branches finish.

## Verify

1. Run the flow and open the W&B project `metaflow-foreach-demo`.
2. Confirm three runs appear, named `train-lr-0.001-<run_id>`, `train-lr-0.01-<run_id>`, and `train-lr-0.1-<run_id>`.
3. Click into each run and confirm the `loss` metric has 10 data points (epochs 0–9).
4. After the flow completes, confirm the `join` step's `wandb_run_ids` artifact contains the three run IDs, inspectable with `python parallel_wandb_flow.py dump` or via the Metaflow UI.

## Common errors

- **Shared run ID across branches (`UsageError`):** Passing the same `wandb.run.id` from `start` to all branches with `resume="must"` makes the SDK sync from multiple processes to one run endpoint. Each branch should initialize its own run, as shown above.
- **`wandb` missing under `@conda`:** A flow using `@conda` must declare `wandb` in the `libraries` dict, or the branch process cannot import it. The `@pypi(packages=["wandb"])` decorator installs via pip without conda overhead:

  ```python
  from metaflow import pypi

  @pypi(packages=["wandb"])
  @step
  def train_branch(self):
      ...
  ```

- **Runs stuck in "running" state:** Forgetting `run.finish()` leaves the run open in W&B. Metrics still log, but the run does not resolve in the project's default view until it finishes or times out.

## References

- Metaflow `foreach` and per-branch process model: https://docs.metaflow.org/metaflow/introduction
- Metaflow steps, `self.next`, and fan-out/fan-in basics: https://docs.metaflow.org/metaflow/basics
