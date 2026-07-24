---
last_verified: 2026-07-23
tool_version: ">=2.0"
sources:
  - https://dev.to/prezaei/integrating-mlflow-with-kubeflow-revised-edition-3mf
  - https://www.youngju.dev/blog/ai-platform/2026-03-11-mlflow-experiment-tracking-model-registry.en
---

# MLflow tracking server with PostgreSQL + MinIO

## Purpose

Run an MLflow tracking server locally for a small team using PostgreSQL as the backend store and MinIO as the S3-compatible artifact store. The server stores experiment metadata (params, metrics, tags) in PostgreSQL and artifacts (models, plots, datasets) in MinIO.

## Prerequisites

- Docker and Docker Compose v2 installed
- At least 2 GB of free memory on the host

## Steps

### 1. Configure environment

```bash
cp .env.example .env
```

Edit `.env` to set passwords, bucket name, or keys. The defaults work for local evaluation.

### 2. Start services

```bash
docker compose up -d
```

This starts PostgreSQL (port 5432), MinIO (ports 9000 API / 9001 console), and the MLflow tracking server (port 5000).

### 3. Create the S3 bucket in MinIO

MinIO requires the bucket to exist before MLflow writes artifacts to it.

```bash
docker compose exec minio mc alias set local http://localhost:9000 "${MINIO_ACCESS_KEY:-minioadmin}" "${MINIO_SECRET_KEY:-minioadmin}"
docker compose exec minio mc mb "local/${MLFLOW_BUCKET_NAME:-mlflow}"
```

### 4. Set the tracking URI in your training code

```python
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("my-first-experiment")

with mlflow.start_run():
    mlflow.log_param("alpha", 0.5)
    mlflow.log_metric("rmse", 0.23)
    mlflow.log_artifact("model.pkl")
```

## Verify

1. Open `http://localhost:5000` in a browser — the MLflow UI shows the experiment page.
2. Run the training snippet above. The experiment appears in the UI with params, metrics, and the model artifact.
3. Open `http://localhost:9001` — the MinIO console shows the bucket with stored artifacts.
4. Check that PostgreSQL stores experiment metadata:

```bash
docker compose exec postgres psql -U mlflow -d mlflow -c "SELECT COUNT(*) FROM experiments;"
```
