# MLflow install and first tracking run

Installed MLflow today with `pip install mlflow`. Took about a minute. No hiccups.

Ran `mlflow --version` to confirm — got `mlflow, version 2.18.0`. Good.

## First experiment

Pulled up the quickstart. Created a tiny script that does a dummy training loop — just random data and a fake loss that shrinks each epoch.

```python
import mlflow

mlflow.set_experiment("first-contact")

with mlflow.start_run():
    for epoch in range(5):
        loss = 1.0 / (epoch + 1)
        mlflow.log_metric("loss", loss, step=epoch)
```

Ran it. No errors. Launched the UI with `mlflow ui` and saw my run in the browser at `http://localhost:5000`. The experiment name showed up, the loss metric plotted across the 5 steps. Pretty neat — I could see the curve dropping right away.

## What I noticed

The UI is simple — runs table on the left, detail pane on the right. It felt familiar if you've used any dashboard before. No auth, no setup beyond `pip install`. The artifact store defaults to `./mlruns` in the current dir.

Stopped the UI with Ctrl-C. The data is still in `mlruns/` — I can start the UI again later from the same folder.
