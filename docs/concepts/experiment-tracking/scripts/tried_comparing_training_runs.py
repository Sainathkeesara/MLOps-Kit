"""Applying experiment tracking to compare ML training runs (L2)

I wanted to see how different hyperparameter values show up in the
tracking UI side-by-side. This script runs three quick training jobs
with different learning rates and logs everything so I can compare
the curves afterward.
"""

import mlflow
import random

mlflow.set_experiment("lr-comparison")

def train_model(lr, epochs=10):
    with mlflow.start_run(run_name=f"lr-{lr}"):
        mlflow.log_param("learning_rate", lr)
        mlflow.log_param("epochs", epochs)
        mlflow.log_param("model", "dummy-regressor")

        best_acc = 0.0
        for epoch in range(epochs):
            # fake training — loss goes down, accuracy goes up
            loss = 0.8 * (0.7 ** epoch) + random.uniform(-0.03, 0.03)
            acc = min(0.5 + 0.04 * epoch + random.uniform(-0.01, 0.01), 0.95)
            mlflow.log_metric("loss", loss, step=epoch)
            mlflow.log_metric("accuracy", acc, step=epoch)
            best_acc = max(best_acc, acc)

        mlflow.log_metric("best_accuracy", best_acc)
        print(f"  lr={lr:6.4f}  best_acc={best_acc:.3f}")

# try three different learning rates side by side
learning_rates = [0.1, 0.01, 0.001]

print("Training with different learning rates...")
for lr in learning_rates:
    train_model(lr)

print("\nDone. Open the MLflow UI and compare the three runs under")
print("'lr-comparison' — the accuracy curves should show which lr worked best.")
