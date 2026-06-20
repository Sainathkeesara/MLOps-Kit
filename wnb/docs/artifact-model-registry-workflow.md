# Integrating W&B Artifacts with the Model Registry

> End-to-end workflow for tracking data and model artifacts through W&B's Artifact system and promoting them through the Model Registry.

## Purpose

W&B Artifacts track the files produced by each run — datasets, model binaries, plots. The Model Registry adds a governance layer: versioned models can be moved through staging aliases (development → staging → production) with annotations. This doc shows how to wire them together so that an artifact logged in a training run becomes a registered model version that downstream pipelines can consume.

## Prerequisites

- A W&B account and project (free tier works).
- `wandb` Python SDK installed (`pip install wandb`).
- A training script that produces a model file (e.g., `.pkl`, `.pt`).
- `WANDB_API_KEY` set in the environment or `wandb login` completed.

## Steps

### 1. Log a model artifact during training

```python
import wandb

run = wandb.init(project="mlops-demo", job_type="train")

# training code that produces model.pkl

artifact = wandb.Artifact(
    name="trained_model",
    type="model",
    description="RandomForest classifier trained on the full feature set",
)
artifact.add_file("model.pkl")
run.log_artifact(artifact)

run.finish()
```

`log_artifact` uploads the file and records it as an Artifact version (`trained_model:v0`, then `:v1`, etc.) linked to this run.

### 2. Link the artifact to the Model Registry

```python
run.link_artifact(artifact, "mlops-demo-model-registry")
```

This creates or updates a registered model named `mlops-demo-model-registry` and associates the artifact version with it. The registry entry can then be moved through aliases.

One thing that tripped me up: `link_artifact` expects the registered model name as the second argument, not the artifact name. If the names differ, the artifact is still linked — the registry holds a reference, not a copy.

### 3. Promote a model version through aliases

Set an alias at link time:

```python
run.link_artifact(artifact, "mlops-demo-model-registry", aliases=["staging"])
```

Promote later in a separate evaluation pipeline:

```python
api = wandb.Api()
registered_model = api.artifact_version(
    "mlops-demo-model-registry",
    "v1"
)
registered_model.aliases.append("production")
registered_model.save()
```

### 4. Consume the promoted model

A deployment service fetches the artifact tagged `production`:

```python
api = wandb.Api()
artifact = api.artifact("mlops-demo-model-registry:production")
artifact.download(root="./prod-model")

# load model.pkl from ./prod-model
```

This decouples consumers from hardcoded version numbers — the alias becomes the contract.

## Verify

1. Open the W&B UI → Project → Artifacts tab. Confirm `trained_model` appears with at least one version.
2. Go to the Model Registry tab. Confirm `mlops-demo-model-registry` exists with the linked version and a `staging` alias.
3. Run the consumer script. Confirm the model downloads and loads successfully.
