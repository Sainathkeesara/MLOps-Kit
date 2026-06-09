"""Minimal KFP v2 pipeline end-to-end with Python SDK.

One component does data prep, another trains, then evaluates.
All wired with typed artifact passing.
"""

from kfp import dsl, compiler
import kfp


@dsl.component(base_image="python:3.9-slim")
def prep_data(output_path: dsl.OutputPath(str)):
    """Generates a small dataset."""
    with open(output_path, "w") as f:
        f.write("x,y\n")
        for i in range(10):
            f.write(f"{i},{i*2}\n")


@dsl.component(base_image="python:3.9-slim")
def train_model(
    data_path: dsl.InputPath(str),
    model_path: dsl.OutputPath(str),
):
    """Trains a model on the data."""
    with open(data_path) as f:
        lines = f.readlines()[1:]  # skip header
    n = len(lines)
    with open(model_path, "w") as f:
        f.write(f"trained on {n} samples\n")


@dsl.component(base_image="python:3.9-slim")
def evaluate(model_path: dsl.InputPath(str)):
    """Prints model info."""
    with open(model_path) as f:
        print(f.read())


@dsl.pipeline(
    name="end-to-end-train",
    description="Data prep → train → evaluate in KFP v2",
    pipeline_root="s3://my-bucket/kfp-pipelines",
)
def training_pipeline():
    prep = prep_data()
    train = train_model(data_path=prep.outputs["output_path"])
    evaluate(model_path=train.outputs["model_path"])


if __name__ == "__main__":
    compiler.Compiler().compile(training_pipeline, "training-pipeline.yaml")
    print("Compiled training-pipeline.yaml")

    client = kfp.Client(host="http://localhost:8080")
    run = client.create_run_from_pipeline_package(
        "training-pipeline.yaml",
        arguments={},
        experiment_name="end-to-end-test",
    )
    print(f"Run: {run.run_id}")