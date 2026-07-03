# KServe — quick primer

> First-day notes for someone who's never used KServe. Personal voice, plain language.

## What is it?

KServe is a Kubernetes-based platform for serving ML models at scale. Think of it like a deployment layer that sits on top of Kubernetes and Knative — the same way Docker Compose abstracts running containers, KServe abstracts running a model server. You define an InferenceService YAML, and KServe handles spinning up the predictor, the networking, and the scaling rules so you can send predictions via HTTP or gRPC without building a serving API yourself.

I've seen it described as "the next generation of KFServing" — same mission (serverless inference on Kubernetes), but redesigned for the v0.7+ KServe API. It works with all the common ML frameworks: scikit-learn, XGBoost, TensorFlow, PyTorch, ONNX, and custom containers. The big practical win is that you get autoscaling to zero out of the box. If nobody's hitting your model endpoint, the pod goes away and you pay nothing in compute.

## What does it do?

KServe takes a trained model artifact (usually stored in S3, GCS, or a persistent volume) and exposes it as a REST/gRPC endpoint on your cluster. You create an InferenceService resource, which declares your model, the runtime (serverless or raw Kubernetes), and optional canary rollout or transformer steps. Behind the scenes it provisions a Knative service, configures an Istio virtual service for routing, and sets up autoscaling based on concurrency or requests-per-second. You send a POST with input data and get predictions back.

## Why does it exist?

Before KServe, data scientists would train a model and then hand it off to an ML engineer who'd write a FastAPI wrapper, build a Docker container, write a Kubernetes deployment + service, configure autoscaling, and set up an ingress. That's real work for what's conceptually a simple operation: "take this model and let me call it over HTTP." KServe exists because model deployment is a solved problem with a known shape — the framework, not the team, should own the boilerplate. It's used by ML platforms and MLOps engineers who want to offer model-as-a-service without customizing every endpoint.

## Key terminology

- **InferenceService** — The core KServe resource. YAML that declares your model URI, runtime, and serving config. Example: a 20-line YAML that turns a scikit-learn pickle into a live endpoint.
- **Predictor** — The component that actually loads the model and runs inference. KServe ships pre-built predictors for sklearn, XGBoost, TensorFlow, etc.
- **Transformer** — An optional step before prediction that preprocesses inputs (tokenization, image resizing). Lets you ship the preprocessing logic alongside the model.
- **Explainer** — An optional sidecar that generates model explanations (SHAP, LIME) alongside each prediction.
- **Canary rollout** — Gradually shift traffic from one model version to another. Example: route 10% of requests to a new model version, monitor for errors, then promote to 100%.
- **Knative** — The Kubernetes add-on that gives KServe serverless scaling (scale to zero, scale based on request concurrency).
- **Istio** — The service mesh KServe uses for traffic routing, TLS, and observability between services.
- **ModelMesh** — An optional serving runtime from Red Hat that caches multiple models in a single pod pool for high-throughput, multi-model deployment.
- **InferenceGraph** — KServe's DAG-based routing for complex topologies (ensemble models, A/B testing, cascading).

## A tiny example

```yaml
apiVersion: "serving.kserve.io/v1beta1"
kind: "InferenceService"
metadata:
  name: "sklearn-iris"
spec:
  predictor:
    model:
      modelFormat:
        name: sklearn
      storageUri: "gs://your-bucket/models/iris-model.pkl"
```

This creates an InferenceService named `sklearn-iris` that loads a scikit-learn Iris model from GCS, exposes it on `/v1/models/sklearn-iris:predict`, and handles autoscaling automatically. The first request that hits the endpoint triggers a cold start; subsequent requests hit the warmed pod.

## What I'll cover next

After the primer I want to dig into the Python SDK for programmatic InferenceService creation, look at canary rollouts with traffic splitting, and understand how transformers let me ship preprocessing alongside the model artifact.
