---
last_verified: 2026-09-08
tool_version: n/a
sources:
  - https://xoomar.com/blog/tutorial/mlops-tools-integration-guide-2026
  - https://infrasketch.net/blog/mlops-system-design
  - https://precisionaiacademy.com/blog/mlops-guide-2026
---

# Model Serving — Patterns in production MLOps projects

> How model serving connects to experiment tracking, feature stores, containerization, and monitoring in real deployments.

## Purpose

I kept running into model serving tutorials that stopped at "start the server and send a request." That's fine for a first contact, but production MLOps projects have to connect the endpoint to the rest of the stack: experiment tracking for model lineage, feature stores for consistent lookups, container registries for reproducible deployments, and monitoring for drift detection. This document describes the patterns that connect model serving to those systems, using the integration script `scripts/combining-model-serving-with-containerization.py` as a concrete reference.

## Pattern 1: Model Serving + Experiment Tracking (MLflow Model Registry)

The production path usually ends at the model registry. A trained model is logged to MLflow, evaluated, and promoted through staging to production. The serving endpoint loads the model by registry URI rather than by filesystem path, so the same artifact can be deployed to staging and production without copying weights.

**When to use:** Any team that needs an audit trail linking a serving version to the exact training run, data snapshot, and configuration.

**Steps:**
1. Log the trained model to MLflow with `mlflow.<framework>.log_model()`.
2. Transition the version through staging to production using `MlflowClient().transition_model_version_stage()`.
3. In the serving container, resolve the model URI via `models:/<name>/Production` so the endpoint always loads the promoted version.
4. Add a performance regression test before promotion: compare the candidate's validation metric against the current production baseline.

**Verify:** Deploy the endpoint with a model URI pointing to a staged version. Confirm the model loads, predict returns a result, and transitioning the version to production changes the loaded artifact without rebuilding the image.

## Pattern 2: Model Serving + Feature Store (Feast online serving)

Training-serving skew is a common failure mode. Features computed in pandas during training may differ from the values served at inference time if the serving code re-implements the logic in a different runtime. A feature store serves the same feature definitions to both paths.

**When to use:** Real-time inference workloads where feature freshness matters and the same entity keys are queried in training and serving.

**Steps:**
1. Define Feature Views in a shared feature repo and materialize them to an Online Store (Redis, DynamoDB, or SQLite for development).
2. In the training pipeline, retrieve historical features with `store.get_historical_features()`.
3. In the serving endpoint, retrieve online features with `store.get_online_features()` using the same feature references.
4. Bundle the feature repo path inside the serving container so the store client can resolve definitions at startup.

**Verify:** Query the endpoint with an entity key that has known feature values. Confirm the prediction uses those values and that the feature latency for a single-entity lookup stays under the SLO (typically under 10 ms for Redis-backed online stores).

## Pattern 3: Model Serving + Containerization (Docker / OCI image)

Containerization freezes the serving runtime: Python version, dependency wheels, model weights, and configuration. The pattern in `scripts/combining-model-serving-with-containerization.py` stages the model artifact, generates a FastAPI entrypoint, and produces a Dockerfile that bundles everything into a single image.

**When to use:** Any deployment where reproducibility across staging, production, and DR environments matters, or where the serving binary must travel across teams that do not share a runtime.

**Steps:**
1. Stage the model artifact and serving code into a versioned bundle directory.
2. Generate the serving application (FastAPI, TorchServe, or Triton ensemble) inside the bundle.
3. Produce a container configuration that copies the bundle into a minimal base image and exposes the serving port.
4. Build the image and run a smoke test before pushing to the registry.

**Verify:** Build the image, start the container, and confirm `/health` returns 200 and `/predict` accepts a sample request. The integration script's `validate` mode checks the bundle structure before build.

## Pattern 4: Model Serving + Monitoring & Drift (Evidently / Whylabs)

Deployment is not the finish line. Production models drift as data distributions shift, and the serving endpoint should emit the signals that monitoring systems need to detect that drift.

**When to use:** Models that serve live traffic for more than a few days, especially in domains with seasonal or adversarial data.

**Steps:**
1. Add a `/metrics` or `/monitor` endpoint to the serving application that exposes recent prediction distributions.
2. Run drift detection on a scheduled basis (hourly or daily) against a reference dataset captured during training.
3. If drift exceeds a threshold, alert the retraining pipeline and optionally trigger a rollback to the previous production version.

**Verify:** Ingest a synthetic drifted dataset into the monitoring job and confirm it produces a drift report above the alert threshold. Confirm the serving endpoint continues to respond during the monitoring run.

## Pattern 5: Model Serving + Pipeline Orchestration (CI/CD promotion)

Serving endpoints are most reliable when promotion is automated. A pipeline orchestrator (Airflow, Kubeflow Pipelines, or GitHub Actions) runs the validation suite against a staged version and promotes it to production if the gates pass.

**When to use:** Teams with frequent retraining where manual review cannot keep pace, or where promotion consistency across environments is required.

**Steps:**
1. Build the serving image from the staged bundle and push it to a registry.
2. Deploy the image to a staging environment and run the validation suite.
3. If the suite passes, update the production deployment manifest to point to the new image tag.
4. Keep a rollback manifest that references the previous tag so the orchestrator can revert within seconds.

**Verify:** Run the pipeline with a validation metric below the promotion threshold. Confirm the production manifest is not updated. Then run with a metric above the threshold and confirm the new image tag appears in production.

## Common pitfalls

**Default bind host.** `127.0.0.1` is the default listen address in many local tutorials. Inside a container or CI runner, external clients cannot reach `127.0.0.1`. Bind to `0.0.0.0` for any workload that is not purely local.

**Model version drift.** Loading the model by filesystem path rather than registry URI means the serving container can silently pick up a different artifact after a redeploy. Resolve by registry URI or by pinning the exact model version in the bundle manifest.

**Missing health checks.** A serving container that returns 200 on `/health` without actually verifying the model is loaded will pass liveness probes while failing silently on traffic. The health endpoint should check that the model weights and feature store connection are available.

**Unbounded concurrency.** The default concurrency limit for many serving frameworks is unbounded, which can exhaust memory or GPU memory under load. Set `max_concurrency` to a value derived from load testing rather than leaving it at the default.

## Verify

1. Run the integration script in `bundle` mode against a sample model directory and confirm it produces a bundle with `manifest.json`, `app.py`, and `model/`.
2. Run the script in `validate` mode and confirm it reports success for a complete bundle and failure when the model directory is empty.
3. Run the script in `containerize` mode and confirm it writes a `Dockerfile` and `requirements.txt` inside the bundle.
4. Build the generated Dockerfile and confirm the container starts, `/health` returns 200, and `/predict` accepts a JSON payload.
5. Modify the `app.py` to load a real model artifact and confirm the serving endpoint returns predictions instead of the stub response.

## Related material

- `scripts/combining-model-serving-with-containerization.py` implements the bundle, validate, and containerize steps end-to-end.
- `0000-primer-model-serving.md` in this directory covers the first-contact concepts of model serving, feature lookup, and container packaging.
- Containerization patterns for multi-stage Docker builds are covered in `docs/concepts/containerization/`.
