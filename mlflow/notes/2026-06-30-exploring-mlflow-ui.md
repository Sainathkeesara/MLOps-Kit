# Exploring the MLflow UI — what's there

Started `mlflow ui` in my project dir — it spins up on `http://localhost:5000`.

## Home / Experiments page

Shows a list of experiments I've created. I saw `first-experiment` from my earlier snippet. Clicking into it shows a table of runs with params and metrics columns. I can sort columns and pick which metrics to display. The star/filter buttons let me narrow down runs.

## Run detail page

Clicking a run ID opens a page with tabs:

- **Parameters** — key-value pairs I logged (learning_rate, batch_size).
- **Metrics** — logged metric values with a mini plot. The plot updates as I add steps.
- **Artifacts** — shows uploaded files. I haven't logged any artifacts yet, so it was empty.
- **Source** — path to the script that generated the run. Helpful when I forget what I ran.

## Compare mode

Selected two runs and hit "Compare" — it showed them side by side in a table. There's also a scatter plot view for comparing metrics visually. Took me a second to find the "Add runs" button in the top-right.

## What tripped me up

1. The UI didn't show my new runs until I hit refresh — no auto-polling.
2. The default artifact location is `mlruns/` in the current directory, which I initially ran in the wrong folder.
3. Running `mlflow ui` from a different directory than the one I logged runs from means they won't show up.

## What I'd try next

Wire the tracking server to a SQLite backend so runs persist across restarts, and try uploading a model file as an artifact to see the download link work.
