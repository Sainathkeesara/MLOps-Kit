"""Minimal Kubeflow Pipelines V2 pipeline with two components.

Has a data-prep step and a training step. Passes data through typed
artifacts. The quickstart only showed one component — this is my attempt
at wiring two together.
"""

from kfp import dsl
from kfp import compiler


@dsl.component
def prep_data(message: str) -> str:
    """Takes a message and prepares it for the trainer."""
    prepared = f"prep: {message}"
    print(f"Prepared: {prepared}")
    return prepared


@dsl.component
def train_model(data: str, epochs: int) -> str:
    """Pretends to train a model on the prepared data."""
    result = f"trained for {epochs} epochs on '{data}'"
    print(f"Result: {result}")
    return result


@dsl.pipeline(
    name="two-step-pipeline",
    description="Prepares data then trains. V2 SDK style.",
)
def my_pipeline(message: str = "hello world", epochs: int = 3):
    prep_task = prep_data(message=message)
    train_task = train_model(
        data=prep_task.output,
        epochs=epochs,
    )


if __name__ == "__main__":
    compiler.Compiler().compile(my_pipeline, "two-step-pipeline.yaml")

    # Also submit a run so I don't have to use the UI every time.
    # The host URL depends on your Kubeflow deployment — port-forward
    # the ml-pipeline service to 8080.
    import kfp
    client = kfp.Client(host="http://localhost:8080")
    run = client.create_run_from_pipeline_func(
        my_pipeline,
        arguments={"message": "test", "epochs": 5},
        experiment_name="Snippet-test",
    )
    print(f"Run submitted: {run.run_id}")
