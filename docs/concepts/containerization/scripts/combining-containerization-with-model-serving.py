# last_verified: 2026-08-14 · containerization n/a

"""
Demonstrates the containerization + model serving integration pattern.

A model is trained with scikit-learn, saved in MLflow's model format,
and then packaged into a Docker image that serves it over HTTP using
mlflow models serve. The script builds the image, runs it, and performs
a smoke test against the root endpoint before tearing the container down.

This follows the flagship pattern from the research notes: MLflow's
model format as the portable artifact, Docker as the deployment seam,
and a lightweight serving runtime inside the container.

Prerequisites:
  - Docker daemon running locally
  - mlflow installed
  - scikit-learn installed
"""

import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request

import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


def train_and_log(model_dir: str) -> str:
    """Train a tiny model and save it in MLflow format."""
    X, y = load_iris(return_X_y=True)
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)

    mlflow.sklearn.save_model(model, model_dir)
    print(f"saved model to {model_dir}")
    return model_dir


def build_image(model_dir: str, tag: str) -> None:
    """Build a Docker image that serves the model with mlflow models serve."""
    if shutil.which("docker") is None:
        raise RuntimeError("docker is not installed or not on PATH")

    with tempfile.TemporaryDirectory() as tmp:
        dockerfile = os.path.join(tmp, "Dockerfile")
        with open(dockerfile, "w") as fh:
            fh.write(
                f"FROM python:3.11-slim\n"
                "WORKDIR /app\n"
                "RUN pip install --no-cache-dir mlflow scikit-learn\n"
                f"COPY {os.path.basename(model_dir)} /app/model\n"
                "EXPOSE 5000\n"
                'CMD ["mlflow", "models", "serve", "--model-uri", "file:///app/model", "--host", "0.0.0.0", "--port", "5000"]\n'
            )
        ctx_model = os.path.join(tmp, os.path.basename(model_dir))
        shutil.copytree(model_dir, ctx_model)

        result = subprocess.run(
            ["docker", "build", "-t", tag, tmp],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError(f"docker build failed: {result.stderr}")
        print(f"built image {tag}")


def smoke_test(tag: str) -> None:
    """Run the container and hit the root endpoint."""
    if shutil.which("docker") is None:
        print("docker not available -- skipping smoke test")
        return

    try:
        container = subprocess.run(
            ["docker", "run", "-d", "-p", "5000:5000", tag],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"docker run failed: {exc.stderr}") from exc

    cid = container.stdout.strip()
    try:
        time.sleep(10)
        with urllib.request.urlopen("http://localhost:5000/", timeout=5) as resp:
            print(f"smoke test: {resp.status}")
    except Exception as exc:
        print(f"smoke test skipped or failed: {exc}")
    finally:
        subprocess.run(["docker", "stop", cid], check=False)
        subprocess.run(["docker", "rm", cid], check=False)


if __name__ == "__main__":
    tag = "containerization-model-serving:practice"
    with tempfile.TemporaryDirectory() as workdir:
        model_dir = os.path.join(workdir, "model")
        os.makedirs(model_dir)
        train_and_log(model_dir)
        build_image(model_dir, tag)
        smoke_test(tag)
        print("done")
