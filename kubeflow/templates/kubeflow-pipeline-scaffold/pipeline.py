"""Kubeflow Pipelines v2 scaffold — train/evaluate pipeline with CI/CD integration."""

from kfp import dsl
from kfp import compiler

from components.train import train_component
from components.evaluate import evaluate_component


@dsl.pipeline(
    name="kubeflow-pipeline-scaffold",
    description="Train and evaluate a model with extracted testable components and CI/CD integration.",
)
def pipeline(
    mlflow_tracking_uri: str = "http://mlflow-server:5000",
    experiment_name: str = "kubeflow-pipeline-scaffold",
    alpha: float = 0.5,
    l1_ratio: float = 0.1,
):
    train_task = train_component(
        mlflow_tracking_uri=mlflow_tracking_uri,
        experiment_name=experiment_name,
        alpha=alpha,
        l1_ratio=l1_ratio,
    )

    evaluate_task = evaluate_component(
        mlflow_tracking_uri=mlflow_tracking_uri,
        experiment_name=experiment_name,
        predictions_path=train_task.output,
    )

    # Configure resources for training task
    train_task.set_cpu_limit("2")
    train_task.set_memory_limit("4Gi")
    train_task.set_cpu_request("1")
    train_task.set_memory_request("2Gi")


if __name__ == "__main__":
    compiler.Compiler().compile(
        pipeline_func=pipeline,
        package_path="pipeline.yaml",
    )
    print("Pipeline compiled to pipeline.yaml")