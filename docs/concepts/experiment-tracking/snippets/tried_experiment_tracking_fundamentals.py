"""Practice: experiment tracking fundamentals exercises (L2)

I wrote this snippet to get comfortable with the basic experiment
tracking pattern — start a run, log stuff, end a run. Using MLflow
here since it's the tracker I have set up locally.
"""

import mlflow
import random

mlflow.set_experiment("fundamentals-practice")

with mlflow.start_run(run_name="first-try"):
    # logging params I'd usually set in a config
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("batch_size", 32)
    mlflow.log_param("optimizer", "adam")

    # pretending I'm training for 5 epochs
    for epoch in range(5):
        loss = 0.5 ** (epoch + 1) + random.uniform(-0.05, 0.05)
        acc = 0.6 + 0.08 * epoch + random.uniform(-0.02, 0.02)
        mlflow.log_metric("loss", loss, step=epoch)
        mlflow.log_metric("accuracy", acc, step=epoch)

    # saving a dummy model file as an artifact
    with open("model.txt", "w") as f:
        f.write("dummy model weights placeholder")
    mlflow.log_artifact("model.txt")

print("Run finished — check the MLflow UI to see params, metrics, and the artifact.")
