# last_verified: 2026-07-03
# kub-025 — Install Kubeflow and run my first KFP pipeline (L1)

from kfp import dsl, compiler, client


@dsl.component(base_image="python:3.9-slim")
def hello_component(name: str) -> str:
    """Prints a greeting and returns it."""
    msg = f"Hello, {name}!"
    print(msg)
    return msg


@dsl.pipeline(name="first-hello-pipeline", description="My first KFP pipeline.")
def hello_pipeline(name: str = "Kubeflow"):
    hello_component(name=name)


if __name__ == "__main__":
    compiler.Compiler().compile(hello_pipeline, "first-hello-pipeline.yaml")
    print("Compiled to first-hello-pipeline.yaml")
    # Port-forward first: kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
    kfp_client = client.Client(host="http://localhost:8080")
    run = kfp_client.create_run_from_pipeline_package(
        "first-hello-pipeline.yaml", arguments={"name": "MLOps-Kit"}
    )
    print(f"Run submitted: {run.run_id}")