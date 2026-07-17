---
last_verified: 2026-07-17
tool_version: 2.17.x
---

# MLflow autologging vs manual logging — when each approach fits

## Purpose

MLflow captures experiment metadata in two flavors: **autologging**, which hooks into a framework's training calls to record parameters, metrics, and artifacts automatically, and **manual logging**, where you make explicit `log_param`, `log_metric`, and `log_artifact` calls. This doc compares the two and gives guidance on when each fits a real ML project. It is written for the L3 stage, where you are comfortable running tracked experiments and are deciding how to structure logging across a codebase.

## When to use autologging

Autologging is the right default when you want broad, low-effort capture during early development and exploration:

- You are iterating on a single framework (scikit-learn, XGBoost, PyTorch, TensorFlow, and others have official flavors).
- You want parameters, train/validation metrics, and the fitted model captured without littering training code with logging calls.
- You accept the framework's default metric names and artifact set.

A minimal example that captures everything automatically:

```python
import mlflow
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

mlflow.sklearn.autolog(log_models=True, log_datasets=False, silent=True)

with mlflow.start_run(run_name="autolog-rf"):
    X, y = load_iris(return_X_y=True)
    model = RandomForestClassifier(n_estimators=100, max_depth=5)
    model.fit(X, y)
```

One call before `fit()` records the estimator's hyperparameters, the training score, and the serialized model artifact.

## When to use manual logging

Manual logging fits when you need control that autologging cannot give you:

- Custom metrics (business KPIs, fairness scores) that a framework has no hook for.
- Per-step or per-epoch logging inside a hand-written training loop, where the framework flavor does not capture intermediate values.
- Domain-specific artifacts such as plots, config files, or data dictionaries that the autolog hook will not produce.
- Projects spanning multiple libraries where relying on each flavor's autolog behavior would fragment the logged schema.

```python
import mlflow
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

with mlflow.start_run(run_name="manual-rf"):
    X, y = load_iris(return_X_y=True)
    model = RandomForestClassifier(n_estimators=100, max_depth=5)
    model.fit(X, y)

    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 5)
    preds = model.predict(X)
    mlflow.log_metric("f1", f1_score(y, preds, average="macro"))
    mlflow.sklearn.log_model(model, "model")
```

The extra lines buy you an explicit, predictable schema — the column names in the tracking store are exactly what you wrote.

## Side-by-side comparison

| Dimension | Autologging | Manual logging |
|-----------|-------------|----------------|
| Code overhead | One `autolog()` call before training | Explicit `log_*` calls per value |
| Parameter capture | All framework-detected params, automatically | Only what you choose to log |
| Metric capture | Defaults (e.g. `training_score`); names vary by flavor | Any name you define |
| Custom artifacts | Limited to the flavor's defaults | Any file via `log_artifact` |
| Control over schema | Low — you accept framework defaults | High — you own the schema |
| Best for | Exploratory runs, fast iteration | Production pipelines, custom metrics |

## Hybrid approach

The two are not mutually exclusive. A common pattern is to enable autologging for broad capture during development, then add targeted manual `log_metric` / `log_artifact` calls for the values that matter to your evaluation. Inside a single run, manual calls supplement rather than replace the autologged entries.

```python
import mlflow
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

mlflow.sklearn.autolog(log_models=True, silent=True)

with mlflow.start_run(run_name="hybrid-rf"):
    X, y = load_iris(return_X_y=True)
    model = RandomForestClassifier(n_estimators=100, max_depth=5).fit(X, y)
    # autolog already captured params/score/model; add the metric we care about
    mlflow.log_metric("f1_macro", f1_score(y, model.predict(X), average="macro"))
```

One caveat worth verifying before adopting the hybrid pattern at scale: autolog's metric naming can differ between library versions and estimator types, so a downstream job that reads `training_score` by key should be tested against the exact versions in your environment. Treat framework-default metric keys as a convenience, not a contract.

## Verify

After running either approach, confirm the capture landed:

```python
from mlflow import MlflowClient

client = MlflowClient()
run = client.get_run(client.search_runs(experiment_ids=["0"])[0].info.run_id)
print(sorted(run.data.params.keys()))
print(sorted(run.data.metrics.keys()))
print(sorted(a.path for a in client.list_artifacts(run.info.run_id)))
```

If the keys you expect are missing, check that `autolog()` was called before the framework import (for autologging) or that the `log_*` call ran inside an active run (for manual logging).
