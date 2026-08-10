# last_verified: 2026-08-09 · containerization n/a
# con-094 — Multi-stage Dockerfile for ML training with serving stage (L2)
#
# Trying to bake both training and serving into one Dockerfile without
# dragging build tools and pip cache into the serving image. The trainer
# stage is fat (full Python, build tools, training deps); the serving
# stage is slim and only ships the pickled model + inference deps.
#
# Base image: python:3.12-slim. The research notes say this is ~50 MB
# for CPU-only Python services and avoids the musl issues of alpine
# that break prebuilt ML wheels (numpy, scikit-learn).
#
# Cache mounts: pip re-downloads packages on every build without a
# cache mount. --mount=type=cache,target=/root/.cache/pip keeps the
# layer count low and speeds up rebuilds during development.
#
# Non-root user: the hardening pattern says run as a non-root user to
# reduce attack surface in the serving stage.
#
# Companion files expected at build context root:
#   requirements.train.txt — training deps (scikit-learn, pandas, numpy)
#   requirements.serve.txt  — lighter serving deps (scikit-learn, numpy)
#   train.py                — trains and pickles model.pkl
#   serve.py                — loads model.pkl, serves predictions on :8000

# syntax=docker/dockerfile:1

# ── Stage 1: training (fat image with build tools) ──────────────────────────

FROM python:3.12-slim AS trainer

WORKDIR /build

# System packages first — rarely changes, good cache position
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Python training deps with cache mount so packages are reused
COPY requirements.train.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.train.txt

# App code last — changes on every commit, only invalidates this layer
COPY train.py .

# Train the model and snapshot it into /model.pkl for the serving stage
RUN python train.py && cp model.pkl /model.pkl

# ── Stage 2: serving (slim image with only inference deps) ──────────────────

FROM python:3.12-slim AS serving

WORKDIR /app

# Copy only the model artifact from the trainer stage — nothing else
COPY --from=trainer /model.pkl /app/model.pkl

# Serving deps are lighter (no pandas, no training extras)
COPY requirements.serve.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.serve.txt

COPY serve.py .

# Drop privileges — run as non-root user in the serving stage
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
CMD ["python", "serve.py"]
