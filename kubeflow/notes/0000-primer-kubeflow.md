# Kubeflow — quick primer

> First-day notes for someone who's never used Kubeflow. Personal voice, plain language.

## What is it?

Kubeflow is a platform for running ML workflows on Kubernetes. I think of it as "ML ops for people who already have a K8s cluster." If MLflow tracks experiments, Kubeflow orchestrates the whole pipeline on K8s.

## What does it do?

It lets me define ML pipelines as containerized components, execute them on a K8s cluster, track experiments, and deploy models. Bundles notebooks, a pipeline dashboard, and integration with Katib and KServe.

## Why does it exist?

Before Kubeflow, teams deploying ML on K8s had to wire everything together themselves. Everyone built their own brittle glue. Kubeflow assembles the common pieces so you focus on the ML code.

## Key terminology

- **Pipeline** — A DAG of containerized components. Example: a three-step pipeline that preprocesses, trains, then evaluates.
- **Component** — A single step in a pipeline, packaged as a container with inputs and outputs.
- **Experiment** — A logical grouping of pipeline runs.
- **Run** — A single execution of a pipeline.
- **Central Dashboard** — The web UI that ties everything together.

## A tiny example

```yaml
apiVersion: pipelines.kubeflow.org/v1beta1
kind: Pipeline
metadata:
  name: hello-kubeflow
spec:
  pipelineSpec:
    components:
      comp-echo:
        implementation:
          container:
            image: alpine:3.18
            command: ["echo"]
            args: ["Hello from Kubeflow"]
```

This defines a single-component pipeline that prints a message. I'd upload the YAML through the Pipelines UI to create my first run.

## What I'll cover next

After this primer I want to install Kubeflow locally, click around the dashboard, then build my first real pipeline component.
