# Metaflow + W&B integration: tracking artifacts and metrics across flows

> How to wire Metaflow runs to Weights & Biases for experiment tracking, artifact lineage, and metric dashboards.

## Purpose

Metaflow tracks runs locally with its own metadata service. Weights & Biases provides a centralized dashboard for comparing experiments across team members and machines. This doc shows how to log parameters, metrics, and artifacts from Metaflow steps to W&B so that each flow run appears as a W&B run with full lineage.

The integration is not automatic — there is no Metaflow plugin for W&B yet (as of mid-2026). Each step that needs tracking must initialize its own W&B run or share one across steps. The pattern below is one way to do it; the docs also suggest using the Metaflow `@environment` or `@pypi` decorators to pin `wandb` per step.

## When to use

| Scenario | Approach |
|---|---|
| Single step logs metrics and artifacts | Initialize W&B inside the step and call `wandb.finish()` at the end |
| Multiple steps contribute to the same run | Pass a W&B run ID between steps via `self` and re-init with `resume` |
| Flow-level param tracking | Log Metaflow `current.parameter` values as W&B config before training |
| Artifact lineage across the DAG | Each step logs its own artifact; W&B's UI shows the parent-child relationship by run |

## Prerequisites

- Metaflow installed (`pip install metaflow`)
- W&B account and `wandb` Python SDK installed (`pip install wandb`)
- `wandb login` completed on the machine or a `WANDB_API_KEY` environment variable set

## Steps

### 1. Log parameters and metrics from a single step

The simplest pattern: add `wandb.init()` and `wandb.log()` inside the step where training happens.

```python
import wandb
from metaflow import FlowSpec, step, Parameter

class MetaflowWandbFlow(FlowSpec):
    learning_rate = Parameter("lr", default=0.01)

    @step
    def start(self):
        self.next(self.train)

    @step
    def train(self):
        run = wandb.init(
            project="metaflow-wandb-demo",
            config={"learning_rate": self.learning_rate},
            name=f"run-lr-{self.learning_rate}"
        )
        for epoch in range(5):
            loss = 1.0 / (epoch + 1)
            wandb.log({"epoch": epoch, "loss": loss})
        run.finish()
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == "__main__":
    MetaflowWandbFlow()
```

Run it:

```bash
python metaflow_wandb_flow.py run --lr 0.01
```

The run appears in the W&B project with the learning rate recorded as a config field and the per-epoch loss as a metric.

### 2. Share a W&B run across steps

Metaflow retries or parallel steps can cause issues if each step calls `wandb.init()` independently. A more robust pattern is to create the run in the first step and re-use the run ID downstream. The `resume` argument lets subsequent steps attach to the same run.

```python
import wandb
from metaflow import FlowSpec, step, Parameter

class SharedWandbFlow(FlowSpec):
    @step
    def start(self):
        run = wandb.init(project="shared-wandb-flow", job_type="start")
        self.wandb_run_id = run.id
        run.log({"phase": "start"})
        run.finish()
        self.next(self.train)

    @step
    def train(self):
        run = wandb.init(
            project="shared-wandb-flow",
            id=self.wandb_run_id,
            resume="must"
        )
        run.log({"phase": "train", "epochs": 10})
        run.finish()
        self.next(self.end)

    @step
    def end(self):
        run = wandb.init(
            project="shared-wandb-flow",
            id=self.wandb_run_id,
            resume="must"
        )
        run.log({"phase": "end", "status": "ok"})
        run.finish()

if __name__ == "__main__":
    SharedWandbFlow()
```

The `resume="must"` argument tells W&B to append to the existing run rather than creating a new one. If the run ID does not exist on the server, `resume` raises a `UsageError` — so run the start step first.

### 3. Log artifacts from each step

Metaflow has its own artifact store, but W&B artifacts give you a central catalog indexed by run. To log a model artifact:

```python
import wandb
import json
from metaflow import FlowSpec, step

class ArtifactFlow(FlowSpec):
    @step
    def start(self):
        self.next(self.train)

    @step
    def train(self):
        model_data = {"coef": [0.3, -1.2], "intercept": 0.5}
        model_path = "/tmp/model.json"
        with open(model_path, "w") as f:
            json.dump(model_data, f)

        run = wandb.init(project="metaflow-artifacts")
        artifact = wandb.Artifact("trained-model", type="model")
        artifact.add_file(model_path)
        run.log_artifact(artifact)
        run.finish()
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == "__main__":
    ArtifactFlow()
```

After the run, the W&B Artifacts tab shows `trained-model:v0` linked to the run that produced it.

### 4. Track nested flows or branches

When a step fans out with `foreach`, each branch can initialize its own W&B run with a distinct name. The parent step can log an artifact listing all child run IDs for traceability.

```python
import wandb
from metaflow import FlowSpec, step

class ForeachWandbFlow(FlowSpec):
    @step
    def start(self):
        self.params = [0.01, 0.05, 0.1]
        self.next(self.train, foreach="params")

    @step
    def train(self):
        lr = self.input
        run = wandb.init(
            project="foreach-wandb",
            config={"lr": lr},
            name=f"train-lr-{lr}"
        )
        run.log({"final_loss": 1.0 - lr})
        run.finish()
        self.next(self.join)

    @step
    def join(self, inputs):
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == "__main__":
    ForeachWandbFlow()
```

## Verify

1. **Single-step tracking**: Run `MetaflowWandbFlow` and open the W&B project page. Confirm a run appears with the learning rate in Config and the per-epoch loss in the Charts tab.
2. **Shared run**: Run `SharedWandbFlow`. The W&B run should contain three phases in the log history. The run name is the same across steps.
3. **Artifact logging**: Run `ArtifactFlow`. Navigate to the Artifacts tab in W&B and confirm `trained-model` exists with version `v0`. The model.json file should be downloadable.
4. **Foreach**: Run `ForeachWandbFlow`. Three separate runs should appear in the project, each with a distinct `lr` config value and `final_loss` metric.

If a step initializes a W&B run but the run does not appear, check:
- `wandb.login()` has been called or `WANDB_API_KEY` is set
- The project name is consistent across steps (typos create separate projects)
- Firewall rules allow outbound HTTPS to `api.wandb.ai`

## Common errors

- **`wandb.errors.error.UsageError` with resume** — The run ID does not exist. Ensure the step that calls `wandb.init(id=..., resume="must")` runs after the step that creates the run.
- **W&B config empty** — Parameters set after `wandb.init()` are not recorded as config. Pass them via the `config` argument.
- **Duplicated runs** — Each `wandb.init()` without `resume` creates a new run. Use `resume` or design so each step initializes only once.
- **`wandb` not found at runtime** — When using `@conda`, add `wandb` to the libraries dict. It is not included by default.

## References

- [Metaflow docs: Step decorators](https://docs.metaflow.org/metaflow/basics#step)
- [W&B docs: Python SDK overview](https://docs.wandb.ai/ref/python)
- [W&B docs: Artifacts](https://docs.wandb.ai/guides/artifacts)
