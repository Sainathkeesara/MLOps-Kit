# Kubeflow — quick primer

> First-day notes for someone who's never used Kubeflow. Personal voice, plain language.

## What is it?

Kubeflow is a Kubernetes-native platform for machine learning workflows. It sits on top of Kubernetes and gives me a set of tools specifically designed for training, tuning, and deploying models at scale. Think of it this way: Kubernetes is the operating system for my cluster, and Kubeflow is the ML toolbox that runs on top of it. If I already know how to work with containers and `kubectl`, Kubeflow feels like a natural extension — just with ML-specific abstractions instead of raw pod specs.

## What does it do?

The main things I care about right now are **Kubeflow Pipelines** (build and run ML workflows as a series of steps), **Kubeflow Notebooks** (spawn Jupyter-like environments on the cluster), and **KServe** (serve models with a single command). The Pipelines piece is what most people start with — I can chain together data-prep, training, and evaluation steps into a reusable workflow, then trigger it from a web UI or CLI.

## Why does it exist?

Before Kubeflow, if I wanted to run an ML experiment on Kubernetes I had to write custom YAML, manage storage mounts by hand, and wire together monitoring and serving myself. Every team reinvented the same glue code. Kubeflow provides a shared, opinionated layer so I can focus on the ML logic instead of the infrastructure plumbing. Data scientists, ML engineers, and platform teams all use it to move experiments from notebook to production without leaving the Kubernetes ecosystem.

## Key terminology

- **Pipeline** — A directed acyclic graph (DAG) of steps that defines an ML workflow. Example: a pipeline that reads data, trains a model, and evaluates it.
- **Component** — A single step inside a pipeline, packaged as a lightweight container. Example: a "train" component that takes a dataset path and outputs a model artifact.
- **Experiment** — A named grouping for pipeline runs so I can compare related executions. Example: an experiment called `iris-classifier` that holds all my tuning runs.
- **Run** — One execution of a pipeline with specific input parameters and outputs. Example: run #17 of my experiment with `learning_rate=0.01`.
- **KFP (Kubeflow Pipelines SDK)** — The Python library I use to define pipelines and components. Example: `from kfp import dsl` to build a DAG.
- **KServe** — The model-serving component that deploys a trained model as a scalable REST endpoint. Example: `kserve deploy` to expose my model on `/v1/models/...`.
- **Notebook controller** — The operator that manages Jupyter notebook instances on the cluster. Example: spin up a notebook with a pre-installed image and GPUs attached.

## A tiny example

```python
from kfp import dsl
from kfp.dsl import Dataset, Model, Metrics

@dsl.component
def train(model: dsl.Output[Model], metrics: dsl.Output[Metrics]):
    # a toy training step
    model.metadata["accuracy"] = 0.94
    metrics.log_metric("accuracy", 0.94)

@dsl.pipeline(name="my-first-pipeline")
def my_pipeline():
    train()

from kfp.client import Client
Client().create_run_from_pipeline_func(my_pipeline, experiment_name="demo")
```

This defines a one-step pipeline with the KFP SDK and submits it to a Kubeflow cluster. The UI will show the run under the `demo` experiment.

## What I'll cover next

Next I want to install Kubeflow on a local cluster (probably Kind), build a slightly longer pipeline with a real dataset, and then play with the UI to inspect run artifacts and compare metrics across executions.
