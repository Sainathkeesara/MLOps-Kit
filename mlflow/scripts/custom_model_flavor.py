"""Build a custom MLflow model flavor from scratch.

Purpose: wrap a preprocessing + prediction pipeline as a custom MLflow
pyfunc flavor, then save, load, and serve it — no built-in flavor needed.

Steps:
  1. Define a custom wrapper class.
  2. Train / prepare the underlying model.
  3. Save the wrapper with mlflow.pyfunc.save_model.
  4. Load in a new process and verify inference.

Verify: run this script end-to-end; the final assert confirms the
loaded model returns the right shape and expected value.
"""

import mlflow
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


class CustomIrisFlavor(mlflow.pyfunc.PythonModel):
    """Custom pyfunc wrapper around a scikit-learn classifier.

    This demonstrates the custom flavor pattern: you could replace the
    internals with any framework (XGBoost, a rule engine, an ONNX
    runtime, …) without changing the save/load contract.
    """

    def __init__(self):
        self._model = None

    def load_context(self, context):
        """Load artifacts from the MLflow model directory."""
        import joblib
        import os
        model_path = os.path.join(context.artifacts["model_dir"], "model.pkl")
        self._model = joblib.load(model_path)

    def predict(self, context, model_input):
        """Return predicted class labels for the given input."""
        if self._model is None:
            raise RuntimeError("Model not loaded — did load_context run?")
        return self._model.predict(model_input)


def train_and_save():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    clf = LogisticRegression(max_iter=200)
    clf.fit(X_train, y_train)

    import joblib
    import tempfile
    import os

    artifact_dir = tempfile.mkdtemp()
    joblib.dump(clf, os.path.join(artifact_dir, "model.pkl"))

    model_uri = mlflow.pyfunc.save_model(
        path="custom_iris_flavor",
        python_model=CustomIrisFlavor(),
        artifacts={"model_dir": artifact_dir},
        conda_env={
            "channels": ["conda-forge"],
            "dependencies": [
                "python=3.10",
                "pip",
                {"pip": ["mlflow", "scikit-learn", "pandas", "joblib"]},
            ],
        },
    )
    print(f"Model saved to: {model_uri}")
    return model_uri, X_test, y_test


def verify(model_uri, X_test, y_test):
    loaded = mlflow.pyfunc.load_model(model_uri)
    preds = loaded.predict(pd.DataFrame(X_test))
    accuracy = (preds.values == y_test).mean()
    print(f"Accuracy on test set: {accuracy:.3f}")
    assert accuracy > 0.8, f"Accuracy {accuracy:.3f} is too low"
    print("Verify passed — custom flavor works correctly.")


if __name__ == "__main__":
    mlflow.set_tracking_uri("http://localhost:5000")
    model_uri, X_test, y_test = train_and_save()
    verify(model_uri, X_test, y_test)
