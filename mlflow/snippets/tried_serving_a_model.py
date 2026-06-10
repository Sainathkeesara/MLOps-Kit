"""mflow-007 — Minimal model serving with MLflow Python API.

Train a quick RandomForest on iris, log it with MLflow Tracking,
then load the model back right away and serve predictions both
from the run URI and from the Model Registry.

The key idea: MLflow saves the whole model object, so you can
load() + predict() anywhere — that's the "serving" part.
"""

import mlflow
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("minimal-serving-demo")

with mlflow.start_run() as run:
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    # Train a quick model
    clf = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)
    clf.fit(X_train, y_train)

    acc = clf.score(X_test, y_test)
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(clf, "model")
    print(f"Run {run.info.run_id} logged — accuracy {acc:.3f}")

    # Serve from the run artifact
    # mlflow.pyfunc.load_model() gives us a generic predict() interface
    model_artifact = mlflow.pyfunc.load_model(f"runs:/{run.info.run_id}/model")
    preds = model_artifact.predict(X_test)
    print(f"Served from run — first 5 predictions: {preds[:5]}")

    # Register the model so we can pull it by name later
    mlflow.register_model(f"runs:/{run.info.run_id}/model", "IrisRandomForest")

# Serve from the Model Registry (by name, not run ID)
registered = mlflow.pyfunc.load_model("models:/IrisRandomForest/latest")
preds2 = registered.predict(X_test)
print(f"Served from registry — match: {(preds2 == preds).all()}")
print("Done — model served via Python API in two ways.")
