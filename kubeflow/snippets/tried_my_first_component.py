"""Minimal Kubeflow Pipelines component — just adds two numbers."""

from kfp import dsl


@dsl.component(base_image="python:3.9-slim")
def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    # not sure if this actually runs standalone outside a pipeline
    print(add(a=3, b=5))
