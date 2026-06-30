"""KFP component that trains a model and logs to MLflow."""

from kfp import dsl
from kfp.dsl import Output, Dataset


@dsl.component(
    base_image="python:3.11-slim",
    packages_to_install=["mlflow", "scikit-learn", "pandas", "numpy"],
)
def train_component(
    mlflow_tracking_uri: str,
    experiment_name: str,
    alpha: float,
    l1_ratio: float,
    predictions_path: Output[Dataset],
):
    """Train ElasticNet model and log to MLflow.

    Args:
        mlflow_tracking_uri: URL of MLflow tracking server.
        experiment_name: Name of the MLflow experiment.
        alpha: ElasticNet regularization strength.
        l1_ratio: ElasticNet mixing parameter.
        predictions_path: Output path for predictions.
    """
    import mlflow
    import numpy as np
    from sklearn.linear_model import ElasticNet
    from sklearn.datasets import load_diabetes
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, mean_absolute_error

    mlflow.set_tracking_uri(mlflow_tracking_uri)
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run():
        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)

        data = load_diabetes()
        X_train, X_test, y_train, y_test = train_test_split(
            data.data, data.target, test_size=0.2, random_state=42
        )

        model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        mae = mean_absolute_error(y_test, predictions)

        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.sklearn.log_model(model, "model")

        np.save(predictions_path.path, predictions)

        print(f"Training complete — RMSE: {rmse:.4f}, MAE: {mae:.4f}")