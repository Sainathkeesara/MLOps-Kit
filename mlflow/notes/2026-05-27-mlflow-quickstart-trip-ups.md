# mlf-004 — Following the MLflow quickstart: what tripped me up

I worked through the official MLflow quickstart today (`mlflow.org/docs/latest/quickstart`). The goal was to log a training run, view it in the UI, and register a model. Here's what happened.

## Steps I followed

1. **Started the Tracking Server** — `mlflow ui` in a terminal. Opened `http://localhost:5000`. Empty experiments page — expected.
2. **Wrote a training script** based on the quickstart's example — trains a `LinearRegression` on California housing data, logs params and metrics.
3. **Ran the script** — `python train.py`. It completed without errors.
4. **Checked the UI** — my run showed up under the default experiment. Params, metrics, and the model artifact were all there.
5. **Registered the model** via the UI — clicked the run, went to Artifacts, clicked the model folder, hit Register Model.

## Where I got stuck

**Stuck 1: Autologging didn't pick up sklearn initially.** I called `mlflow.sklearn.autolog()` but my import was `from sklearn.ensemble import RandomForestRegressor`. That worked after restarting the kernel — but the quickstart doesn't mention that autolog hooks need to be set before importing the library. I wasted 10 minutes rerunning the same script thinking I'd broken something.

```python
# Correct order — autolog BEFORE sklearn imports
import mlflow
mlflow.sklearn.autolog()

from sklearn.ensemble import RandomForestRegressor  # now hooks attach
```

**Stuck 2: The UI didn't refresh automatically.** After my first run, I kept refreshing the browser and seeing 0 runs. Turns out my script logged to a different `MLFLOW_TRACKING_URI` than the UI was using. I'd started the UI from one terminal and run the script from another that had a stale environment variable set. Fix: unset `MLFLOW_TRACKING_URI` in the script terminal or explicitly pass `mlflow.set_tracking_uri("http://localhost:5000")`.

**Stuck 3: Model registration failed with "already exists".** The UI lets you create a new registered model with the same name as an existing one — but only if you use a different version. The error message just said "name already exists" with no hint about versioning. I had to delete the model and re-register.

## What I'd try next

- Run the full MLflow Projects example (`mlflow run .`) with a conda environment.
- Set up a SQLite-backed server for persistence across restarts.
- Try the Model Registry API to programmatically transition a model from Staging to Production.
