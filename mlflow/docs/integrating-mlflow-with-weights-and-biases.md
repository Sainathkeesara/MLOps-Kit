---
last_verified: 2026-07-25
tool_version: n/a
---

# Integrating MLflow with Weights & Biases: hybrid experiment tracking patterns

## Purpose

Using MLflow and Weights & Biases together in the same experiment workflow gives practitioners a way to combine MLflow's model registry and artifact lineage with W&B's real-time dashboard and team collaboration. This doc covers patterns for running both systems in parallel, synchronizing metadata, and deciding which tool owns which piece of the tracking pipeline.

## When to use this pattern

This pattern is useful when a team already uses one system and is adding the other, or when different stages of a lifecycle benefit from different tools: W&B for rapid iteration and team sharing during development, MLflow for model registration and deployment governance in downstream pipelines.

## Hybrid experiment tracking workflow

1. **Instrument MLflow autologging for framework-level capture.** Enable autologging at the start of the training script so MLflow records parameters, metrics, and the trained model artifact automatically.

2. **Initialize a W&B run alongside the MLflow run.** Create a W&B run with a matching `run_name` so the two systems can be correlated in dashboards.

3. **Log shared metrics to both systems.** Inside the training loop, emit metrics to MLflow via `mlflow.log_metric` and to W&B via `wandb.log`. The dual-write pattern ensures both dashboards receive the same signal.

4. **Log artifacts to MLflow for persistence.** After training, use `mlflow.log_artifact` to store the model, config, and any evaluation artifacts in the MLflow artifact store. W&B artifacts can mirror the same files for team access.

5. **Register the model in MLflow after evaluation.** Once the model passes validation thresholds, call `mlflow.register_model` to promote it into the MLflow Model Registry for serving and deployment pipelines.

## Example

```python
import mlflow
import wandb
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

mlflow.sklearn.autolog(log_models=True, silent=True)

wandb.init(project="hybrid-tracking", name="rf-baseline")

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with mlflow.start_run(run_name="rf-baseline"):
    model = RandomForestClassifier(n_estimators=100, max_depth=5)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    mlflow.log_metric("accuracy", acc)
    wandb.log({"accuracy": acc})

    mlflow.sklearn.log_model(model, "model")
    wandb.log_artifact("mlflow-artifacts:/0/model/model.pkl", type="model")

mlflow.register_model("runs:/<run_id>/model", "iris-rf")
wandb.finish()
```

## Verify

Confirm both systems received the run data:

- In the MLflow UI, check that the run appears under the correct experiment with `accuracy` in the metrics tab and the model artifact in the artifacts tab.
- In the W&B dashboard, verify the run is listed under the `hybrid-tracking` project with the `accuracy` metric plotted and the artifact attached.
- Cross-reference the `run_name` in both systems to ensure the correlation is correct. If names diverge, the linking breaks and manual reconciliation is required.