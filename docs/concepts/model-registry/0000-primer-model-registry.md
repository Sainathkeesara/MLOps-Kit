---
last_verified: 2026-07-25
tool_version: n/a
sources: []
---

# Model Registry — quick primer

> First-day notes on Model Registry. What it is, why it matters, and the key ideas to know.

## What is it?

I just learned that a model registry is a central place to store and version trained ML models — think of it like GitHub, but for models instead of code. Before registries existed, people passed around `.pkl` files on Slack or named files `model_final_v3_actual_final.pkl` on shared drives. A model registry gives every model a home: you push a trained model in, tag it with a name and version, and the registry remembers who made it, which training run produced it, and what metrics it scored.

## Why does it matter for MLOps?

Experiment tracking tells me what I tried; the model registry tells me what's actually deployed. Here's why it matters for MLOps work:

- When I'm ready to deploy a model, I need to know which specific version is the best one. The registry is the single source of truth for that.
- I can promote a model through stages (staging → serving) and roll back to a previous version if something goes wrong in serving.
- Compliance and audit work becomes possible — an auditor can ask "which model is serving right now and how was it validated?" and I can point to a registry entry instead of a folder on someone's laptop.
- Automated CI pipelines need the registry to work: train a model, push it, run validation tests, and only promote it if the tests pass.

## Key terminology

- **Registered model** — A named entry in the registry that holds all versions of a given model. Example: `fraud-detection-v2` is a registered model containing versions 1, 2, 3, and so on.
- **Model version** — A specific iteration of a registered model, usually auto-numbered. Example: version `3` of `fraud-detection-v2`.
- **Alias / stage** — A human-readable label that points to a specific version. Example: the alias `serving` points to version `3`, and `staging` points to version `4`.
- **Model lineage** — The chain that connects a model back to its training data, code, and experiment run. Example: I can trace from a deployed model all the way back to the data version and hyperparameters used to train it.
- **Promotion** — Moving a model version from one stage to the next. Example: promoting version `4` from `staging` to `serving` after it passes validation tests.
- **Artifact URI** — The storage location where the actual model files live. Example: `s3://my-bucket/models/fraud-v3/` or a local path like `./mlartifacts/`.

## A concrete example

Here's what registering a model looks like in Python:

```python
import mlflow

with mlflow.start_run() as run:
    mlflow.sklearn.log_model(model, "model")
    run_id = run.info.run_id

mlflow.register_model(
    model_uri=f"runs:/{run_id}/model",
    name="fraud-detection-v2"
)

# Version 1 is created automatically. Tag it for staging.
client = mlflow.tracking.MlflowClient()
client.set_registered_model_alias("fraud-detection-v2", "staging", version=1)
```

This takes a model from a completed training run, registers it as version 1, and tags it "staging" — ready for validation before going to serving.

## How this connects to what's next

The model registry doesn't work in isolation — it depends on experiment tracking (the run ID links a model back to its training details) and feeds into deployment tools like KServe or Seldon Core (which pull models from the registry by alias). Together, tracking → registering → validating → deploying forms the model lifecycle that MLOps is built around.