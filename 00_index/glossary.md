# Glossary

## DVC
- **DVC** — Data Version Control; an open-source tool for versioning datasets and ML pipeline stages alongside code.
- **Pipeline stage** — A step in a DVC pipeline (e.g. prepare, train, evaluate) defined in `dvc.yaml` with inputs, outputs, and commands.
- **`.dvc` file** — A lightweight metafile that tracks a dataset or model file, storing its hash and cache location instead of the file itself.

## Kubeflow
- **Pipeline** — A DAG-based definition of an ML workflow composed of components, defined as a YAML manifest or compiled from the Kubeflow Pipelines SDK.
- **Manifest** — A YAML file describing a Kubeflow resource (pipeline, component, experiment, run).
- **KFP SDK** — The Kubeflow Pipelines SDK (v2) used to define, compile, and run pipelines in Python.
- **Pipeline root** — The storage location (S3, MinIO, GCS) where KFP stores pipeline artifacts and outputs.
- **`dsl.component`** — A decorator in the KFP SDK that marks a Python function as a reusable pipeline component.

## Metaflow
- **Flow** — A directed acyclic graph of steps that defines an ML workflow in Metaflow.
- **Step** — A single unit of work in a Metaflow flow, decorated with `@step`.
- **Namespace** — A Metaflow concept for isolating runs and data across users or environments.
- **Branching** — A pattern where a step fans out to multiple parallel steps via `self.next(step_a, step_b)`.
- **Join** — A step that collects outputs from multiple parallel branches using the `inputs` parameter.
- **Parameter** — A CLI-defined flow parameter declared with `Parameter()` that can be overridden at runtime.

## MLflow
- **MLflow Project** — A reusable, packaging-format for ML code with a `MLproject` file specifying entry points and environments.
- **Autologging** — Automatic logging of metrics, parameters, and model artifacts by MLflow's `autolog()` integration with common ML frameworks.
- **Model Registry** — A centralized model store in MLflow for versioning, annotating, and managing model lifecycle stages.

## Feast
- **Feature Store** — A centralized system for managing and serving ML features consistently across training and inference.
- **Feature View** — A defined feature or group of features with a data source, transformation logic, and optional metadata.
- **Entity** — A primary key or identifier (e.g. `user_id`, `product_id`) that features are associated with.
- **Feature Service** — A deployed server that serves the latest feature values for real-time inference.
- **Offline Store** — A data store (e.g. BigQuery, Snowflake, Parquet) that holds historical feature data for training.
- **Online Store** — A low-latency data store (e.g. Redis, DynamoDB) that holds the latest feature values for serving.

## Weights & Biases
- **Run** — A single execution of an experiment tracked in W&B, with logged metrics, hyperparameters, and outputs.
- **Sweep** — A hyperparameter optimisation job in W&B that orchestrates multiple runs with a search strategy (grid, random, Bayesian).
- **Artifact** — A versioned file or directory (dataset, model, output) stored and tracked in W&B.
