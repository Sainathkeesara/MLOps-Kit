# Kubeflow Pipelines quickstart — what tripped me up

> Following the official Kubeflow Pipelines quickstart. L2, first-person notes on what worked and where it broke.

## Steps I followed

I started at the [Kubeflow Pipelines quickstart](https://www.kubeflow.org/docs/components/pipelines/v2/quickstart/).

First I made sure my Kubeflow cluster was running (I set it up earlier with Kind — the cluster from `2026-05-27-kind-cluster-for-kubeflow.md`). Then I installed the KFP SDK v2:

```bash
pip install kfp
```

I checked the version — `2.0.1` at time of writing.

Then I created a minimal pipeline file. The quickstart example defines a component with the `@dsl.component` decorator and uses `dsl.pipeline` to wire it together. I compiled the pipeline, uploaded it through the UI, and ran it.

## Got stuck on

### `dsl.component` vs `@kfp.v2.dsl.component` imports

The quickstart uses `from kfp import dsl` and then `@dsl.component`. But some older blog posts and StackOverflow answers reference `@kfp.v2.dsl.component`. Importing from `kfp.v2` raised a deprecation warning in 2.0. The quickstart is correct — stick with `from kfp import dsl`.

### Pipeline root not set

When I tried to compile the pipeline with `compiler.Compiler().compile(pipeline_func, 'pipeline.yaml')`, it complained about a missing pipeline root. The SDK needs to know where to store artifacts. I fixed it by passing a `pipeline_root` in the `@dsl.pipeline` decorator or setting `KFP_PIPELINE_ROOT` env var. I used an S3-compatible bucket path from the Kind cluster's MinIO service.

### The compile-and-upload loop

Compiling locally, uploading via UI, then running is fine for one-off, but the quickstart doesn't mention `kfp.Client` for programmatic uploads. I added a few lines to submit the run from the same script:

```python
client = kfp.Client(host='http://localhost:8080')
client.create_run_from_pipeline_func(
    my_pipeline,
    arguments={},
    experiment_name='Quickstart'
)
```

This saved a lot of time once I stopped using the UI for each run.

### Run status stale

After submitting a run, the Python client returned almost immediately with a Run object, but the status was still "Pending". I had to poll or just check the UI. There's a `wait_for_completion` method but it defaults to 24h timeout — not great for a quick test. I ended up using `wait_for_completion(timeout=300)` for my tiny pipeline.

## What I'd try next

I want to build a pipeline with multiple components that pass data between each other — the quickstart only shows a single-component pipeline. The V2 SDK has `dsl.OutputPath` and `dsl.InputPath` for typed artifact passing, which looks like the right path for multi-step workflows. I also want to try compiling and running entirely from a notebook instead of the Python script.
