---
last_verified: 2026-08-27
tool_version: n/a
---

# Databricks ML — quick primer

> First-day notes for someone who's never used Databricks ML. Personal voice, plain language.

## What is it?

Databricks ML is the machine-learning layer built on top of the Databricks Lakehouse Platform. Think of it as the difference between a raw cloud data warehouse and a fully stocked kitchen — the lakehouse gives you the storage and compute, and Databricks ML adds the MLflow tracking, the model registry, the feature store, the notebook orchestration, and the serving endpoints so you can go from experiment to a deployed model without gluing together a dozen separate tools.

I've been thinking of it as "what happens when a data-engineering platform decides to own the ML lifecycle too." It's not a single library you pip install; it's a managed workspace (on AWS, Azure, or GCP) where your notebooks, clusters, jobs, and models all live under one roof. The tight integration with Delta Lake and Spark means your training data and your feature tables are the same tables, which is the part that actually matters day-to-day.

## What does it do?

Databricks ML lets you run experiments on scalable clusters, log them automatically to MLflow, register winning models in a centralized registry governed by Unity Catalog, and deploy them as real-time serving endpoints or batch inference jobs. It also gives you a feature store for reuse across teams, AutoML for quick baselines, and orchestration via Databricks Workflows (multi-task jobs) so the whole pipeline — ingest, train, evaluate, promote, serve — lives in one place.

## Why does it exist?

Before Databricks ML, a typical setup was: Spark for data prep in one system, a separate MLflow server for experiment tracking, a custom Flask or KServe container for serving, and a cron job duct-taped to a notebook for retraining. Each piece had its own auth, its own UI, its own failure modes. Databricks ML exists because the glue work between those pieces is where ML projects quietly die — someone has to keep the tracking server alive, debug why the serving container can't read the model artifact, retrain the model when data drifts. It's used by data scientists and ML engineers who'd rather spend their time on models than on infrastructure plumbing, especially in regulated industries where Unity Catalog's governance and audit trails are a requirement, not a nice-to-have.

## Key terminology

- **Workspace** — The top-level Databricks container that holds your notebooks, clusters, jobs, and models. Example: your company's `https://acme.cloud.databricks.com` instance.
- **Cluster** — A managed Spark pool of VMs you attach to notebooks or jobs. Example: a `i3.xlarge` cluster with autoscaling from 2 to 8 workers for training.
- **Unity Catalog** — Databricks' governance layer: a three-level namespace (`catalog.schema.table`) that controls access to data and models. Example: `mlops_catalog.model_registry.sentiment_classifier`.
- **MLflow on Databricks** — Managed MLflow tracking, model registry, and experiment UI built into the workspace. Example: `mlflow.log_metric("val_accuracy", 0.92)` auto-appears in the Experiments sidebar.
- **Model Serving** — One-click real-time endpoints that serve registered models with autoscaling and A/B traffic splitting. Example: deploy `sentiment_classifier` v3 to a serving endpoint that scores JSON payloads.
- **Databricks Workflows** — Multi-task job orchestration (run notebook A, then train task B, then conditional deploy). Example: a nightly retraining job that runs only if data freshness passes a threshold.
- **Feature Store** — Managed feature tables with online and offline serving, backed by Delta tables. Example: a `customer_features` table shared between the fraud-detection training pipeline and the real-time scoring endpoint.
- **Delta Live Tables (DLT)** — Declarative ETL pipelines that handle incremental processing, expectations, and lineage. Example: a DLT pipeline that cleans raw events into a feature table with `EXPECT (count > 0)`.

## A tiny example

```python
import mlflow

mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Users/me/sentiment-classifier")

with mlflow.start_run():
    mlflow.log_param("model_type", "sentiment_classifier")
    mlflow.log_metric("val_accuracy", 0.92)
```

This connects the MLflow client to the managed tracking server in your workspace, sets the experiment namespace, and logs a single parameter and metric from a training run. The run shows up in the Databricks Experiments UI automatically — no tracking server to host.

## What I'll cover next

After the primer I want to walk through logging a real experiment end-to-end with the Python SDK, then dig into Unity Catalog model promotion workflows and how the feature store connects training to serving.
