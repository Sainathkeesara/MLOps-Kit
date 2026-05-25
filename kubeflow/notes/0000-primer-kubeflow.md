# Kubeflow — quick primer

> First-day notes for someone who's never used Kubeflow. Personal voice, plain language.

## What is it?

Kubeflow is a platform for running machine learning workflows on Kubernetes. I think of it as "ML ops for people who already have a Kubernetes cluster." If MLflow tracks experiments and DVC versions data, Kubeflow orchestrates the whole pipeline — from data prep through training to serving — on top of K8s.

## What does it do?

It lets you define ML pipelines as a series of components (each running in its own container), execute them on a Kubernetes cluster, track experiments, and deploy trained models as inference services. It bundles Jupyter notebooks, a pipeline dashboard, and integration with tools like Katib (hyperparameter tuning) and KServe (model serving).

## Why does it exist?

Before Kubeflow, teams deploying ML on Kubernetes had to wire everything together themselves — spin up containers, manage storage, set up monitoring, handle retries. Every team built their own brittle glue. Kubeflow assembles the common pieces into one distributable platform so you focus on the ML code, not the plumbing.

## Key terminology

- **Pipeline** — A directed acyclic graph (DAG) of containerized components. Example: a three-step pipeline that preprocesses data, trains a model, then evaluates it.
- **Component** — A single step in a pipeline, packaged as a container with defined inputs and outputs. Example: a component that normalizes CSV columns, outputs a cleaned Parquet file.
- **Experiment** — A logical grouping of pipeline runs. Example: "try-all-learning-rates" groups 10 runs with different LR values.
- **Run** — A single execution of a pipeline. Example: one run of the training pipeline with batch_size=32.
- **Recurring Run** — A pipeline that executes on a schedule. Example: retrain a model every Monday at midnight.
- **Notebook Server** — A Jupyter environment spun up inside the cluster, with pre-configured ML libraries. Example: launch a notebook server with 2 CPUs and 4 GB RAM from the Central Dashboard.
- **Central Dashboard** — The web UI that ties all Kubeflow components together. Example: visit http://localhost:8080 to see pipelines, notebooks, and experiments in one place.

## A tiny example

```yaml
apiVersion: pipelines.kubeflow.org/v1beta1
kind: Pipeline
metadata:
  name: hello-kubeflow
spec:
  pipelineSpec:
    description: "A minimal one-step pipeline"
    root:
      dag:
        tasks:
          echo:
            componentRef:
              name: comp-echo
    components:
      comp-echo:
        implementation:
          container:
            image: alpine:3.18
            command: ["echo"]
            args: ["Hello from Kubeflow"]
```

This defines the simplest possible pipeline — a single component that prints a message. I'd upload the YAML through the Kubeflow Pipelines UI to create my first run.

## What I'll cover next

After this primer I want to install Kubeflow locally (probably with the kind-based quickstart), click around the dashboard once it's up, then build my first real pipeline component that does actual ML work.
