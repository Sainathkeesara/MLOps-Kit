"""
Training script with W&B experiment tracking.

Logs parameters, metrics, and model artifacts to W&B. Designed for CI/CD
integration where runs are triggered automatically by the pipeline.
"""

import argparse
import pickle

import wandb
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split


def main():
    parser = argparse.ArgumentParser(description="Train a model with W&B tracking")
    parser.add_argument("--n-estimators", type=int, default=100)
    parser.add_argument("--max-depth", type=int, default=None)
    parser.add_argument("--project", default="wandb-cicd-demo")
    parser.add_argument("--entity", default=None)
    args = parser.parse_args()

    X, y = load_breast_cancer(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    run = wandb.init(project=args.project, entity=args.entity, job_type="train")
    run.config.update({
        "n_estimators": args.n_estimators,
        "max_depth": args.max_depth,
    })

    model = RandomForestClassifier(
        n_estimators=args.n_estimators,
        max_depth=args.max_depth,
        random_state=42,
    )
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    accuracy = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds)

    wandb.log({"accuracy": accuracy, "f1": f1})

    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    artifact = wandb.Artifact(
        name=f"rf-model-run-{run.id[:8]}",
        type="model",
        description="RandomForest classifier trained on breast cancer dataset"
    )
    artifact.add_file("model.pkl")
    run.log_artifact(artifact)

    print(f"Accuracy: {accuracy:.4f}, F1: {f1:.4f}")
    wandb.finish()


if __name__ == "__main__":
    main()