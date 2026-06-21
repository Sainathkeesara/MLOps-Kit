"""KFP component that evaluates a model and logs metrics to MLflow."""

from kfp import dsl
from kfp.dsl import Input, Dataset


@dsl.component(
    base_image="python:3.11-slim",
    packages_to_install=["mlflow", "scikit-learn", "numpy"],
)
def evaluate_component(
    mlflow_tracking_uri: str,
    experiment_name: str,
    model_path: Input[Dataset],
):
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

    with mlflow.start_run():
        y_pred = np.load(model_path.path)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)

        mlflow.log_metric("eval_rmse", rmse)
        mlflow.log_metric("eval_mae", mae)

        print(f"Evaluation complete — RMSE: {rmse:.4f}, MAE: {mae:.4f}")
