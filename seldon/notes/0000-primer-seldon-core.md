---
last_verified: 2026-07-04
tool_version: n/a
---

# Seldon Core — quick primer

> First-day notes for someone who's never used Seldon Core. Personal voice, plain language.

## What is it?

Seldon Core is an open-source platform for deploying, monitoring, and scaling ML models on Kubernetes. It wraps any ML model (pickle, ONNX, TensorFlow, PyTorch, custom container) behind a standardised REST/gRPC API with built-in metrics, request logging, and A/B testing. It lives in the same space as KServe — serving models on Kubernetes — but leans harder into graph-based inference pipelines and integration with Prometheus/Grafana for observability.

I think of Seldon Core as a routing layer: you give it a model image and a deployment config, and it handles the pod management, traffic splitting, and metrics export so you don't have to write a custom inference server every time.

## What does it do?

Seldon Core takes a Docker image that contains your model and serving code, wraps it in a SeldonDeployment custom resource, and exposes it as an HTTP/gRPC endpoint. Out of the box you get Prometheus metrics, request/response logging, canary rollouts, and shadow deployments. It also supports multi-model serving graphs where requests flow through a chain of transformers before hitting the predictor.

## Why does it exist?

Before Seldon Core, adding canary traffic splits, A/B testing, or metrics export to a model endpoint meant wiring up Istio virtual services, Prometheus instrumentation, and logging middleware by hand — every time. Seldon Core exists to package those patterns into a single YAML resource that an MLOps engineer can apply with `kubectl`. It's used by teams running multiple models that need observability and gradual rollout without building a serving platform from scratch.

## Key terminology

- **SeldonDeployment** — The core CRD. A YAML spec that declares one or more model predictors, optional transformers, and routing policy. Example: a SeldonDeployment with two canary versions splitting traffic 90/10.
- **Predictor** — The component that loads the model and responds to inference requests. Each predictor runs in its own pod.
- **Transformer** — An optional step that preprocesses input before it reaches the predictor. Useful for tokenization, image resizing, or feature engineering at serving time.
- **Explainer** — A sidecar that generates model explanations (SHAP, Alibi) alongside predictions.
- **Graph** — Seldon's directed acyclic graph of inference steps. A typical graph is `input → transformer → predictor → output`. You define it in the SeldonDeployment spec.
- **Canary deployment** — Route a percentage of traffic to a new model version alongside the current one. Seldon measures error rate and auto-rolls back if it spikes.
- **Shadow deployment** — Send mirrored traffic to a new model without returning its predictions to the user. Useful for offline validation.
- **Prometheus metrics** — Seldon exports request count, latency, and error rate per model by default. No custom instrumentation needed.
- **Ambassador / Istio** — Seldon integrates with Ambassador API Gateway or Istio for external traffic routing and TLS termination.
- **Model Docker image** — The model must be packaged as a Docker image with a Seldon-compatible API wrapper. Seldon provides base wrappers for Python, Java, and R.

## A tiny example

```yaml
apiVersion: machinelearning.seldon.io/v1
kind: SeldonDeployment
metadata:
  name: sklearn-iris
spec:
  name: iris
  predictors:
  - graph:
      implementation: SKLEARN_SERVER
      modelUri: gs://your-bucket/models/iris-model.pkl
      name: classifier
    name: default
    replicas: 1
```

This deploys an Iris classifier with Seldon's built-in sklearn server. Apply with `kubectl apply -f seldondeployment.yaml` and the model is live behind `http://<cluster-ip>/seldon/default/sklearn-iris/api/v1.0/predictions`.

## What I'll cover next

I want to install Seldon Core on a local cluster, deploy this sklearn model, and try sending predictions through the Python SDK. After that I'll look at canary deployments and how the graph-based routing lets me chain transformers before inference.
