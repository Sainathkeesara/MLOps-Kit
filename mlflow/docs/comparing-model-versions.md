# Comparing registered model versions with MLflow Model Registry

## Purpose

The MLflow Model Registry lets you register trained models, tag them with a version number, move them through lifecycle stages (Staging → Production → Archived), and compare versions side by side. This doc covers registering multiple versions of the same model, comparing their metrics and parameters through the API, and promoting one to Production.

## Prerequisites

- MLflow Tracking Server running (`mlflow ui` or a remote server)
- Two or more trained runs with different hyperparameters logged
- `mlflow` Python package installed

## Steps

### 1. Register a model from a run

After training a model with `mlflow.sklearn.autolog()` (or manual logging), you have a run ID. Register the model:

```python
import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")

run_id = "abc123..."  # from an earlier training run

result = mlflow.register_model(
    model_uri=f"runs:/{run_id}/model",
    name="IrisRandomForest"
)
```

The first registration creates version 1. A second registration with the same name creates version 2.

### 2. Register additional versions

If you train with different hyperparameters, register the new run under the same model name:

```python
# second training run — different n_estimators
with mlflow.start_run():
    mlflow.sklearn.autolog()
    clf = RandomForestClassifier(n_estimators=200, max_depth=5)
    clf.fit(X_train, y_train)
    acc = clf.score(X_test, y_test)
    run_id_2 = mlflow.active_run().info.run_id

mlflow.register_model(
    model_uri=f"runs:/{run_id_2}/model",
    name="IrisRandomForest"
)
```

This creates version 2 under `IrisRandomForest`.

### 3. Compare versions programmatically

Fetch all registered versions and compare their run metrics:

```python
from mlflow.tracking import MlflowClient

client = MlflowClient()

for v in client.search_model_versions("name='IrisRandomForest'"):
    run = client.get_run(v.run_id)
    params = run.data.params
    metrics = run.data.metrics
    print(f"Version {v.version} — stage={v.current_stage}")
    print(f"  params: n_estimators={params.get('n_estimators')}, max_depth={params.get('max_depth')}")
    print(f"  metrics: accuracy={metrics.get('accuracy')}")
```

If a model was registered without autologging, the params and metrics dicts may be empty — that's expected if the run didn't log them under the registered model's run.

### 4. Transition a version to Production

Once you pick the best version (higher accuracy, lower latency, etc.), move it to Production:

```python
client.transition_model_version_stage(
    name="IrisRandomForest",
    version=2,
    stage="Production"
)
```

The older version stays in None (or Staging) — it won't be served unless explicitly requested.

### 5. Compare versions in the UI

Open `http://127.0.0.1:5000` and click the model name in the Models tab. The UI shows each version, its current stage, who registered it, and when. Click a version to see the source run details.

The UI also colors the stage badges (None = gray, Staging = yellow, Production = green, Archived = red), which makes it quick to spot which version is active.

## Verify

```python
client = MlflowClient()
versions = client.search_model_versions("name='IrisRandomForest'")
assert len(versions) >= 2, "Expected at least two registered versions"
prod = [v for v in versions if v.current_stage == "Production"]
assert len(prod) == 1, "Expected exactly one version in Production"
print(f"Version {prod[0].version} is in Production — confirmed")
```

## Common errors

- **`ALREADY_EXISTS`** when registering — the model name already has a version in a non-Archived stage. This is fine; MLflow auto-increments the version number.
- **Run not found** — the run ID used in `model_uri` doesn't exist or belongs to a different tracking server. Double-check the tracking URI matches where the run was logged.
- **Stage transition fails** — transitioning from Production back to Staging requires `archive_existing_versions=True` if you want to move a different version into Production.

## References

- [MLflow Model Registry docs](https://mlflow.org/docs/latest/model-registry.html)
- [MlflowClient API reference](https://mlflow.org/docs/latest/python_api/mlflow.client.html)
