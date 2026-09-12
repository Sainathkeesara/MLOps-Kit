---
last_verified: 2026-09-12
tool_version: "1.4.39"
sources:
  - https://docs.bentoml.com/en/latest/get-started/hello-world.html
  - https://theneuralbase.com/bentoml/learn/beginner/local-testing/
  - https://www.hivebook.wiki/wiki/bentoml-python-framework-for-serving-ml-ai-models
  - https://github.com/bentoml/BentoML/
---

# BentoML — quick primer

> First-day notes for someone who's never used BentoML. Personal voice, plain language.

## What is it?

I kept running into the same problem: I'd train a model, then spend a whole afternoon wiring up Flask or FastAPI just to serve predictions over HTTP. BentoML is a Python framework that skips that entire step. You define a service class in Python, point it at your model, and it handles the HTTP serving, batching, and container packaging in one go. Think of it as the "just serve it" button for ML models. It's similar to Seldon Core or KServe but way simpler to get started with — no Kubernetes required for local dev.

## What does it do?

I can write a Python class decorated with `@bentoml.service`, add `@bentoml.api` methods that become HTTP routes, and BentoML handles the rest. It loads models (with caching), batches requests for GPU efficiency, generates OpenAPI docs automatically, and builds container images via `bentoml build`. The `bentoml serve` command gives me a local dev server with hot-reload, and `bentoml containerize` produces an OCI image I can deploy anywhere.

## Why does it exist?

Every ML team I've worked on reinvented the model-serving wheel differently. Flask wrapper here, FastAPI wrapper there, hand-rolled Dockerfile, hope the pickle format survives. BentoML exists because that wheel is hard to get right — model format compatibility, request batching, container layer optimization — and nobody wants to solve it from scratch for every project.

## Key terminology

- **Service** — A Python class decorated with `@bentoml.service` that groups related prediction endpoints. Example: `class IrisClassifier` loads a model and exposes `/predict`.
- **API endpoint** — A method inside a service decorated with `@bentoml.api` that becomes an HTTP route. Example: `def predict(self, input: IrisInput) -> IrisOutput` maps to `POST /predict`.
- **Bento** — The packaged output of `bentoml build`: a self-contained directory with your code, model, and dependencies. It's the deployable artifact.
- **Bentofile** — A YAML config file (`bentofile.yaml`) that declares build-time settings like Python version, docker base image, and included packages. Example: `docker: python_version: "3.11"`.
- **Adaptive batching** — BentoML automatically groups incoming requests into batches for GPU efficiency. Requires `batchable=True` on the API method and a list-shaped signature.
- **Model store** — BentoML's local registry for saved models. `bentoml.sklearn.save("iris", model)` stores the model with a version tag that the service loads at startup.
- **Runner** — (Legacy) Pre-2024 tutorials use `bentoml.Service(runners=[...])` for model execution. Modern BentoML 1.2+ uses class-based services; don't mix the two patterns.

## A tiny example

```python
import bentoml
from bentoml.io import NumpyNdarray

@bentoml.service(resources={"cpu": "2"})
class IrisClassifier:
    def __init__(self):
        self.model = bentoml.sklearn.get("iris:latest").to_runner()
        self.model.init_local()

    @bentoml.api(batchable=True)
    def predict(self, input: NumpyNdarray) -> NumpyNdarray:
        return self.model.predict.run(input)
```

This loads a saved scikit-learn model, exposes a batched `/predict` endpoint, and allocates 2 CPU cores. Run with `bentoml serve service.py:IrisClassifier`.

## What I'll cover next

After this primer I plan to dig into BentoML's build workflow — writing a `bentofile.yaml`, building a Bento, and containerizing it. I also want to explore adaptive batching in more depth and figure out how GPU resource allocation works in practice.
