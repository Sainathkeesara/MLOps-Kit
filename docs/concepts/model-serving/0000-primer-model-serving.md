# Model Serving — quick primer

> First-day notes on Model Serving. What it is, why it matters, and the key ideas to know.

## What is it?

Model serving is the practice of exposing a trained ML model as a service that other applications can query. Think of it as turning a pickle file into a REST endpoint: you load your model, wrap it in an API, and deploy it to a system that handles scaling, monitoring, and traffic routing. The goal is to let apps get predictions from your model without knowing anything about pandas, scikit-learn, or how you trained it.

Before serious serving tools, I'd write a Flask app in an evening, deploy it once, and cross my fingers. That works until you need canary rollouts, GPU scaling, or to roll back a broken model. Model serving platforms handle the production concerns so you can focus on getting predictions right.

## Why does it matter for MLOps?

Training is only half the story — most ML value comes from predictions in production. Model serving bridges that gap by:
- Making models queryable via HTTP/gRPC without exposing training code.
- Handling scale: from 10 requests per day to 10,000 per second.
- Enabling safe rollouts: gradual traffic shifts, easy rollbacks.
- Tracking usage: how many predictions, latency, errors.
- Managing multiple versions: A/B testing and blue-green deployments.

Without serving infrastructure, you're stuck with manual deploys and brittle scripts. With it, deployment becomes a repeatable process.

## Key terminology

- **Inference** — Running a model on new data to generate predictions. Example: scoring a single user transaction.
- **REST endpoint** — An HTTP API that accepts JSON input and returns predictions. Example: POST /predict with `{"features": [...]}`.
- **gRPC** — A binary protocol for high-performance model serving. Lower latency than REST for high-throughput use cases.
- **Model server** — The runtime process that loads and serves a model. Example: KServe controller, Seldon engine.
- **InferenceService** — A Kubernetes CRD (Custom Resource Definition) that declares how a model should be served. Example: name=my-model, version=1, runtime=sklearn.
- **Transformer** — Pre/post-processing logic bundled with the model. Example: normalizing input features before calling the model.
- **Canary rollout** — Gradually shifting traffic to a new model version. Example: 10% traffic to v2, 90% to v1.
- **Replica** — Multiple copies of a model server to handle load. Example: 3 replicas serving 3,000 requests per second.
- **Autoscaling** — Dynamically adjusting replicas based on traffic. Example: spin up more replicas when CPU exceeds 70%.

## A concrete example

```python
# Using KServe Python SDK to deploy
from kserve import V1beta1InferenceService

isvc = V1beta1InferenceService(
    metadata={'name': 'sklearn-iris'},
    spec=V1beta1InferenceServiceSpec(
        predictor=V1beta1SKLearnSpec(
            storage_uri='gs://my-bucket/models/iris.pkl',
            resources={'limits': {'cpu': '1', 'memory': '2Gi'}}
        )
    )
)
kserve_client.create(isvc)
```

This creates an InferenceService that loads a sklearn model from GCS and serves it on an HTTP endpoint. Traffic routes to this service automatically.

## How this connects to what's next

Model serving depends on containers (to package models consistently), pipeline orchestration (to automate training-to-deployment), and monitoring (to detect when accuracy drops). Next I'll see how KServe and Seldon Core handle these concerns differently.