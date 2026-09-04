---
last_verified: 2026-09-04
tool_version: n/a
---

# Containerization — Multi-stage Dockerfile for MLOps

> Trying to separate training and serving into one Dockerfile

## What I was trying to do

I wanted a single Dockerfile that could train a model and then serve it, but without dragging gcc, CUDA toolkit, and pip cache into the serving image. Multi-stage builds let me define separate `FROM` lines — each stage can use a different base image, and I copy only the artifacts I need between them.

## The Dockerfile

I wrote this for a scikit-learn churn model. The first stage (`trainer`) has everything needed to train: a full Python image, build tools, training deps. The second stage (`serving`) starts from a slim Python image and copies just the pickled model and the serving code.

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.11 AS trainer
WORKDIR /build
COPY requirements.train.txt .
RUN pip install --no-cache-dir -r requirements.train.txt
COPY train.py .
RUN python train.py && cp model.pkl /model.pkl

FROM python:3.11-slim AS serving
COPY --from=trainer /model.pkl /app/model.pkl
COPY requirements.serve.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.serve.txt
COPY serve.py /app/
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

I built it with `docker build -t churn-predictor:1.0.0 --target serving .` and verified the image was ~180 MB instead of the ~900 MB the single-stage version was.

## Got stuck on

**File not found at runtime.** The first time I ran the container it crashed because `app:app` expects `serve.py` to match the `COPY` destination but the `COPY` path was wrong. Double-checking the working directory in `serve.py`'s import paths fixed it.

**Training stage cached bad model.** I iterated on `train.py` but Docker used the cached layer from the first build. Adding `--no-cache-filter=trainer` to the build command forced a re-run of just the training stage.

## What I'd try next

Pin base image digests instead of tags so rebuilds are reproducible. I also want to try splitting the training stage further — one layer for system deps and one for Python packages — so the cache invalidates less often during development.
