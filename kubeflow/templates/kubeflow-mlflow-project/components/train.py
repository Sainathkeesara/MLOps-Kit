"""KFP component that trains a model and logs parameters/metrics to MLflow."""

from kfp import dsl
from kfp.dsl import Input, Output, Dataset


@dsl.component(
    base_image="python:3.11-slim",
    packages_to_install=["mlflow", "scikit-learn", "pandas", "numpy"],
)
def train_component(
    mlflow_tracking_uri: str,
    experiment_name: str,
    alpha: float,
    l1_ratio: float,
    model_path: Output[Dataset],
):
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

        y_pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)

        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.sklearn.log_model(model, "model")

        with open(model_path.path, "w") as f:
            np.save(f, y_pred)

        print(f"Training complete — RMSE: {rmse:.4f}, MAE: {mae:.4f}")
