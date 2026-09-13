---
last_verified: 2026-09-13
tool_version: "1.4.39"
sources:
  - https://docs.bentoml.com/en/latest/get-started/hello-world.html
  - https://theneuralbase.com/bentoml/learn/beginner/local-testing/
  - https://theneuralbase.com/bentoml/learn/beginner/bentoml-service-decorator/
  - https://theneuralbase.com/bentoml/learn/beginner/quickstart-resources/
  - https://theneuralbase.com/bentoml/learn/beginner/version-1-2-modern-api/
---

# BentoML — quick primer

> First-day notes for someone who's never used BentoML. Personal voice, plain language.

## What is it?

I just learned that BentoML turns a trained model into an HTTP service. It is a serving framework rather than a general web framework: I define the service and its request methods, then BentoML handles the serving surface and packaging.

## What does it do?

BentoML lets me mark a class with `@bentoml.service` and its request methods with `@bentoml.api`. I can load a model once during initialization, expose prediction methods, and check the generated `/docs` page. `bentoml build` creates a Bento bundle, and `bentoml containerize` turns it into a runnable container.

## Why does it exist?

Without a serving tool, I would write web-server glue and build a container myself. BentoML keeps those pieces together so I can move from a model artifact to a testable service without inventing the setup.

## Key terminology

- **Service** — a class marked with `@bentoml.service` that groups a model and its endpoints.
- **API method** — a method marked with `@bentoml.api` that accepts a request and returns a response.
- **Bento** — the bundle created by `bentoml build`, containing code, model, configuration, and environment details.
- **Containerize** — the step that makes a Bento runnable as a container with `bentoml containerize`.
- **bentofile.yaml** — configuration for packages and container options used while building a Bento.
- **Host** — the address used by `bentoml serve`; `--host 0.0.0.0` allows cross-machine testing.

## A tiny example

```python
import bentoml
import numpy as np

@bentoml.service
class Doubler:
    @bentoml.api
    def predict(self, values: np.ndarray) -> list[float]:
        return [float(value * 2) for value in values]
```

```bash
bentoml serve service:Doubler --host 0.0.0.0
```

This starts the service so I can inspect `/docs` before adding a trained model.

## What I'll cover next

Next I want to save a small model, load it once in a service, and build a Bento. Then I will try the generated container and compare local requests with the `/docs` page.
