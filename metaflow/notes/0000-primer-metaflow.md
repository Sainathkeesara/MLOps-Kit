# Metaflow — quick primer

> First-day notes for someone who's never used Metaflow. Personal voice, plain language.

## What is it?

Metaflow is a Python framework for building and managing data science workflows, originally built at Netflix. If MLflow is about tracking experiments and Kubeflow is about running pipelines on Kubernetes, Metaflow sits somewhere in between — it gives you a simple Python API to define multi-step workflows (DAGs) that scale from your laptop to the cloud without rewriting code.

## What does it do?

You write a flow as a Python class with steps decorated by `@step`. Each step is a function that does one thing — load data, process it, train a model. Metaflow handles the orchestration: it runs steps in order, passes data between them, snapshots intermediate state, and lets you resume from a failed step. It also integrates with AWS, GCP, and Azure so the same flow that runs locally can run on batch compute without changes.

## Why does it exist?

Before Metaflow, data scientists who wanted workflow orchestration had to choose between heavy platforms (Airflow, Kubeflow) or manual scripts. Airflow is great for scheduled DAGs but not designed for iterative data science. Kubeflow assumes Kubernetes. Scripts break silently. Metaflow targets the "data scientist on a laptop" use case first — you get versioned runs, automatic snapshots, and a clean Python API — with optional cloud scaling when you need it.

## Key terminology

- **Flow** — The top-level unit of work; a Python class that inherits from `FlowSpec`. Example: `class MyFlow(FlowSpec):` defines one flow.
- **Step** — A single stage in the flow, decorated with `@step`. Example: `@step` on a `load_data` method that reads a CSV.
- **Artifact** — Any Python object stored as part of a step's data. Example: `self.data = pd.read_csv("input.csv")` — `self.data` becomes an artifact Metaflow snapshots.
- **Run** — One execution of a flow. Example: `my_flow.run()` creates a run with a unique ID.
- **Namespace** — A grouping for runs, typically per user. Example: runs under `production` vs `experimental`.
- **Datastore** — Where Metaflow stores artifacts and metadata (local filesystem or S3). Example: local metadata goes to `~/.metaflow/`.
- **Metadata Service** — An optional REST service that tracks run metadata for team visibility. Example: start with `METAFLOW_SERVICE_URL` pointing to a shared server.

## A tiny example

```python
from metaflow import FlowSpec, step

class HelloFlow(FlowSpec):

    @step
    def start(self):
        self.message = "Hello from Metaflow"
        self.next(self.end)

    @step
    def end(self):
        print(f"Message: {self.message}")

if __name__ == "__main__":
    HelloFlow().run()
```

This defines a two-step flow that sets a message in the first step and prints it in the second. Running it with `python hello_flow.py` shows Metaflow's run logging and stores artifacts.

## What I'll cover next

After this primer I want to install Metaflow, set up a project scaffold with a conda environment, then build a real flow that loads data, trains a model, and evaluates it — the full end-to-end loop.
