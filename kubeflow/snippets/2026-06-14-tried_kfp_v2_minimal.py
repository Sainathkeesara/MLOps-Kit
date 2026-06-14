"""kub-009 — Minimal KFP v2 pipeline with the Python SDK.

Two lightweight arithmetic components wired together. I wanted to see
the bare minimum to define, compile, and submit a pipeline w/ v2 SDK.
"""

from kfp import dsl, compiler
import kfp


@dsl.component(base_image="python:3.9-slim")
def add(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b


@dsl.component(base_image="python:3.9-slim")
def multiply(value: int, factor: int) -> int:
    """Multiplies an integer by a factor."""
    return value * factor


@dsl.pipeline(
    name="minimal-v2-pipeline",
    description="add then multiply — simplest DAG I could think of",
)
def my_pipeline(a: int = 3, b: int = 4, factor: int = 2):
    add_task = add(a=a, b=b)
    multiply(value=add_task.output, factor=factor)


if __name__ == "__main__":
    compiler.Compiler().compile(my_pipeline, "minimal-v2-pipeline.yaml")

    # Port-forward the ml-pipeline service to 8080 first:
    #   kubectl port-forward -n kubeflow svc/ml-pipeline 8080:80
    client = kfp.Client(host="http://localhost:8080")
    run = client.create_run_from_pipeline_func(
        my_pipeline,
        arguments={"a": 10, "b": 20, "factor": 3},
        experiment_name="kub-009-test",
    )
    print(f"Submitted run: {run.run_id}")
