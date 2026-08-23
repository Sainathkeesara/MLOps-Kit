---
last_verified: 2026-08-23
tool_version: n/a
sources:
  - https://docs.nvidia.com/datascience/deployment/stable/examples/fraud-detection-mlops-pipeline/notebook/index.html
  - https://www.youngju.dev/blog/ai-platform/2026-03-07-ai-platform-mlflow-experiment-tracking-model-registry.en
  - https://loftllc.dev/en/docs/tech/infrastructure/devstack-mlflow-integration/
  - https://mlflow.org/articles/mlops-pipeline-automation-best-practices-in-2026/
---

# Experiment Tracking in Real MLOps Projects: Patterns and Pitfalls

## Purpose

Experiment tracking starts out feeling trivial — log a param, log a metric, done. The hard part is keeping it consistent once a project grows past a single script: multiple pipelines, shared model registries, CI/CD triggers, and teams that need to compare each other's runs weeks later. This doc covers the patterns that hold up in production MLOps projects and the pitfalls that tend to bite after the first few weeks.

## Combining tracking with pipeline orchestration

A production pipeline chains stages — preprocessing, training, evaluation, deployment — and each stage wants to log its own metrics. The cleanest pattern is to pass a single run identifier between stages so that every stage logs to the same experiment rather than spawning disconnected runs. Prefect and Airflow can forward the MLflow run ID between tasks, preserving lineage across the full pipeline from raw data to deployed model [source: https://docs.nvidia.com/datascience/deployment/stable/examples/fraud-detection-mlops-pipeline/notebook/index.html].

At production scale, teams tend to separate the orchestrator (which owns the bird's-eye view of the pipeline) from the tracker (which owns the detailed view of each experiment). Dagster provides the pipeline-level view while MLflow provides the run-level view, linked by a correlation ID that ties a specific pipeline execution to the experiments it produced [source: https://loftllc.dev/en/docs/tech/infrastructure/devstack-mlflow-integration/].

### Pitfall: fragmented lineage

When every pipeline stage opens its own run without passing a shared ID, the project ends up with dozens of orphan runs that cannot be stitched back together. Debugging "why did accuracy drop?" then requires manual detective work across unrelated runs. Passing a correlation ID or run ID between stages avoids this.

## Connecting runs to the model registry

Experiment tracking and the model registry solve different problems — tracking records what was tried, the registry records what is live — but they need to be linked. Each registered model version should point back to the run that produced it, so that promoting a model to production carries its full training lineage with it.

MLflow deprecated the old Stages API in favor of aliases like `candidate`, `challenger`, and `champion` [source: https://www.youngju.dev/blog/ai-platform/2026-03-07-ai-platform-mlflow-experiment-tracking-model-registry.en]. This enables a champion/challenger pattern: a new model is evaluated against the current production model before promotion, and aliases make it clear which version is serving traffic without hard-wiring stage transitions into the registry.

### Pitfall: registering without linking the run

It is possible to register a model without attaching the source run ID. The result is a registry entry that cannot be traced back to the hyperparameters, data version, or code commit that produced it. Always log the run ID at registration time — if the registry does not capture it natively, store it as a tag.

## Using tracked metrics as drift-detection baselines

The metrics logged during training become the baselines against which production drift is measured. When a model is promoted, its training-time accuracy and loss distributions define the thresholds that trigger retraining alerts later. Experiment tracking captures these baselines; monitoring tools consume them. The handoff between the two is a common source of silent failures — if the metric name or shape changes between training and serving, drift detection compares against the wrong baseline [source: https://docs.nvidia.com/datascience/deployment/stable/examples/fraud-detection-mlops-pipeline/notebook/index.html].

### Pitfall: baseline/target drift without versioning

A baseline metric is only meaningful alongside the data and code that produced it. When the training pipeline changes (new preprocessing, new features), the old baseline no longer applies, but monitoring keeps alerting against it. Versioning baselines alongside model versions keeps the comparison honest.

## CI/CD integration and performance gates

Production MLOps projects trigger training runs on code or data changes, enforce performance gates inside the pipeline, and use canary-release logic to shadow-test a new model before promotion. GitHub Actions can automate champion promotion with environment-based approval flows, so that a new model only replaces the current champion after it clears both automated gates and a human approval step [source: https://www.youngju.dev/blog/ai-platform/2026-03-07-ai-platform-mlflow-experiment-tracking-model-registry.en].

A multi-level testing pyramid helps catch problems before they reach the tracker: data validation at the base, unit and integration tests in the middle, end-to-end pipeline runs at the top. Storing artifacts in a central model registry makes every version traceable from training run through to deployment [source: https://mlflow.org/articles/mlops-pipeline-automation-best-practices-in-2026/].

### Pitfall: gating on a single metric

Performance gates that check only accuracy (or only loss) miss regressions in latency, calibration, or fairness. Define a small set of gate metrics up front and require all of them to clear before promotion.

## How this connects forward

These patterns assume a single team and a single pipeline. The next step is applying them across multiple teams sharing a model registry, or wiring experiment tracking into automated retraining loops that react to drift signals without human intervention.
