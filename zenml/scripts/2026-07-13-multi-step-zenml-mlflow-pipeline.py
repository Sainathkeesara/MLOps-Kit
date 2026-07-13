# last_verified: 2026-07-13 · zenml (version not specified in research)

"""zenml-010 — Multi-step ZenML pipeline with a custom materializer and MLflow logging.

I followed the quickstart primer and the first training snippet to build
something closer to a real workflow: ingest -> preprocess -> train -> evaluate,
with a custom materializer so ZenML knows how to persist a sklearn model
between steps, plus MLflow experiment tracking enabled.
"""

import os
from typing import Tuple

import mlflow
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from zenml import pipeline, step
from zenml.materializers.base_materializer import BaseMaterializer

# ---------------------------------------------------------------------------
# Custom materializer for sklearn models
# ---------------------------------------------------------------------------
# ZenML has built-in materializers for common types (DataFrame, ndarray, …)
# but not for a fitted sklearn estimator, so I wrote a minimal one that
# pickles the model into the artifact store. This is what I needed to pass
# the trained model from the train step to the evaluate step.
# ZenML auto-discovers materializers that match the step return type via
# ASSOCIATED_TYPES, so this class is picked up when train_model declares
# -> RandomForestClassifier.


class SklearnModelMaterializer(BaseMaterializer):
    ASSOCIATED_TYPES = (RandomForestClassifier,)

    def load(self, data_type):
        import joblib

        path = os.path.join(self.uri, "model.joblib")
        return joblib.load(path)

    def save(self, data):
        import joblib

        os.makedirs(self.uri, exist_ok=True)
        joblib.dump(data, os.path.join(self.uri, "model.joblib"))


# ---------------------------------------------------------------------------
# Pipeline steps
# ---------------------------------------------------------------------------


@step
def load_data() -> Tuple[np.ndarray, np.ndarray]:
    """Load the iris dataset and return features and labels."""
    X, y = load_iris(return_X_y=True)
    return X, y


@step
def preprocess_data(
    X: np.ndarray, y: np.ndarray
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Split into train/test and standardize features."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test


@step
def train_model(
    X_train: np.ndarray, y_train: np.ndarray
) -> RandomForestClassifier:
    """Train a RandomForest classifier and log params/metrics to MLflow."""
    with mlflow.start_run(run_name="zenml-train-step"):
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("model_type", "RandomForestClassifier")
        train_acc = model.score(X_train, y_train)
        mlflow.log_metric("train_accuracy", train_acc)
    return model


@step
def evaluate_model(
    model: RandomForestClassifier,
    X_test: np.ndarray,
    y_test: np.ndarray,
) -> float:
    """Evaluate the model on held-out data and log test accuracy to MLflow."""
    with mlflow.start_run(run_name="zenml-evaluate-step", nested=True):
        test_acc = model.score(X_test, y_test)
        mlflow.log_metric("test_accuracy", test_acc)
    return test_acc


# ---------------------------------------------------------------------------
# Pipeline definition
# ---------------------------------------------------------------------------


@pipeline
def training_pipeline():
    """End-to-end training pipeline: load -> preprocess -> train -> evaluate."""
    X, y = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(X, y)
    model = train_model(X_train, y_train)
    test_acc = evaluate_model(model, X_test, y_test)
    print(f"Test accuracy: {test_acc:.2f}")


if __name__ == "__main__":
    mlflow.set_tracking_uri("./mlruns")
    mlflow.set_experiment("zenml-multi-step-pipeline")
    training_pipeline()
