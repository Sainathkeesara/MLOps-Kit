# Kubeflow Pipelines quickstart — second pass trip-ups

> L2 notes on my second run-through of the KFP v2 quickstart. First-person, what differed from the first time.

## Steps I took

I went back to the [KFP v2 quickstart](https://www.kubeflow.org/docs/components/pipelines/v2/quickstart/) today to build on what I captured in `2026-05-27-pipelines-quickstart-trip-ups.md`. Cluster was already up from the minikube + CLI session (`2026-06-06-install-minikube-and-kubeflow-cli.md`), so I jumped straight to the SDK part.

I opened a fresh virtualenv and ran `pip install 'kfp>=2.0'`. This time I hit version `2.7.1`, a few minor versions ahead of the `2.0.1` I noted last time.

## Got stuck on

### `@dsl.component` without a base_image

On my first pass I used the default base image and it worked. This time I left the decorator minimal:

```python
@dsl.component
def my_component(text: str) -> str:
    return text.upper()
```

The pipeline compiled but the resulting run pod couldn't pull `python:3.9` because my Kind cluster doesn't have internet access. I added `base_image='python:3.9-slim'` explicitly and the run completed. I forgot about the network constraint because my usual dev cluster has egress.

### Using `InputPath` / `OutputPath` for the first time

The quickstart inline example passes plain strings, so I didn't see the typed artifact passing. I tried to extend it with `OutputPath` and the compile step failed:

```python
@dsl.component
def process(path: dsl.OutputPath('String'), data: str):
    ...
```

The compiler expects `dsl.OutputPath()` with no type argument for raw files, and you have to import `OutputPath` directly from `kfp.dsl`. I was trying to type hint it like a Python type annotation — that's not how it works. The fix:

```python
from kfp.dsl import OutputPath

@dsl.component
def write_file(path: OutputPath(), content: str):
    ...
```

### Pipeline root from the environment

I set `pipeline_root='s3://my-bucket/pipeline-root'` inside the `@dsl.pipeline` decorator. Works fine when the bucket exists. But when I removed the argument to test the env var fallback, the compile step silently produced a pipeline.yaml with an empty pipeline root. The run then failed with a cryptic `INVALID_ARGUMENT` error from the KFP backend. I should have read the error message earlier — it clearly says "pipeline root is empty". The lesson: always explicitly set pipeline root until I trust the env var fallback.

## What I'd try next

I want to wire two components together with `OutputPath` / `InputPath` so data flows between them. The quickstart example is single-component only, so I need to look at the multi-step guides in the KFP docs. I also want to try `kfp.Client().create_run_from_pipeline_func` instead of compiling to YAML and uploading manually.
