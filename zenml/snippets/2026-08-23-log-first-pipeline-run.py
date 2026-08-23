# last_verified: 2026-08-23 · zenml n/a

"""zenml-013 — Log my first ZenML pipeline run with the Python SDK.

Just trying to get a pipeline to run and see what ZenML logs automatically.
The pipeline decorator is the main entry point — decorate a function and
call it, and ZenML handles the rest.
"""

from zenml import pipeline, step
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


@step
def load_data():
    X, y = load_iris(return_X_y=True)
    return X[:100], y[:100]


@step
def train_model(X, y) -> float:
    model = RandomForestClassifier()
    model.fit(X, y)
    return model.score(X, y)


@pipeline
def first_pipeline():
    X, y = load_data()
    acc = train_model(X, y)
    print(f"Training accuracy: {acc:.2f}")


if __name__ == "__main__":
    first_pipeline()
