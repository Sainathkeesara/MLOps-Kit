#!/usr/bin/env python3
"""Deploy my first Kubeflow pipeline end-to-end.

Compiles and uploads a pipeline, then creates a run.
Still figuring out the Client auth — port-forwarding for now.
"""

from kfp import dsl, compiler, client


@dsl.component
def say_hello(name: str) -> str:
    return f"Hello, {name}!"


@dsl.pipeline
def hello_pipeline(name: str = "MLOps-Kit"):
    say_hello(name=name)


if __name__ == "__main__":
    # Compile to YAML
    compiler.Compiler().compile(hello_pipeline, "hello-pipeline.yaml")
    print("Compiled hello-pipeline.yaml")

    # Upload and run — assumes `kubectl port-forward ...` is active
    kfp_client = client.Client(host="http://localhost:8080")
    run = kfp_client.create_run_from_pipeline_package(
        "hello-pipeline.yaml",
        arguments={"name": "Kubeflow"},
    )
    print(f"Run ID: {run.run_id}")
    print(f"Run URL: {run.run_url}")
