# mlf-002 — Install MLflow and run the Tracking server

I decided to try MLflow today and start with getting the Tracking UI running locally.

**what I did**

1. Installed MLflow with pip:
   `pip install mlflow`

2. Started the Tracking UI:
   `mlflow ui`
   This popped up a server at `http://localhost:5000`. Neat — the default port is 5000.

3. I confirmed the UI loaded by hitting the URL in my browser. The home page showed zero experiments at first, which makes sense because I haven't logged anything yet.

**sidenotes**

- `mlflow ui` is a shorthand for `mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns`.
- If I want to share MLflow data across team members CI, I can point the backend to a shared SQL database instead of a SQLite file.
- The artifacts (model files, plots, etc.) live under a `./mlruns` folder by default on disk.

**next thing I'll try**

Log a run through Python so the UI shows up something.
