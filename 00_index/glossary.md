# Glossary

## DVC
- **DVC** — Data Version Control; an open-source tool for versioning datasets and ML pipeline stages alongside code.
- **Pipeline stage** — A step in a DVC pipeline (e.g. prepare, train, evaluate) defined in `dvc.yaml` with inputs, outputs, and commands.
- **`.dvc` file** — A lightweight metafile that tracks a dataset or model file, storing its hash and cache location instead of the file itself.

## Kubeflow
- **Pipeline** — A DAG-based definition of an ML workflow composed of components, defined as a YAML manifest or compiled from the Kubeflow Pipelines SDK.
- **Manifest** — A YAML file describing a Kubeflow resource (pipeline, component, experiment, run).

## Metaflow
- **Flow** — A directed acyclic graph of steps that defines an ML workflow in Metaflow.
- **Step** — A single unit of work in a Metaflow flow, decorated with `@step`.
- **Namespace** — A Metaflow concept for isolating runs and data across users or environments.

## MLflow
- **MLflow Project** — A reusable, packaging-format for ML code with a `MLproject` file specifying entry points and environments.
- **Autologging** — Automatic logging of metrics, parameters, and model artifacts by MLflow's `autolog()` integration with common ML frameworks.
- **Model Registry** — A centralized model store in MLflow for versioning, annotating, and managing model lifecycle stages.

## Weights & Biases
- **Run** — A single execution of an experiment tracked in W&B, with logged metrics, hyperparameters, and outputs.
- **Sweep** — A hyperparameter optimisation job in W&B that orchestrates multiple runs with a search strategy (grid, random, Bayesian).
- **Artifact** — A versioned file or directory (dataset, model, output) stored and tracked in W&B.
