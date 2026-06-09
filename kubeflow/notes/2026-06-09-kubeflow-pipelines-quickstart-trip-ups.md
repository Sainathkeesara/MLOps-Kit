# Kubeflow Pipelines quickstart — trip-ups on my third run

> L2 notes on running through the KFP v2 quickstart again today. I've done this twice before and still found new things to trip on.

## Steps I took

I started a fresh venv and installed `kfp>=2.0`. Got version `2.7.1` this time. My minikube cluster was already running from the previous session, so I skipped setup and went straight to building a pipeline.

I copied the quickstart's `my_component` and `add` component examples into a notebook cell, then wired them into `@dsl.pipeline`. The compile step worked, I uploaded the resulting YAML with `kfp.Client().upload_pipeline`, and kicked off a run.

## Got stuck on

### Component outputs don't auto-forward

I assumed chaining components would auto-pass outputs like Airflow XComs. I wrote:

```python
@dsl.pipeline(name='add-pipeline')
def add_pipeline(a: int = 1, b: int = 2):
    add_task = add(a=a, b=b)
    print_result(text=add_task.output)
```

It compiled fine but the run errored out with `TypeError: ... output is not a string`. I forgot that `add_task.output` is a `kfp.dsl.Artifact` object, not the raw value. The fix was either to change the `print_result` component to accept the artifact type, or to just pass the component's named output property explicitly. I landed on:

```python
from kfp.dsl import Artifact, Input, Output

@dsl.component
def show(artifact: Input[Artifact]):
    print(artifact.path)
```

That made it click — KFP treats everything as an artifact path, not an in-memory value. Coming from Airflow and Metaflow, the mental shift is that there's no XCom-style serialization unless you explicitly use artifact passing.

### `kfp.Client().create_run_from_pipeline_func` needs a package path

I tried skipping the YAML compile step and calling the client directly with my pipeline function. The docs show this:

```python
client.create_run_from_pipeline_func(
    my_pipeline,
    arguments={...}
)
```

But I got a 400 error. Turns out the SDK version I'm on expects `pipeline_file` to point at a compiled YAML, not a function reference. The two-argument form that takes a function directly must have been removed or renamed between minor releases. I ended up doing the compile-then-upload flow and it worked.

### Minikube runs fail silently when a component image is missing

I built a custom component with `base_image='python:3.12'` but never pushed it to any registry. The pipeline run sat in "Running" for five minutes then moved to "Failed" with no log output. I had to exec into the ml-pipeline pod to see the real error: `ImagePullBackOff`.

Since minikube has no external egress and no local registry by default, the pod can't pull the image. I fixed it by loading the image directly into minikube:

```bash
minikube image load python:3.12
```

Or by adding a local registry. For now, loading the image works.

## What I'd try next

I want to actually pass an `OutputPath` between two components instead of just printing artifacts. The quickstart examples stop at single-component pipelines, so I'll have to stitch two steps together and see where the type hints break. I also want to get the direct `create_run_from_pipeline_func` form working so I can skip the compile step entirely — that feels cleaner for iterative dev.
