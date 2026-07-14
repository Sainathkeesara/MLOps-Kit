# last_verified: 2026-07-14 · mlflow 3.14.0

"""mlf-011 — MLflow tracking quickstart: log params, metrics, and a model artifact.

Following the official MLflow Tracking quickstart to get a feel for the
core API surface before wiring it into a real project.
"""

import mlflow
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Started a local Tracking server with `mlflow server --host 127.0.0.1 --port 5000`
# in another terminal. Without a server, runs just go to a local ./mlruns directory.
mlflow.set_tracking_uri("http://127.0.0.1:5000")

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

with mlflow.start_run(run_name="quickstart-example") as run:
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 4)
    mlflow.log_param("random_state", 42)

    model = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", accuracy)

    # log_model saves the model artifact so I can load it later for serving
    mlflow.sklearn.log_model(model, "model")

    print(f"Run ID: {run.info.run_id}")
    print(f"Accuracy: {accuracy:.3f}")
    print("Open http://127.0.0.1:5000 to see the run in the UI.")
