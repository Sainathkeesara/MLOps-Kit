#!/usr/bin/env python
# mflow-027 — Minimal model training with MLflow autologging (L2)
# Simple training script to test autolog behavior.

import mlflow
mlflow.sklearn.autolog()  # called early so it wraps sklearn before training starts

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

mlflow.set_experiment("autolog-demo")  # using default experiment if it exists

with mlflow.start_run():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    
    # autolog will capture n_estimators and max_depth automatically
    clf = RandomForestClassifier(n_estimators=50, max_depth=3)
    clf.fit(X_train, y_train)
    
    # accuracy from score() isn't auto-logged, so I log it manually
    acc = accuracy_score(y_test, clf.predict(X_test))
    mlflow.log_metric("test_accuracy", acc)

    print(f"Accuracy: {acc:.3f}")