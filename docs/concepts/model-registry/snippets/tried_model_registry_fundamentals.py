"""Practice: model registry fundamentals exercises (L2)

I wanted to understand the model registry workflow — train something,
register it, tag a version, and load it back. Using MLflow's registry
since it integrates with the tracker I already have.
"""

import mlflow
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=200, n_features=4, random_state=42)

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

with mlflow.start_run() as run:
    mlflow.sklearn.log_model(model, "model")
    run_id = run.info.run_id

# register the model so it gets its own version history
model_uri = f"runs:/{run_id}/model"
mlflow.register_model(model_uri, "practice-classifier")

# tag the first version as "staging" so I know it's not production-ready yet
client = mlflow.tracking.MlflowClient()
client.set_registered_model_alias("practice-classifier", "staging", version=1)

print("Registered 'practice-classifier' v1 with alias 'staging'.")
print("Next step: load it back with mlflow.sklearn.load_model() and test it.")
