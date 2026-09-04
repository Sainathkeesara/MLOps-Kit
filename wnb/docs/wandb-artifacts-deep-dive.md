---
last_verified: 2026-09-04
tool_version: n/a
sources: []
---

# W&B Artifacts deep-dive: versioning datasets, models, and pipeline outputs

## Purpose

W&B Artifacts turn experiment tracking from "metrics on a dashboard" into a
versioned data lineage graph. Every artifact is an immutable, content-addressed
version of a file or directory — a dataset, a model checkpoint, or any pipeline
output — that is linked to the run that produced or consumed it. This document
explains how to use artifacts to version each stage of an ML pipeline so that any
model can be traced back to the exact data and code that created it.

This is one way to structure artifact versioning with the Python SDK. It does not
replace a dedicated feature store or data lake, but it gives you automatic
lineage between data versions, model versions, and training runs.

## When to use

- You want to reproduce a model from three weeks ago and need the exact dataset
  version it trained on.
- Multiple pipeline stages (ingest → train → evaluate) should hand off data
  without copying files manually.
- You need an audit trail of which model binary shipped to a given experiment.

## Prerequisites

- A W&B account and `wandb login` completed locally.
- `pip install wandb` and a project to log into.
- Basic familiarity with `wandb.init()` / `run.finish()`.

## Core concepts

- **Artifact** — a versioned container of files. Created with
  `wandb.Artifact(name, type=...)`.
- **Type** — a free-form label (`"dataset"`, `"model"`, `"evaluation"`) used to
  group and filter artifacts.
- **Version** — artifacts of the same name get auto-incrementing versions
  (`dataset-customers:v0`, `:v1`, …).
- **Alias** — a mutable pointer (`latest`, `production`, `staging`) layered on
  top of an immutable version.
- **Lineage** — the graph of which run logged an artifact and which run used it.
- **`used`/`logged`** — `run.use_artifact()` records a consumer edge;
  `run.log_artifact()` records a producer edge.

## Steps

### 1. Log a dataset as a versioned artifact

Create the artifact, add files, then log it inside an active run.

```python
import wandb

run = wandb.init(project="mlops-kit-demo", name="ingest-v1")
artifact = wandb.Artifact("customers", type="dataset")
artifact.add_file("data/processed/customers.parquet")
run.log_artifact(artifact)
run.finish()
```

Each call to `log_artifact` with the same name bumps the version: the first run
produces `customers:v0`, the next `customers:v1`.

### 2. Consume a specific dataset version in training

Reference the artifact by name + version (or alias) and download it.

```python
run = wandb.init(project="mlops-kit-demo", name="train-v1")
data = run.use_artifact("customers:v1")
local_dir = data.download()
# train from files in local_dir
run.finish()
```

Using `use_artifact` records a consumer edge so the lineage graph shows that
`train-v1` depended on `customers:v1`.

### 3. Log a model and promote it with an alias

After training, log the model artifact and tag the good ones with `production`.

```python
run = wandb.init(project="mlops-kit-demo", name="train-v1")
model = wandb.Artifact("churn-model", type="model")
model.add_file("models/churn_model.joblib")
logged = run.log_artifact(model, aliases=["latest"])
run.finish()
```

Aliases are mutable, so you can re-point `production` without changing the
underlying immutable version.

### 4. Track a pipeline output (evaluation report)

Downstream stages log their own artifacts, building a chain: dataset → model →
evaluation.

```python
run = wandb.init(project="mlops-kit-demo", name="evaluate-v1")
model = run.use_artifact("churn-model:latest")
eval_report = wandb.Artifact("churn-eval", type="evaluation")
eval_report.add_file("evaluation_results.json")
run.log_artifact(eval_report)
run.finish()
```

### 5. Inspect lineage in the UI

Open the Artifacts tab of a run to see the `logged` and `used` artifacts, and
open an artifact's version page to see the full producer/consumer graph across
all runs.

## Verify

- The Artifacts tab of each run shows the correct `logged` and `used` entries.
- `customers` increments versions on each ingest run (`v0`, `v1`, …).
- `churn-model:production` points at the expected version after re-alias.
- The artifact version page shows `train-v1` consumed `customers:v1` and
  `evaluate-v1` consumed `churn-model:latest`.

## Common errors

- **Forgetting `use_artifact`** — logging a model trained on a dataset without
  calling `use_artifact` breaks the lineage; the run won't show the dependency.
- **Mutable `latest` in training** — pinning `:latest` instead of `:v1` makes
  runs non-reproducible; prefer explicit versions for training inputs.
- **Huge artifacts** — `add_file` uploads the whole file every version; for
  large datasets prefer `add_reference` to an external store over re-uploading.

## References

- W&B Artifacts guides and the `wandb.Artifact` Python API reference cover
  `log_artifact`, `use_artifact`, versioning, and aliasing in depth.
