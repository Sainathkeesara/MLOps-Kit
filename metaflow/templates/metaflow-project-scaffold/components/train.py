"""Model training logic extracted from the Metaflow flow for testability."""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def train_random_forest(X_train, y_train, n_estimators=100, random_state=42):
    """Train a RandomForest classifier and return (model, train_accuracy)."""
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state,
    )
    model.fit(X_train, y_train)
    train_preds = model.predict(X_train)
    train_accuracy = accuracy_score(y_train, train_preds)
    return model, train_accuracy
