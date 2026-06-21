"""
Hyperparameter sweep configuration for W&B.

Defines a sweep that explores n_estimators and max_depth to maximize F1 score.
Used by the W&B agent for distributed hyperparameter optimization.
"""

import wandb
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split


def train():
    with wandb.init() as run:
        config = run.config

        X, y = load_breast_cancer(return_X_y=True)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = RandomForestClassifier(
            n_estimators=config.n_estimators,
            max_depth=config.max_depth,
            random_state=42,
        )
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        accuracy = accuracy_score(y_test, preds)
        f1 = f1_score(y_test, preds)

        wandb.log({"accuracy": accuracy, "f1": f1})


if __name__ == "__main__":
    train()