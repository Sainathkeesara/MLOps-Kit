"""zenml-002 — My first ZenML pipeline with a training step.

Just getting a pipeline to run end-to-end. Used the decorator API
from the primer and added a real-ish training step.
"""

from zenml import pipeline, step
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris


@step
def load_data():
    X, y = load_iris(return_X_y=True)
    return X[:100], y[:100]  # smaller subset for speed


@step
def train_model(X, y) -> float:
    model = RandomForestClassifier()
    model.fit(X, y)
    return model.score(X, y)


@pipeline
def training_pipeline():
    X, y = load_data()
    acc = train_model(X, y)
    print(f"Training accuracy: {acc:.2f}")


if __name__ == "__main__":
    training_pipeline()
