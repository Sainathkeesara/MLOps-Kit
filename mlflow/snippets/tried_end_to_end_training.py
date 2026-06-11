"""mflow-008 — End-to-end training pipeline with MLflow autologging.

Purpose: Demonstrate a complete MLflow training workflow with automatic parameter
and metric capture via sklearn.autolog(), plus model registration to the Model
Registry for downstream serving.

When to use: When you want to quickly prototype a model and capture all relevant
metadata without writing explicit logging calls.

Prerequisites: MLflow installed, sqlite backend available or local mlruns folder.
"""

import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Configuration — adjust for your setup
TRACKING_URI = "sqlite:///mlflow.db"
EXPERIMENT_NAME = "iris-classifier-pipeline"
REGISTERED_MODEL_NAME = "IrisClassifier"

def main():
    # Set up tracking — using local backend store
    mlflow.set_tracking_uri(TRACKING_URI)
    
    # Get or create experiment
    experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
    if experiment is None:
        experiment_id = mlflow.create_experiment(EXPERIMENT_NAME)
        experiment = mlflow.get_experiment(experiment_id)
    
    print(f"Experiment: {experiment.name} (ID: {experiment.experiment_id})")
    
    # Enable autologging before training
    # log_models=True: saves the sklearn model automatically
    # log_datasets=True: logs input data metadata (MLflow 2.4+)
    mlflow.sklearn.autolog(log_models=True, log_datasets=True)
    
    # Load data
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train — autolog captures params, metrics, and model automatically
    with mlflow.start_run(run_name="autolog-training-run") as run:
        clf = RandomForestClassifier(
            n_estimators=100,
            max_depth=4,
            min_samples_split=2,
            random_state=42
        )
        clf.fit(X_train, y_train)
        
        # Evaluate manually for custom metric logging
        acc = accuracy_score(y_test, clf.predict(X_test))
        mlflow.log_metric("test_accuracy", acc)
        
        run_id = run.info.run_id
        print(f"Run completed: {run_id[:8]}")
        print(f"Test accuracy: {acc:.3f}")
    
    # Register the autologged model to the Model Registry
    try:
        registered = mlflow.register_model(
            f"runs:/{run_id}/model",
            REGISTERED_MODEL_NAME
        )
        print(f"Model registered as '{REGISTERED_MODEL_NAME}'")
        print(f"Version: {registered.version}")
    except Exception as e:
        print(f"Registration skipped or failed: {e}")

if __name__ == "__main__":
    main()