# Model Registry — quick primer

> First-day notes on Model Registry. What it is, why it matters, and the key ideas to know.

## What is it?

A model registry is a central place to store, version, and manage trained ML models — think of it like a GitHub for models rather than code. You push a model artifact in, tag it with a version number or an alias (like "staging" or "production"), and the registry keeps track of which experiment run produced it and what metadata goes with it.

Before registries, teams passed around `.pkl` files on Slack or S3 buckets with filenames like `model_final_v3_actual_final.pkl`. Nobody knew which version was in production or what hyperparameters it used. The model registry solves that by being the single source of truth for "what model is currently live and how do I trace it back to its training run."

## Why does it matter for MLOps?

Model registry is the bridge between experimentation and production. Experiment tracking tells you what you tried; the model registry tells you what's actually deployed. Without it:

- You can't roll back to a previous version quickly.
- You don't know if the model in production came from the current dataset or last month's.
- Auditors and compliance folks have no way to verify which model was serving on a given date.
- Deploying a new model becomes a manual copy-paste operation that breaks.

An MLOps pipeline needs the registry to automate promotions. For example: a CI pipeline trains a model, pushes it to the registry with alias "staging", runs validation tests, and only promotes to "production" if the tests pass. That's impossible without a registry.

## Key terminology

- **Registered model** — A named entry in the registry that holds all versions of a given model. Example: `fraud-detection-v2` is a registered model.
- **Model version** — A specific iteration of a registered model, usually auto-incremented. Example: version `3` of `fraud-detection-v2`.
- **Alias (or stage)** — A human-readable label pointing to a specific version. Example: `production` → v3, `staging` → v4.
- **Artifact URI** — The storage location of the actual model file (e.g. an S3 path or local file path).
- **Run ID** — Links back to the experiment tracking run that produced this model. Example: looking up the run ID shows the params, metrics, and dataset used.
- **Model lineage** — The chain from raw data → training run → registered model → deployment. Traceable for audits.
- **Promotion** — Moving a model version from one stage to the next. Example: promote v4 from `staging` to `production` after validation.

## A concrete example

```python
# Pseudo-code for registering a model
import mlflow  # or wandb, or any registry

with mlflow.start_run() as run:
    mlflow.sklearn.log_model(model, "model")
    run_id = run.info.run_id

# Register the model from the run
mlflow.register_model(
    model_uri=f"runs:/{run_id}/model",
    name="fraud-detection-v2"
)

# Version 1 is auto-created. Now set an alias.
client = mlflow.tracking.MlflowClient()
client.set_registered_model_alias("fraud-detection-v2", "staging", version=1)
```

This takes a model from a completed run, registers it as version 1, and tags it "staging" — ready for validation before going to production.

## How this connects to what's next

A model registry doesn't exist in isolation — it depends on experiment tracking (the run ID that links back to training details) and feeds into deployment tools like KServe or Seldon Core (which pull models from the registry by alias). Together they form the deploy pipeline: track → register → validate → promote → serve.
