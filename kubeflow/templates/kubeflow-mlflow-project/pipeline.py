"""KFP pipeline that wires MLflow tracking into training and evaluation steps."""

from kfp import dsl
from kfp import compiler

from components.train import train_component
from components.evaluate import evaluate_component


@dsl.pipeline(
    name="mlflow-integration-pipeline",
    description="Train and evaluate a model while logging to MLflow.",
)
def mlflow_pipeline(
    mlflow_tracking_uri: str = "http://localhost:5000",
    experiment_name: str = "kubeflow-pipeline-demo",
    alpha: float = 0.5,
    l1_ratio: float = 0.1,
):
    train_task = train_component(
        mlflow_tracking_uri=mlflow_tracking_uri,
        experiment_name=experiment_name,
        alpha=alpha,
        l1_ratio=l1_ratio,
    )

    evaluate_component(
        mlflow_tracking_uri=mlflow_tracking_uri,
        experiment_name=experiment_name,
        model_path=train_task.output,
    )


if __name__ == "__main__":
    compiler.Compiler().compile(
        pipeline_func=mlflow_pipeline,
        package_path="pipeline.yaml",
    )
    print("Pipeline compiled to pipeline.yaml")
