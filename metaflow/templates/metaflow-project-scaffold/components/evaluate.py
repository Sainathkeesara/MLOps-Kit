"""Evaluation logic extracted from the Metaflow flow for testability."""

from sklearn.metrics import accuracy_score, classification_report


def evaluate_classifier(model, X_test, y_test, target_names):
    """Evaluate a classifier and return (test_accuracy, report_string)."""
    preds = model.predict(X_test)
    test_accuracy = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds, target_names=target_names, digits=3)
    return test_accuracy, report
