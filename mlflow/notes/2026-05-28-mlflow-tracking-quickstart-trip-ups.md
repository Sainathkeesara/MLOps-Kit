# mflow-004 — MLflow Tracking quickstart: what tripped me up

I ran through the official MLflow Tracking quickstart today — the one at `mlflow.org/docs/latest/tracking/quickstart.html`. The general quickstart covered logging and the UI, but this one goes deeper into the Tracking API itself: runs, params, metrics, tags, and artifacts. I wanted to understand the tracking surface before I start wiring it into real training jobs.

## Steps I followed

1. **Installed MLflow** — already had it from the earlier setup, but confirmed with `mlflow --version` (2.14.x).
2. **Started the Tracking Server** with SQLite backend: `mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0`. This is more persistent than the ephemeral `mlflow ui`.
3. **Wrote a standalone script** using `mlflow.start_run()` to log params, metrics, and a tag.
4. **Queried runs via the API** — used `MlflowClient()` to search runs and fetch run data programmatically.
5. **Logged an artifact** — saved a simple plot as a PNG and logged it with `mlflow.log_artifact()`.

## Where I got stuck

**Stuck 1: The `start_run` context manager vs manual start/stop.** The quickstart uses `with mlflow.start_run():` — which is clean. But when I tried an explicit `mlflow.start_run()` + `mlflow.end_run()` in a loop, runs got nested. Turns out MLflow nests run contexts by default unless you set `nested=True`. The error message just said "Run already active" — took me a few reads to figure out it was a context nesting issue.

```python
# This nests — not what I wanted
mlflow.start_run()
mlflow.log_param("x", 1)
mlflow.start_run()  # nested without explicit request
mlflow.log_param("y", 2)
mlflow.end_run()
mlflow.end_run()
```

**Stuck 2: SQLite path resolution.** I started the server from `~/mlflow-test/` and ran the client script from `~/mlflow-test/experiments/`. The server couldn't find the database because the script connected to `sqlite:///mlflow.db` which resolved relative to the script's CWD, not the server's. Fix: always use absolute paths for the SQLite URI.

**Stuck 3: `log_artifact` vs `log_figure`.** I tried to log a matplotlib figure with `log_artifact("plot.png")` — which worked, but the UI showed it as a raw download. The quickstart later mentions `mlflow.log_figure(fig, "plot.png")` which renders inline in the UI. Subtle but much nicer for reviewing runs.

**Stuck 4: Fetching runs with `search_runs` returned nothing at first.** I had `experiment_ids=["0"]` but my runs were in experiment "1" (created by the UI when I clicked "New Experiment"). The default is experiment 0 only — I had to pass `experiment_ids=None` to search all experiments.

## What I'd try next

- Wire the Tracking API into a real training loop with parameter sweeps.
- Try the autologging side of the Tracking API with `mlflow.sklearn.autolog()` and see how much it captures automatically.
- Set up the Model Registry API to transition a model through registry stages.
