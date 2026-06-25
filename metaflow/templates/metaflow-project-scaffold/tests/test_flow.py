"""Unit tests for component functions used by the Metaflow flow.

These tests exercise the extracted logic without spinning up the Metaflow runtime.
"""

from components.data import load_and_split_data, scale_features
from components.train import train_random_forest
from components.evaluate import evaluate_classifier
import numpy as np


def test_load_and_split_data():
    X_train, X_test, y_train, y_test, target_names = load_and_split_data(
        test_size=0.3, random_state=42
    )
    total = len(X_train) + len(X_test)
    assert total == 150, f"Expected 150 total samples, got {total}"
    assert X_train.shape[1] == 4
    assert len(X_test) == 45
    assert target_names == ["setosa", "versicolor", "virginica"]


def test_scale_features():
    X_train, X_test, _, _, _ = load_and_split_data(random_state=42)
    X_train_scaled, X_test_scaled = scale_features(X_train, X_test)
    assert X_train_scaled.shape == X_train.shape
    assert X_test_scaled.shape == X_test.shape
    assert abs(X_train_scaled.mean()) < 1e-10
    assert abs(X_train_scaled.std() - 1.0) < 1e-6


def test_train_random_forest():
    X_train, X_test, y_train, y_test, _ = load_and_split_data(random_state=42)
    X_train_scaled, X_test_scaled = scale_features(X_train, X_test)
    model, train_acc = train_random_forest(
        X_train_scaled, y_train, n_estimators=50, random_state=42
    )
    assert 0.0 <= train_acc <= 1.0
    test_preds = model.predict(X_test_scaled)
    test_acc = np.mean(test_preds == y_test)
    assert test_acc >= 0.8


def test_evaluate_classifier():
    X_train, X_test, y_train, y_test, target_names = load_and_split_data(
        random_state=42
    )
    X_train_scaled, X_test_scaled = scale_features(X_train, X_test)
    model, _ = train_random_forest(
        X_train_scaled, y_train, n_estimators=50, random_state=42
    )
    test_accuracy, report = evaluate_classifier(
        model, X_test_scaled, y_test, target_names
    )
    assert 0.0 <= test_accuracy <= 1.0
    assert "setosa" in report
