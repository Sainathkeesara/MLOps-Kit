# ClearML Orchestration — quick primer

> First-day notes for someone who's never used ClearML Orchestration. Personal voice, plain language.

## What is it?

ClearML is an open-source MLOps platform that started as Allegro Trains. ClearML Orchestration is the part of it that lets you define, schedule, and run tasks and pipelines — the workflow engine under the hood. If you've used Apache Airflow for data pipelines, think of ClearML Orchestration as Airflow but purpose-built for ML workflows: it's aware of experiments, models, datasets, and compute environments.

## What does it do?

It lets you wrap any Python code into a `Task`, set its parameters and dependencies, and execute it either locally or on a remote worker (called a ClearML Agent). You can chain tasks into pipelines with directed acyclic graphs, schedule recurring runs, and monitor execution in the web UI. It also handles queue management — you submit tasks to a queue, and idle agents pick them up.

## Why does it exist?

Before ClearML, I'd have to glue together something like Airflow for scheduling, MLflow for experiment tracking, and a homegrown solution for compute management. ClearML Orchestration bundles all three into one API. It exists so that MLOps teams don't have to stitch together five different tools just to get a training pipeline running on a remote GPU machine.

## Key terminology

- **Task** — The fundamental unit of work. A Task wraps a Python script or function with metadata like parameters, requirements, and output models. Example: `Task.init(project_name="my-project", task_name="train-model")`.
- **Queue** — A named queue that holds tasks waiting to be executed. Agents listen on specific queues. Example: `queue="default"` vs `queue="gpu"`.
- **Agent** — A service that runs on a machine, pulls tasks from a queue, and executes them. Agents can be configured with Docker containers, so the execution environment is reproducible.
- **Pipeline** — A DAG of Tasks connected via dependencies. Defined with decorators like `@Pipeline.add_step()` or the PipelineController class.
- **ClearML Server** — The backend that stores task metadata, logs, artifacts, and serves the web UI. You can use the free hosted tier or self-host.
- **Artifact** — A file or object that a Task produces or consumes. Models, datasets, plots — anything you upload or download. Example: `task.upload_artifact(name="model", artifact_object=model)`.
- **Configuration** — A set of hyperparameters or settings tied to a Task. Stored as key-value pairs or nested dicts. Example: `task.set_parameters({"lr": 0.001, "epochs": 10})`.

## A tiny example

```python
from clearml import Task

task = Task.init(project_name="Hello", task_name="first-task")
task.set_parameters({"greeting": "hello world"})
print("parameters logged:", task.get_parameters())
```

This creates a Task, logs a parameter, and prints it back. The Task appears in the ClearML web UI under the "Hello" project.

## What I'll cover next

Now that I know what a Task is and how to log parameters, I'll try chaining multiple tasks into a pipeline and running them on a remote agent. I also want to figure out how ClearML handles containerized environments on a GPU queue.
