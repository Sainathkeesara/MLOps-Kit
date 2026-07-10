# last_verified: 2026-07-10 · mlflow 3.7.0

"""con-015 — Apply model registry to version and promote ML models (L2)

I followed the model-registry workflow: train a tiny classifier,
register it, tag it stage-by-stage, and load it back by alias.
MLflow is the registry I'm practicing with because it's already in the kit.
"""

import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# small synthetic dataset so this runs standalone; no external data files needed
# reused the same make_classification call from the existing registry snippet
X, y = make_classification(n_samples=200, n_features=4, random_state=42)

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

with mlflow.start_run(run_name="registry-demo") as run:
    # log_model stores the artifact in the run;
    # register_model gives it a name + version in the registry
    mlflow.sklearn.log_model(model, artifact_path="model")
    run_id = run.info.run_id
    print(f"Logged run {run_id}")

# register the model so it gets its own version history
model_uri = f"runs:/{run_id}/model"
mlflow.register_model(model_uri, "registry-demo-clf")

# use the client directly — this is what CI promotion scripts would call
client = mlflow.tracking.MlflowClient()

# tag the freshly registered version as "staging"
client.set_registered_model_alias("registry-demo-clf", "staging", version=1)
print("registry-demo-clf v1 -> alias 'staging'")

# promote to "production" once validation gates pass
client.set_registered_model_alias("registry-demo-clf", "production", version=1)
print("registry-demo-clf v1 -> alias 'production'")

# serving jobs typically load by alias so they don't hardcode a version
loaded = mlflow.sklearn.load_model("models:/registry-demo-clf@production")
print(
    f"Loaded model from production alias, "
    f"predictions: {loaded.predict(X[:3]).tolist()}"
)
