---
last_verified: 2026-07-12
tool_version: n/a
sources: []
---

# Seldon Core vs KServe for sklearn model serving — picking the right platform

I spent the last couple days trying to get an sklearn model deployed, and ended up comparing Seldon Core and KServe. Here's what I found.

## What both do

Both are Kubernetes-native model-serving frameworks. You give them a serialised model (pickle, ONNX, etc.) and a wrapper, and they spin up a REST/gRPC endpoint with autoscaling, monitoring, and canary rollouts. On paper they do the same job.

## Where they differ in practice

**KServe** is built on Knative + Istio. If you already have Istio in your cluster, it slots in naturally. The inference-service YAML is clean — one resource kind (`InferenceService`) that handles the model, the transformer, and the explainer. It supports `predictor`, `transformer`, and `explainer` components out of the box. The Python SDK (`kserve`) lets you define custom predictors with minimal boilerplate. I found the quickstart simpler to get running on a fresh kind cluster.

**Seldon Core** uses ambassador or Istio for routing. Its `SeldonDeployment` CRD is more configurable — you can define complex graphs (e.g. ensemble of models with a combiner). The `seldon-core-microservice` wrapper handles the model server, and the Python wrapper (`seldon-core-mlflow`) made it easy to deploy an MLflow-logged model without writing a custom class. The monitoring (prometheus metrics) is richer out of the box — you get request/response logging, metrics, and explainability without extra config.

## What tripped me up

1. **KServe's Knative dependency.** Installing KServe means installing Knative-serving and Istio first. On a low-resource cluster that was already tight, Knative's activator and autoscaler added noticeable overhead. Seldon Core runs without Knative — just ambassador or a simple ingress.

2. **Seldon Core's graph DSL vs KServe's component approach.** Seldon Core's `SeldonDeployment` lets you wire multiple models together in a DAG, but the YAML is nested deeply and I kept getting the indentation wrong. KServe's approach — separate `InferenceService` resources — felt more familiar coming from Kubernetes.

3. **Sklearn-specific paths.** For a single sklearn model without preprocessing:
   - **Seldon Core**: use `seldon-core-mlflow` to point at the MLflow run, or wrap with `SKLearnServer` from `seldon-core`. The `SKLearnServer` handles loading the pickle and calling `.predict()` automatically.
   - **KServe**: use `sklearn` storage-uri in the `InferenceService` spec — point at the model file in S3/GCS and it works. The `SKLearnModel` class from `kserve` does the same as Seldon's version.

4. **Canary rollouts.** KServe's canary is built into the `InferenceService` spec (`canaryTrafficPercent`). Seldon Core needs an Istio VirtualService or ambassador config for the same thing — more moving parts.

## Which one I'd pick

For a single sklearn model with basic needs, **KServe** felt simpler to set up and maintain. If I needed ensemble graphs, richer monitoring, or was already on Istio, I'd go **Seldon Core**.

## What I'd try next

I want to test both with a model that has a custom pre-processing transformer, to see where the wrapper overhead differs.
