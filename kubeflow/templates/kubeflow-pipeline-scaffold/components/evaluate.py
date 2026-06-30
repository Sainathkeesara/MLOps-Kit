"""KFP component that evaluates predictions and logs to MLflow."""

from kfp import dsl
from kfp.dsl import Input, Dataset


@dsl.component(
    base_image="python:3.11-slim",
    packages_to_install=["mlflow", "scikit-learn", "numpy"],
)
def evaluate_component(
    mlflow_tracking_uri: str,
    experiment_name: str,
    predictions_path: Input[Dataset],
):
    """Evaluate predictions and log metrics to MLflow.

    Args:
        mlflow_tracking_uri: URL of MLflow tracking server.
        experiment_name: Name of the MLflow experiment.
        predictions_path: Input path containing model predictions.
    """
    import mlflow
    import numpy as np
    from sklearn.datasets import load_diabetes
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, mean_absolute_error

    mlflow.set_tracking_uri(mlflow_tracking_uri)
    mlflow.set_experiment(experiment_name)

    data = load_diabetes()
    _, X_test, _, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )

    predictions = np.load(predictions_path.path)

    with mlflow.start_run():
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        mae = mean_absolute_error(y_test, predictions)

        mlflow.log_metric("eval_rmse", rmse)
        mlflow.log_metric("eval_mae", mae)

        print(f"Evaluation complete — RMSE: {rmse:.4f}, MAE: {mae:.4f}")