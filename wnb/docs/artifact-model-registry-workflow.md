# W&B Model Registry — End-to-End Workflow

> Integrate W&B Artifacts with the Model Registry for versioned model governance and promotion through staging aliases.

## Purpose

W&B Artifacts track model files produced in training runs. The Model Registry adds a governance layer: registered models can be promoted through aliases (staging → production) with lineage tracking. This workflow shows how to log artifacts, link them to registry collections, and consume registered models in deployment pipelines.

## When to use

Use this pattern when you need model version control with promotion workflows. The registry provides a central catalog for models that downstream services can consume via stable aliases rather than hardcoded versions.

## Prerequisites

- W&B account with registry access (organization plan required for Model Registry)
- `wandb` Python SDK installed
- Training script producing a model artifact (`.pkl`, `.pt`, `.onnx`)

## Steps

### 1. Log a model artifact during training

```python
import wandb

run = wandb.init(project="mlops-demo", job_type="train")

# training code producing model.pkl

artifact = wandb.Artifact(
    name="trained-model",
    type="model",
    description="RandomForest classifier on the full feature set"
)
artifact.add_file("model.pkl")
run.log_artifact(artifact)

run.finish()
```

`log_artifact()` creates the artifact version (`trained-model:v0`, then `:v1`, etc.) linked to the run.

### 2. Link artifact to Model Registry collection

Use `target_path` with the registry prefix and collection name:

```python
import wandb

run = wandb.init(project="mlops-demo", job_type="register")

# Re-create artifact for linking
artifact = wandb.Artifact(name="trained-model", type="model")
artifact.add_file("model.pkl")

# Link to registry: wandb-registry-{REGISTRY}/{COLLECTION}
run.link_artifact(
    artifact=artifact,
    target_path="wandb-registry-models/model-registry",
    aliases=["staging"]
)

run.finish()
```

The `target_path` format is `wandb-registry-{registry_name}/{collection_name}`. W&B auto-creates the collection if it does not exist.

### 3. Promote a model version to production

Update aliases using the API to promote from staging to production:

```python
import wandb

api = wandb.Api()

# Fetch the staging version and add production alias
artifact = api.artifact("wandb-registry-models/model-registry:staging")
# Or use version index: api.artifact("wandb-registry-models/model-registry:v0")
artifact.aliases.append("production")
artifact.save()
```

### 4. Consume the registered model

Deployment services fetch the model by alias:

```python
import wandb

api = wandb.Api()
artifact = api.artifact("wandb-registry-models/model-registry:production")
download_path = artifact.download()

# Load model from download_path
```

Or use `use_artifact` to declare the model as input to a downstream run:

```python
import wandb

run = wandb.init(project="deployment-service")

artifact = run.use_artifact("wandb-registry-models/model-registry:production")
model_dir = artifact.download()
```

## Verify

1. Open W&B UI → Artifacts tab. Confirm the logged artifact appears with a version.
2. Navigate to Registry → Collections. Confirm the linked collection exists with the version and `staging` alias.
3. After promotion, verify the `production` alias is present.
4. Run the consumer script. Confirm the model downloads and loads successfully.

## Common errors

- **Registry not found**: Organization plan required. Upgrade from personal plan or use artifacts without registry linkage.
- **Collection type mismatch**: The `type` in `Artifact()` must match the collection's accepted artifact types.
- **Alias not applied**: `artifact.save()` required after modifying aliases. Without it, changes are not persisted.