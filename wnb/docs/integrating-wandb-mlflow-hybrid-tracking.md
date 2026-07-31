---
last_verified: 2026-07-31
tool_version: n/a
sources: []
---

# Integrating W&B with MLflow for Hybrid Experiment Tracking

## Purpose

Hybrid experiment tracking combines W&B's real-time dashboard, visualization, and collaboration features with MLflow's model registry and deployment tracking. This pattern is useful when a team wants W&B's visual experiment comparison during active development while maintaining MLflow's centralized model governance for downstream workflows.

## When to use

Use this approach when:
- Multiple team members need to compare hyperparameter runs in a shared dashboard during active development
- The organization already uses MLflow for model registry, staging, and deployment tracking
- You want experiment logging during training without migrating the entire model governance workflow to a single platform

## Prerequisites

- W&B account with API key configured
- MLflow tracking server accessible or local tracking directory
- Python packages installed: `wandb`, `mlflow`

## Steps

### 1. Initialize both tracking clients

Set up W&B and MLflow in the same training script. W&B initializes through `wandb.init()`, while MLflow requires `mlflow.set_tracking_uri()` and `mlflow.set_experiment()`.

```python
import wandb
import mlflow

wandb.init(project="hybrid-tracking-demo", name="run-001")
    mlflow.set_tracking_uri("local-mlflow-server:5000")
    mlflow.set_experiment("hybrid-tracking-demo")
```

### 2. Log parameters and metrics to both systems

Call `wandb.log()` alongside `mlflow.log_param()` and `mlflow.log_metric()` inside the training loop. Each backend stores its own copy of the data; no sync layer is required.

```python
for epoch in range(epochs):
    loss, accuracy = train_epoch(model, dataloader)
    wandb.log({"loss": loss, "accuracy": accuracy})
    mlflow.log_metric("loss", loss, step=epoch)
    mlflow.log_metric("accuracy", accuracy, step=epoch)
```

### 3. Register the model in MLflow after training

After training completes, log the model artifact to MLflow's model registry for version control and deployment tracking.

```python
mlflow.log_model(model, "model")
```

### 4. Create a traceable link between systems

Record the W&B run ID in the MLflow run as a tag, and vice versa. This lets you jump from the W&B dashboard to the MLflow experiment without a synchronization service.

```python
wandb.run.tags = [f"mlflow-run-{mlflow.active_run().info.run_id}"]
mlflow.set_tag("wandb_run_id", wandb.run.id)
```

## Verify

1. Open the W&B project dashboard. Confirm training metrics, parameters, and system stats appear for the run.
2. Open the MLflow UI. Confirm the experiment, run, and registered model artifact appear.
3. Verify the W&B run tags contain the MLflow run ID, and the MLflow run tags contain the W&B run ID.

## Common errors

- **Experiment name divergence**: Using different project names in `wandb.init(project=...)` and `mlflow.set_experiment()` makes it hard to correlate runs across systems. Align the names or use a shared naming convention.
- **Local-only MLflow tracking**: Forgetting `mlflow.set_tracking_uri()` causes runs to land in a local `./mlruns` directory, making them invisible to teammates. Always point MLflow at a shared tracking server in team environments.
- **Unset run on W&B side**: Calling `wandb.log()` before `wandb.init()` raises a runtime error. W&B requires an active run before logging.

## References

- MLflow tracking documentation
- W&B Python SDK reference
- MLflow model registry concepts
