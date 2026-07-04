---
last_verified: 2026-07-04
tool_version: 2.17.x
---

# mflow-026 — Following the official MLflow quickstart (July 2026): what tripped me up

I revisited the MLflow quickstart today — the one at `mlflow.org/docs/latest/getting-started/intro-quickstart/index.html`. I'd gone through this before in May but wanted to rerun it fresh to see what changed and what still catches me.

## Steps I followed

1. **Installed MLflow** — `pip install mlflow` in a fresh venv. Landed on 2.17.x. No issues.
2. **Ran the quickstart script** — the one that trains a `LinearRegression` on California housing and logs params, metrics, and the model with autolog. Saved it as `quickstart_train.py`.
3. **Viewed results in the UI** — `mlflow ui` then opened `http://localhost:5000`.
4. **Loaded the model as a PyFunc** — the quickstart shows you how to reload and score the model from the saved artifact.

## Where I got stuck

**Stuck 1: The quickstart example uses `mlflow.autolog()` without the sklearn prefix.** The snippet in the docs just says `mlflow.autolog()`. This works — but it's ambiguous about *which* flavor is being used. I assumed sklearn was auto-detected, but later when I tried `mlflow.sklearn.autolog(log_models=False)` I realised the two APIs behave slightly differently. The quickstart doesn't explain that `mlflow.autolog()` is a unified wrapper and you can still call flavor-specific versions for fine control.

```python
# Quickstart way — works, but hides which flavors are active
mlflow.autolog()

# More explicit — lets you pass flavor-specific kwargs
mlflow.sklearn.autolog(log_models=False)  # skip saving the model artifact
```

**Stuck 2: The UI showed NaN for some metrics on the first run.** The quickstart uses `mean_squared_error` from sklearn, which returns a float. But I had a typo in my script where I was logging `mlflow.log_metric("mse", "not_a_number")` accidentally (leftover from debugging). The UI displayed "NaN" with no error — took me a while to spot the string value in the runs table. MLflow doesn't validate metric types at log time.

**Stuck 3: `mlflow models serve` needed the artifact URI format, not the run name.** After training, I tried `mlflow models serve -m "models:/LinearRegression/1"` but I hadn't registered the model. The quickstart loads the model by run ID: `mlflow.pyfunc.load_model(f"runs:/{run_id}/model")`. For serving you need the artifact store path explicitly, which the quickstart doesn't cover. I ended up using `mlflow models serve -m runs:/<run-id>/model` — which worked but is not portable.

## What I'd try next

- Wire autolog into a proper training loop with hyperparameter sweeps.
- Set up a shared tracking server with PostgreSQL so I don't lose runs.
- Play with the Model Registry API — transitioning stages from Staging to Production programmatically.
