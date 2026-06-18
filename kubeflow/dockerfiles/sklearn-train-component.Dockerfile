FROM python:3.9-slim AS base

WORKDIR /component

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY train.py /component/train.py

RUN useradd -m -u 1000 kfp && chown -R kfp:kfp /component
USER kfp

ENTRYPOINT ["python", "/component/train.py"]
