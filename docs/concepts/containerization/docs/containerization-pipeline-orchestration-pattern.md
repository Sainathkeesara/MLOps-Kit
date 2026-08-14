---
last_verified: 2026-08-14
tool_version: n/a
sources:
  - https://mlflow.org/docs/latest/ml/deployment/
  - https://kodekloud.com/blog/using-kubernetes-for-mlops
  - https://multiwaresolutions.com/blog/mlops-2026-kubeflow-pipelines-and-model-registry-afa0-2026-06-09
  - https://www.zenml.io/mlops-tags/model-registry
  - https://www.freecodecamp.org/news/containerize-mlops-pipeline-from-training-to-serving/
---

# Containerization + Pipeline Orchestration pattern

> Combining containerized steps with a pipeline orchestrator to make ML workflows reproducible and portable.

## Purpose

Containerization and pipeline orchestration solve different but complementary problems. Containerization guarantees that each step runs with the same runtime every time. Pipeline orchestration guarantees that steps run in the right order, with the right inputs, and that failures are retried or escalated. When combined, the two produce a workflow that is both reproducible and observable.

This pattern is most useful when a training pipeline has multiple stages — data validation, preprocessing, training, evaluation — and each stage needs a different set of dependencies. Without containers, the orchestrator assumes a shared environment, which creates drift between dev and prod. With containers, the orchestrator schedules images and leaves environment management to each step.

## When to use

- Pipeline steps have conflicting dependencies (e.g., one stage needs a training framework while another needs an inference runtime).
- The same pipeline must run on different compute targets (local, Kubernetes, cloud).
- Lineage tracking is required: knowing exactly which image, code commit, and dataset produced a model.
- Migrating from a notebook-driven workflow to a production scheduler.

## Prerequisites

- A container registry (Docker Hub, ECR, GCR) accessible from the orchestrator.
- An orchestrator that supports containerized steps — Kubeflow Pipelines or Argo Workflows.
- A model registry or artifact store to pass outputs between steps.

## Steps

1. **Containerize each stage independently.** Write a Dockerfile for every stage that has non-trivial dependencies. Use a slim base image and install only what that stage needs. For training stages, include experiment-tracking libraries; for serving stages, include only the inference runtime and health-check endpoint.

2. **Pin base images and dependencies.** Use explicit tags or digest pins. Lock dependency files and bake them into the image. This removes environment-drift failures caused by upstream package updates.

3. **Define the pipeline as a DAG of containers.** In Kubeflow Pipelines, each `@dsl.component` specifies its own `base_image`. The compiler produces a static YAML spec that the KFP service schedules. In Argo, each step references a container image directly. The key invariant is that the pipeline spec describes images, not scripts.

4. **Pass artifacts through typed ports.** Modern SDKs let components declare `Output[Dataset]` or `Output[Model]` artifacts. The orchestrator stores these in ML Metadata (MLMD) or an object store, so downstream steps can consume them without knowing the upstream container's internals.

5. **Verify reproducibility end-to-end.** After compiling the pipeline, run it twice with the same inputs and compare the outputs. If the pipeline is truly reproducible, the second run should produce identical artifacts. Any difference points to non-deterministic code, timestamps baked into the image, or unversioned data.

## Verify

- Pipeline compiles without warnings.
- Each step runs in its own container (check pod specs or step logs).
- Model artifact hash is identical across two runs with the same inputs.
- Failure in one step stops the pipeline; no partial artifacts are promoted.
