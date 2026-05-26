import mlflow
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("autolog-demo")

with mlflow.start_run() as run:
    mlflow.sklearn.autolog()

    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    clf = RandomForestClassifier(n_estimators=100, max_depth=3)
    clf.fit(X_train, y_train)

    acc = clf.score(X_test, y_test)
    print(f"Test accuracy: {acc:.3f}")

    mlflow.register_model(
        f"runs:/{run.info.run_id}/model",
        "IrisRandomForest"
    )
