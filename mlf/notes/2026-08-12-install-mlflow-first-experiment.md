---
last_verified: 2026-08-12
tool_version: n/a
sources: []
---

# Installing MLflow and logging my first experiment

Installed MLflow today with `pip install mlflow`. It came down clean — no native deps, no server to start for a first run.

My first experiment was a 6-line script: create an experiment, open a run, log one param and one metric, done.

```python
import mlflow

mlflow.set_experiment("my-first-experiment")

with mlflow.start_run(run_name="install-test"):
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.94)
```

Ran it — nothing printed, which threw me at first. I had to trust it worked. So I started the UI with `mlflow ui` and opened the browser. There was the run, under `my-first-experiment`, with `learning_rate` and `accuracy` right there. That's when it clicked: the tracking is silent by default; you look at the UI (or the client API) to see what you logged.

## What I noticed

- Logging goes into a local `mlruns/` folder by default — no database, no setup.
- The experiment name groups runs; you can filter by it in the UI.
- A `with mlflow.start_run()` block handles open/close for you.

Next I want to log a model artifact and compare a couple of runs side by side, since comparing runs is the whole point of tracking.

Noted a small gotcha: if I forgot the `with` block and called `mlflow.log_metric` outside a run, it silently did nothing. Keep everything inside the run context.
