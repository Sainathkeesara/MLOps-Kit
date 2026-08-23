---
last_verified: 2026-08-23
tool_version: n/a
sources:
  - https://docs.nvidia.com/datascience/deployment/stable/examples/fraud-detection-mlops-pipeline/notebook/index.html
  - https://www.youngju.dev/blog/ai-platform/2026-03-07-ai-platform-mlflow-experiment-tracking-model-registry.en
  - https://loftllc.dev/en/docs/tech/infrastructure/devstack-mlflow-integration/
  - https://mlflow.org/articles/mlops-pipeline-automation-best-practices-in-2026/
---

# Pipeline orchestration patterns for production MLOps

## Purpose

This doc covers the recurring patterns that show up when wiring ML pipelines into production systems. It is not a tutorial for a specific orchestrator — it is a map of the design decisions you will face regardless of whether you pick Airflow, Prefect, Kubeflow, or Dagster. The patterns are drawn from real MLOps deployments where experiment tracking, model registry, and serving are connected through an orchestration layer.

## When to use these patterns

These patterns apply when:

- You have more than one stage in your ML pipeline (preprocessing → training → evaluation → deployment).
- You need end-to-end lineage — the ability to trace a deployed model back to the exact data, code, and hyperparameters that produced it.
- You want automated promotion (champion/challenger) driven by experiment-tracked metrics rather than manual approval.
- Multiple team members need to see what was tried, what worked, and what was deployed.

## Pattern 1 — Orchestrator-driven stage chaining with run ID propagation

The most common pattern is to have the orchestrator pass an experiment run ID between stages. Each stage logs to the same run, preserving end-to-end lineage.

```python
# In a Kubeflow pipeline component
from kfp import dsl
import mlflow

@dsl.component
def preprocess(data_path: str, output_path: str):
    mlflow.set_experiment("fraud-detection")
    with mlflow.start_run() as run:
        # ... preprocessing logic ...
        mlflow.log_param("input_rows", len(df))
        mlflow.log_artifact(output_path)
        # Return run_id so downstream stages can attach to it
        return run.info.run_id
```

The run ID becomes the shared correlation token. The orchestrator stores it as pipeline output and injects it into subsequent stages. This avoids coupling scheduling state to tracking state — the orchestrator handles "when" while the tracker handles "what happened" [source: https://loftllc.dev/en/docs/tech/infrastructure/devstack-mlflow-integration/].

## Pattern 2 — Typed-artifact passing between stages

Modern pipeline frameworks support typed artifacts. MLflow 2.9+ introduced model artifacts with typed schemas, and W&B Artifacts attach lineage metadata automatically. The key insight is that artifacts should carry their provenance — not just the file, but the run, data version, and code commit that produced them.

```python
# MLflow typed artifact passing
with mlflow.start_run():
    model = train_model(X_train, y_train)
    mlflow.sklearn.log_model(model, "model")
    # The artifact now carries: run_id, experiment_id, UTC timestamp,
    # and the git commit hash if git integration is enabled
```

Typed artifacts make it possible to build deployment gates that check artifact properties (model format, training data hash, metric thresholds) before promoting to production [source: https://www.youngju.dev/blog/ai-platform/2026-03-07-ai-platform-mlflow-experiment-tracking-model-registry.en].

## Pattern 3 — Champion/challenger with automated promotion

The champion/challenger pattern uses experiment-tracked metrics to drive deployment decisions. A new model (challenger) is trained and evaluated, then compared against the currently deployed model (champion). If the challenger meets the promotion criteria, it replaces the champion.

```python
# Simplified champion/challenger logic
champion_metrics = get_champion_metrics()  # from model registry
challenger_metrics = get_challenger_metrics()  # from latest run

if challenger_metrics["auc"] > champion_metrics["auc"] * 1.01:
    promote_to_champion(challenger_model)
else:
    log_decision("challenger did not meet threshold")
```

This pattern works best when the orchestrator enforces a performance gate inside the pipeline — the model is not promoted unless the metric comparison passes. GitHub Actions or similar CI/CD systems can automate the approval flow with environment-based gates [source: https://www.youngju.dev/blog/ai-platform/2026-03-07-ai-platform-mlflow-experiment-tracking-model-registry.en].

## Pattern 4 — Centralized tracking as single source of truth

In production, multiple pipeline versions may run concurrently (A/B tests, shadow deployments, feature branches). Centralized tracking ensures every pipeline version logs to the same experiment store, making cross-version comparison possible.

The NVIDIA fraud-detection pipeline demonstrates this: preprocessing, training, evaluation, and deployment stages all log to a single MLflow experiment, with the run ID propagated through the orchestration chain. Triton model-repository directories (`1/`, `2/`, `3/`) map to experiment runs, enabling champion vs. challenger comparison via versioned serving [source: https://docs.nvidia.com/datascience/deployment/stable/examples/fraud-detection-mlops-pipeline/notebook/index.html].

## Pattern 5 — Separation of concerns between orchestrator and tracker

A common mistake is coupling the orchestrator's scheduling state to the tracker's run state. The orchestrator (Airflow/Prefect/Dagster) should manage "when" things run — scheduling, retries, resource allocation. The tracker (MLflow/W&B/ClearML) should manage "what happened" — parameters, metrics, artifacts.

The two systems link via a shared `correlation_id` or run tag. This means you can swap out the orchestrator without losing tracking history, and vice versa. Pipeline automation best practices recommend centralized tracking as the single source of truth, with typed-artifact passing between stages to maintain lineage [source: https://mlflow.org/articles/mlops-pipeline-automation-best-practices-in-2026/].

## Verify

To verify these patterns are working:

1. **Lineage check**: Trace a deployed model back through the registry, to the experiment run, to the training data version. Every link should resolve.
2. **Reproducibility check**: Re-run a pipeline stage with the same run ID and confirm it produces the same metrics.
3. **Promotion check**: Train a challenger that beats the champion's metric threshold and confirm it is automatically promoted.

## Common errors

- **Run ID not propagated**: If downstream stages create new runs instead of attaching to the existing one, lineage breaks. Ensure the orchestrator passes the run ID as a pipeline parameter.
- **Artifact drift**: Logging artifacts to different tracking URIs across stages fragments the lineage. Use a centralized tracking server for all stages.
- **Metric threshold mismatch**: Champion/challenger comparison fails if the two models are evaluated on different data splits or with different metrics. Always compare on the same evaluation set.

## References

- NVIDIA fraud-detection MLOps pipeline: https://docs.nvidia.com/datascience/deployment/stable/examples/fraud-detection-mlops-pipeline/notebook/index.html
- MLflow experiment tracking + model registry integration: https://www.youngju.dev/blog/ai-platform/2026-03-07-ai-platform-mlflow-experiment-tracking-model-registry.en
- MLflow integration architecture: https://loftllc.dev/en/docs/tech/infrastructure/devstack-mlflow-integration/
- MLflow pipeline automation best practices: https://mlflow.org/articles/mlops-pipeline-automation-best-practices-in-2026/
