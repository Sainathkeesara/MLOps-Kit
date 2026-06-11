"""mflow-007 — Minimal model serving with MLflow Python API.

Following the MLflow quickstart to load a registered model and serve
predictions locally. The pyfunc interface is the generic way to get
model predictions without framework-specific knowledge.
"""

import mlflow
import pandas as pd
from sklearn.datasets import load_iris

# Point at the local tracking server — needed because serving from
# registry requires a backend to fetch the model artifacts
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Tried loading with models:/IrisRandomForest/Production first, but that
# only works after registering a model. Using runs:/ URI as fallback
# because it works even without the model registry set up.
model_uri = "runs:/<run-id>/model"

loaded = mlflow.pyfunc.load_model(model_uri)

# Test with iris data — using first 3 samples to verify prediction shape
X, _ = load_iris(return_X_y=True)
sample = pd.DataFrame(X[:3])

# pyfunc.predict returns a pandas Series or DataFrame, not numpy array
predictions = loaded.predict(sample)
print(f"Predictions: {predictions.tolist()}")