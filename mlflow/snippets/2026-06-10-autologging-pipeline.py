import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

TRACKING_URI = "http://127.0.0.1:5000"
EXPERIMENT_NAME = "autologging-pipeline"
MODEL_REGISTRY_NAME = "IrisBestModel"


def train_and_evaluate(model_class, model_name, params, X_train, X_test, y_train, y_test):
    mlflow.set_experiment(EXPERIMENT_NAME)

    with mlflow.start_run(run_name=model_name):
        mlflow.autolog()
        mlflow.log_params({"model": model_name})

        try:
            if params:
                model = model_class(**params)
            else:
                model = model_class()

            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            acc = accuracy_score(y_test, preds)
            mlflow.log_metric("accuracy", acc)

            result = mlflow.register_model(
                f"runs:/{mlflow.active_run().info.run_id}/model",
                MODEL_REGISTRY_NAME,
            )
            return {
                "name": model_name,
                "accuracy": acc,
                "version": result.version,
            }
        except Exception as exc:
            mlflow.log_param("error", str(exc))
            return {
                "name": model_name,
                "accuracy": None,
                "version": None,
                "error": str(exc),
            }


def main():
    mlflow.set_tracking_uri(TRACKING_URI)

    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    candidates = [
        (RandomForestClassifier, "random-forest", {"n_estimators": 100, "max_depth": 3}),
        (GradientBoostingClassifier, "gradient-boosting", {"n_estimators": 50, "max_depth": 2}),
        (LogisticRegression, "logistic-regression", {"max_iter": 200}),
    ]

    results = [
        train_and_evaluate(cls, name, params, X_train, X_test, y_train, y_test)
        for cls, name, params in candidates
    ]

    best = max((r for r in results if r["accuracy"] is not None), key=lambda r: r["accuracy"])

    client = mlflow.tracking.MlflowClient()
    client.transition_model_version_stage(
        name=MODEL_REGISTRY_NAME,
        version=best["version"],
        stage="Production",
        archive_existing_versions=True,
    )

    print(f"Best model: {best['name']} (v{best['version']}, accuracy={best['accuracy']:.3f})")


if __name__ == "__main__":
    main()
