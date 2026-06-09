# KFP v2 SDK gotchas and first component exploration

> L2 notes on KFP v2 SDK surprises encountered during component writing and pipeline compilation.

## Steps I took

Started with the official KFP v2 SDK quickstart and expanded into trying my own minimal component. Cluster was already set up from the minikube session, so I jumped straight to writing and compiling.

## Got stuck on

### `kfp` vs `kfp.deprecated` import confusion

The quickstart uses `from kfp import dsl` which pulls from `kfp>=2.0`. But some older examples in blogs still import from `kfp.dsl` which silently gives you the v1 DSL. My component looked fine but the compiled YAML had v1 structure. Had to ensure `pip install 'kfp>=2.0'` and check `dsl.__version__` to confirm.

### `@dsl.component` decorator behavior

In v2, `@dsl.component` wraps a Python function and expects it to be importable. Unlike v1 where you could inline command strings, v2 serializes the function code into the component. I tried:

```python
@dsl.component
def my_op():
    print("hello")  # Implicit return None
```

The function returns `None`, which compiles fine but downstream steps expecting string input fail. Need to either return a value or use `dsl.OutputPath()` for file passing.

### Containerized function = whole file gets packaged

My component file lived next to unrelated code and I was surprised that `kfp.compiler.Compiler().compile()` embedded the entire `.py` file's source into the component. Moving components to dedicated files kept the YAML clean and avoided leaking secrets into the container spec.

### Pipeline root must be explicit

If I omit `pipeline_root` in the `@dsl.pipeline` decorator, the compile succeeds but the run fails with `INVALID_ARGUMENT`. The error message mentions "pipeline root is empty" which only makes sense in hindsight. Always set it:

```python
@dsl.pipeline(name="my-pipe", pipeline_root="s3://bucket/pipelines")
```

### Multi-step component wiring

The quickstart single-component example doesn't show how to wire outputs to inputs:

```python
step_a = component_a()
step_b = component_b(input=step_a.output)  # Not step_a.output!
```

Using `step_a.output` (the output attribute) instead of `step_a.outputs['output']` (dictionary access) is the v2 way. The latter works but feels legacy.

## What I'd try next

Build a three-component pipeline: download → process → train. Want to see how `dsl.Artifact` types flow through the graph and whether I can inspect intermediate outputs in the UI without persisting to external storage.