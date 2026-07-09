# last_verified: 2026-07-09 · Metaflow n/a

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    metaflow \
    ray[default] \
    numpy \
    pandas \
    scikit-learn \
    cloudpickle \
    boto3 \
    s3fs

RUN groupadd -r metaflow && useradd -r -g metaflow -u 1000 -m -d /app metaflow

WORKDIR /app

COPY --chown=metaflow:metaflow . /app/flow/

USER metaflow

ENTRYPOINT ["python"]
CMD ["-m", "metaflow"]
