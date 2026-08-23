---
last_verified: 2026-08-23
tool_version: n/a
sources:
  - https://mlflow.org/articles/mlops-pipeline-automation-best-practices-in-2026/
  - https://docs.nvidia.com/datascience/deployment/stable/examples/fraud-detection-mlops-pipeline/notebook/index.html
  - https://www.youngju.dev/blog/ai-platform/2026-03-07-ai-platform-mlflow-experiment-tracking-model-registry.en
  - https://loftllc.dev/en/docs/tech/infrastructure/devstack-mlflow-integration/
---

# Experiment Tracking in real MLOps projects — patterns and pitfalls

> Patterns that keep experiment tracking useful across a team, and the
> pitfalls that turn it into a noisy database no one trusts.

## Purpose

Experiment tracking is most valuable when every stage of a pipeline — data
validation, training, evaluation, and deployment — logs to the same run
record. In practice, teams fragment those logs across spreadsheets, ad-hoc
scripts, and disconnected tools, which defeats the purpose. This document
describes the patterns that hold the system together and the pitfalls that
tend to appear once the pipeline grows beyond a single notebook.

## Key patterns

### Centralize the tracking server

A single tracking backend (for example, an MLflow Tracking Server or a W&B
team account) gives every engineer and pipeline stage one place to log and
query. The NVIDIA fraud-detection example chains orchestrator stages and
passes the MLflow `run_id` between them so preprocessing, training,
evaluation, and deployment all attach to the same experiment trace
[source: https://docs.nvidia.com/datascience/deployment/stable/examples/fraud-detection-mlops-pipeline/notebook/index.html].

### Link runs to model versions

MLflow 2.9+ deprecated stage labels in favor of aliases such as
`candidate`, `challenger`, and `champion`. Each experiment run should link
to a registered model version so the lineage from "this training run" to
"this deployed model" is unambiguous [source: https://www.youngju.dev/blog/ai-platform/2026-03-07-ai-platform-mlflow-experiment-tracking-model-registry.en].

### Enforce performance gates in CI/CD

Trigger training on code or data changes, then enforce metric thresholds
inside the pipeline before a model is promoted. GitHub Actions can automate
champion promotion with environment-based approval flows
[source: https://mlflow.org/articles/mlops-pipeline-automation-best-practices-in-2026/].

### Separate scheduling from tracking state

The orchestrator (Airflow, Prefect, Dagster) manages the pipeline's
bird's-eye view, while the experiment tracker provides per-run detail. A
shared `correlation_id` or run tag links the two without coupling scheduling
state to tracking state [source: https://loftllc.dev/en/docs/tech/infrastructure/devstack-mlflow-integration/].

## Common pitfalls

### Unlogged experiments

Skipping `log_param` or `log_metric` because the hyperparameters "feel
obvious" is the most common mistake. A month later, no one can reproduce the
run or explain why the accuracy jumped.

### Missing artifacts

Logging only metrics and forgetting the model file means the best run cannot
be promoted to a registry. Always log the serialized model as an artifact.

### Run fragmentation

Starting a new experiment ID for every tweak makes comparison impossible.
Use one experiment per problem and rely on runs within that experiment to
capture variations.

### No baseline for drift detection

Experiment-tracked baseline metrics become drift-detection thresholds once
the model is in production. Without a recorded baseline, there is nothing to
compare the production metrics against
[source: https://docs.nvidia.com/datascience/deployment/stable/examples/fraud-detection-mlops-pipeline/notebook/index.html].

## Steps to implement

1. Stand up a single tracking server and point every pipeline stage at it.
2. Wrap training and evaluation scripts so they log parameters, metrics, and
   artifacts to the active run.
3. Tag each run with the pipeline `correlation_id` so the orchestrator and
   tracker can be queried jointly.
4. Register the model version at the end of training and attach the run ID
   to the registry entry.
5. Add CI/CD gates that fail the pipeline when metrics fall below the
   baseline recorded in the champion version.

## Verify

- **Single source of truth**: every engineer can query the same experiment
  and see the full run history.
- **Reproducible runs**: rerunning a pipeline with the same parameters
  produces metrics within tolerance of the logged run.
- **Traceable promotions**: every model version in the registry links back to
  an experiment run, and every run links to the pipeline execution that
  produced it.
