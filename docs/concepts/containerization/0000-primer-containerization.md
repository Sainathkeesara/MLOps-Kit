# Containerization — quick primer

> First-day notes on Containerization. What it is, why it matters, and the key ideas to know.

## What is it?

Containerization is the practice of packaging code and its dependencies into a portable unit (a container) that runs the same everywhere. Think of it like a lightweight VM: everything your code needs — Python version, libraries, model files — lives in one snapshot that you can run on your laptop, a cloud VM, or Kubernetes without "but it works on my machine" problems.

Before Docker, I'd spend hours debugging why a script worked locally but failed on the server. Someone had Python 3.9, some needed 3.10. A library was installed on one machine but not documented. Containerization fixes this by making the environment part of the code.

## Why does it matter for MLOps?

ML code has messy dependency requirements — specific Python versions, CUDA drivers, compiled libraries. Containerization matters because:
- It eliminates environment drift between dev, test, and prod.
- It lets you version your runtime alongside your model.
- It enables scaling: spin up 10 identical containers in Kubernetes.
- It isolates experiments: no cross-contamination between model versions.

Every serious MLOps platform (Kubeflow, KServe, Seldon) expects containers. Without them, you're stuck with manual environment setup.

## Key terminology

- **Container image** — A read-only template containing code and dependencies. Example: `ml-model:v1.2.3` with sklearn 1.3.
- **Container registry** — A storage service for images, like Docker Hub or ECR. Example: push `my-model:latest` to GitHub Packages.
- **Dockerfile** — A script that builds an image layer by layer. Example: `FROM python:3.10`, `COPY requirements.txt .`, `RUN pip install -r requirements.txt`.
- **Layer** — Each instruction in a Dockerfile creates a cached layer. Example: installing dependencies once saves rebuild time.
- **Base image** — The starting point for a container (usually an OS plus runtime). Example: `python:3.10-slim` or `nvidia/cuda:12.0-runtime`.
- **ENTRYPOINT** — The command that runs when the container starts. Example: `python serve.py` starts a model server.
- **Volume** — A directory mounted from the host into the container for persistent data. Example: `/models` volume to share model files.
- **Multi-stage build** — Building in stages to keep final images small. Example: compile in one stage, copy artifacts to clean stage.
- **GPU support** — Special base images and runtime flags for GPU acceleration. Example: `nvidia/cuda` base with `--gpus all` flag.

## A concrete example

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY model.pkl .
COPY serve.py .

ENTRYPOINT ["python", "serve.py"]
```

This builds an image with Python 3.10, installs dependencies, copies the model and server script, and runs the server when started.

## How this connects to what's next

Containers are the foundation for model serving (KServe, Seldon all containerize models) and pipeline orchestration (Metaflow steps run in containers). Next I want to write a Dockerfile for a sklearn model and run it locally before pushing it to a registry for use in Kubernetes.