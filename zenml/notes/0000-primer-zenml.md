# ZenML — quick primer

> First-day notes for someone who's never used ZenML. Personal voice, plain language.

## What is it?

ZenML is an MLOps framework that ties your ML code to infrastructure through a pipeline abstraction. If MLflow is a tracking server you call from your scripts, ZenML is more like a framework your scripts live inside — it manages the pipeline DAG, caches step outputs, swaps out backends, and keeps a metadata log of everything that ran. I think of it as "MLflow + Airflow, but purpose-built for ML and with a consistent Python API."

## What does it do?

It lets me define ML pipelines as Python functions with decorators, run them locally during development, then switch to a remote orchestrator (like Kubeflow, Airflow, or Vertex AI) by changing a single line of config. It caches steps that haven't changed, logs parameters and artifacts automatically, and keeps a metadata store I can query later.

## Why does it exist?

Before ZenML, teams would cobble together a pipeline by gluing a tracking tool (MLflow) to an orchestrator (Airflow/Kubeflow) with custom wiring. The glue code — translating configs, passing URIs, handling caching — was different every time. ZenML standardises that layer so the pipeline code stays the same whether I'm running on my laptop or on a remote K8s cluster.

## Key terminology

- **Pipeline** — A directed acyclic graph of steps, defined as a Python function with `@pipeline`. Example: a training pipeline with `ingest_data() -> prepare_features() -> train_model() -> evaluate_model()`.
- **Step** — A single unit of work, defined with `@step`. Each step runs in its own execution context. Example: `@step` def `train_model(X_train, y_train)` that returns a trained classifier.
- **Stack** — A configuration that says "here are my orchestrator, artifact store, metadata store, and container registry." Switching stacks is how I move from running things on my laptop to running them on a remote cluster.
- **Artifact store** — Where step outputs are saved (local filesystem, S3, GCS, MinIO).
- **Metadata store** — A database (SQLite, MySQL, PostgreSQL) that logs pipeline runs, step status, parameters, and artifact URIs.
- **Orchestrator** — The backend that actually runs the pipeline steps (local, Kubeflow, Airflow, Vertex AI, etc.).
- **Materializer** — A component that knows how to serialize/deserialize a Python type to/from the artifact store. ZenML includes default materializers for `DataFrame`, `np.ndarray`, `torch.nn.Module`, etc.

## A tiny example

```python
from zenml import pipeline, step

@step
def load_data() -> dict:
    return {"X": [1, 2, 3], "y": [0, 1, 0]}

@step
def train_model(data: dict) -> str:
    accuracy = 0.95  # pretend this came from real training
    return f"Model trained with accuracy {accuracy}"

@pipeline
def training_pipeline():
    data = load_data()
    result = train_model(data)

if __name__ == "__main__":
    training_pipeline()
```

Running `python hello_zenml.py` executes the pipeline locally with the default stack. ZenML prints a run summary and stores the run in the local SQLite metadata store.

## What I'll cover next

After this primer I want to install ZenML, set up a real stack with a remote artifact store, and build a pipeline that does actual data loading and model training — not just string printing. Then I'll look at the ZenML dashboard to inspect run history.
