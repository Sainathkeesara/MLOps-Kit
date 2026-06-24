# Pipeline Orchestration — quick primer

> First-day notes on Pipeline Orchestration. What it is, why it matters, and the key ideas to know.

## What is it?

Pipeline orchestration is the practice of wiring together individual ML steps (data loading, preprocessing, training, evaluation, deployment) into a repeatable, automated sequence. Think of it like Airflow for ML, but with special awareness for how data flows between steps and how models get versioned. Instead of manually running scripts in order, you define a graph where each node is a compute job and edges represent data dependencies.

Before orchestration tools, I'd chain bash scripts with `&&` or write Python scripts that called functions in order, hoping nothing failed mid-way. That breaks down fast when you need retries, parallelism, caching, or when steps run on different machines.

## Why does it matter for MLOps?

ML workflows aren't one-off notebooks — they need to run nightly, on new data, triggered by events, or when models drift. Orchestration makes this reliable:
- It tracks lineage: if the model fails, you can trace back which raw data version produced it.
- It handles failures gracefully: a stuck job can be retried without rerunning the whole pipeline.
- It enables scheduling: train every morning on yesterday's data automatically.
- It scales across machines: step 2 can run on a GPU cluster while step 1 runs on a small CPU instance.

Every MLOps system — from Kubeflow to Metaflow to ZenML — starts here because you can't have continuous training or deployment without a way to reliably stitch steps together.

## Key terminology

- **Pipeline** — A directed acyclic graph (DAG) of ML steps that must run in order. Example: train → evaluate → register, where evaluation waits for training to finish.
- **Step** — An individual unit of work in a pipeline (data load, transform, train). Example: a Python function that reads CSV and outputs features.
- **Task** — A specific execution of a step with concrete inputs. Example: the training step for run #2026-06-23-abc123.
- **DAG** — The dependency graph that defines order: edges point from upstream to downstream steps. Example: data_prep → train → evaluate.
- **Dependency** — The input data or artifact a step needs to run. Example: evaluate needs the model artifact from train.
- **Trigger** — What starts a pipeline: a schedule, a code push, or new data arrival. Example: run nightly at 2am.
- **Cache** — Storing step outputs so re-running the pipeline skips already-done work. Example: skip retraining if input data hasn't changed.
- **Parameter** — A runtime input to the pipeline that can vary between runs. Example: learning_rate=0.001 vs learning_rate=0.01.
- **Artifact** — A file or object produced by a step (model weights, metrics JSON). Example: the pickle file written by the train step.
- **Executor** — Where a step actually runs: locally, in Kubernetes, or in a cloud environment.

## A concrete example

```python
# Minimal pipeline with three steps using a simple orchestrator
def ingest():
    df = pd.read_csv("s3://bucket/raw.csv")
    return df

def train(data):
    model = fit_model(data)
    return model

def evaluate(model):
    score = model.score(test_data)
    return score

# Build the pipeline DAG
pipeline = Pipeline()
pipeline.then(ingest).then(train).then(evaluate)
pipeline.run()
```

This shows the core idea: each step produces something the next step consumes, and the orchestrator manages the execution order.

## How this connects to what's next

Pipeline orchestration is the backbone for feature stores (orchestrate feature computation), model serving (automate deployment steps), and monitoring (trigger retraining when drift is detected). Next I want to try running this pattern in Metaflow and see how their step decorators map to this mental model.