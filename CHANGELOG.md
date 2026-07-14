# Changelog

## 2026-07-14

- clml-006: config(yaml) — ClearML task and pipeline configuration for remote GPU execution (L2)
- mfl-032: notes — Install Metaflow, run the hello-world flow, and explore the CLI (L1)
- mlf-011: snippet(python) — MLflow tracking quickstart: log params, metrics, and a model artifact (L2)
- kub-033: notes — Install Kubeflow Pipelines standalone on kind and explore the UI (L1)
- kserve-007: snippet(python) — Custom predictor with Alibi explainer for InferenceService via the Python SDK (L2)
- mlf-012: config(yaml) — Configure MLflow tracking server with PostgreSQL backend and S3 artifact store (L2)
- Passed ([x]) mlf-011 — MLflow: snippet — Follow the official MLflow tracking quickstart — log params, metrics, and a model artifact · Level: L2 · 2026-07-14
- Passed ([x]) kub-033 — Kubeflow: notes — Install Kubeflow Pipelines standalone on kind and explore the UI · Level: L1 · 2026-07-14
- Passed ([x]) clml-006 — ClearML: config — ClearML task and pipeline configuration for remote GPU execution · Level: L2 · 2026-07-14
- Passed ([x]) mfl-032 — Metaflow: notes — Install Metaflow, run the hello-world flow, and explore the CLI · Level: L1 · 2026-07-14
- databricks-003: config(yaml) — Unity Catalog model registration config with catalog, schema, access controls, and staging lifecycle (L2)
- databricks-004: script(python) — Model registration and staging promotion with Unity Catalog and MLflow (L2)

## 2026-07-13

- metaflow-028: manifest(yaml) — Metaflow DevStack Docker Compose manifest for local metadata service and UI (L2)
- wnb-034: manifest(yaml) — W&B CI/CD GitHub Actions workflow for the wandb-cicd-project template (L2)
- con-072: script — Generate and smoke-test a multi-stage Dockerfile (training stage → onnxruntime serving stage) via the Docker CLI (L2)
- Passed ([x]) con-072 — Containerization: script — Multi-stage Dockerfile for ML training with onnxruntime serving stage · Level: L2 · 2026-07-13
- zenml-010: script(python) — Multi-step ZenML pipeline with custom materializers and MLflow logging (L2)
- Passed ([x]) zenml-010 — ZenML: script — Multi-step ZenML pipeline with custom materializers and MLflow logging · Level: L2 · 2026-07-13
- zenml-011: notebook — Hierarchical ZenML pipelines: parent-child orchestration and artifact lineage (L2)

## 2026-07-12

- seldon-007: notes — Seldon Core vs KServe for sklearn model serving: choosing the right platform (L2)
- con-070: script(python) — Writing and reading features from an online store with a point-in-time join backend (L2)
- con-071: script(python) — Deploy a FastAPI inference endpoint with batching, caching, and health checks (L2)
- mfl-030: script(python) — Metaflow flow with @step, custom logging, and artifact persistence (L2)
- clml-007: notes — ClearML pitfalls: queues, task dependencies, and artifact uploads (L2)
- kub-029 (rework): manifest(yaml) — Rewrote the kubeflow-pipeline-scaffold CI/CD workflow with no unverified action version pins (git-based checkout, runner Python, run.py submit); cleaned the reference manifest of unbacked version numbers (L2)
- Passed ([x]) kub-029 — Kubeflow: manifest — Create `.github/workflows/ci-cd.yml` for kubeflow-pipeline-scaffold template · Level: L2 · 2026-07-12
- zenml-009: config(yaml) — ZenML stack config with MLflow experiment tracker and S3 artifact store (L2)
- mfl-031: script(python) — Metaflow flow with @kubernetes decorator and cloud metadata tracking (L2)

## 2026-07-11

- mfl-029: notes — Follow the official Metaflow quickstart and write up what tripped me up (L2)
- wnb-035: notes — Follow the official W&B quickstart and write up what tripped me up (L2)
- kub-030: notes — KFP v2 quickstart: two-pod-per-step, artifact passing, and cache-deployer pitfalls (L2)
- wnb-033: manifest(yaml) — Add the missing `.github/workflows/ci-cd.yml` to the wandb-cicd-project template so the README's CI/CD reference resolves (L2)
- kub-029: manifest(yaml) — Add `.github/workflows/ci-cd.yml` to the kubeflow-pipeline-scaffold template plus a reference manifest describing the CI/CD workflow steps and secrets (L2)

## 2026-07-10

- con-015: script(python) — Apply model registry to version and promote ML models (L2)
- con-016: snippet(python) — Data versioning fundamentals exercises (L2)
- con-017: script(python) — Track dataset snapshots for reproducible training with data versioning (L2)
- con-018: snippet(python) — Pipeline orchestration fundamentals exercises (L2)
- con-019: script(python) — Build and run a DAG-based ML pipeline with orchestration (L2)
- con-020: snippet(python) — Feature store fundamentals exercises (L2)

## 2026-07-09

- mflow-030: notebook — Exploring MLflow runs, experiments, and model registry interactively (L2)
- mfl-028: snippet(python) — Build my first Metaflow flow with branching, retry, and foreach (L2)
- mfl-026: notes — Explore Metaflow's CLI and local development UI (L1)
- mfl-027 (rework): dockerfile — Custom Metaflow runtime Docker image with GPU and distributed dependencies (L4) — pinned CUDA base image tag, kubectl version, and kustomize download URL; added version sources to research.md
- wnb-033: notes — Explore the W&B dashboard: projects, runs, and artifacts (L1)

## 2026-07-06

- mflow-029: config(yaml) — Configure MLflow tracking server with PostgreSQL backend and S3 artifact store (L2)
- kub-026: notes — Explore the Kubeflow Central Dashboard: app tiles, subprojects, and what tripped me up (L1)
- mfl-025: snippet(python) — Install Metaflow and run my first flow locally (L1)
- mfl-026: notes — Explore Metaflow's CLI and local development UI (L1)
- kub-025: notes — Follow the official KFP v2 quickstart and write up what tripped me up (L2)

## 2026-07-05

- mfl-028: script(python) — End-to-end experiment with MLflow tracking, model logging, and registry registration (L2)
- wnb-033: notes — Explore the W&B dashboard: projects, runs, and artifacts (L1)

## 2026-07-04

- wnb-032: snippet(python) — Log my first experiment with W&B Python SDK (L1)
- kserve-003: config(yaml) — Minimal InferenceService YAML for a sklearn model (L1)
- seldon-001: notes(primer) — What is Seldon Core? — quick primer (L1)
- seldon-002: snippet(python) — Install Seldon Core and deploy my first model with the Python SDK (L1)

## 2026-07-03

- kserve-001: notes(primer) — What is KServe? — quick primer (L1)
- kserve-002: snippet(python) — Install KServe and deploy my first InferenceService (L1)
- evid-003: notes — What I learned comparing Report and TestSuite APIs in Evidently (L1)
- mfl-028: script(python) — End-to-end experiment with Metaflow tracking, model logging, and run comparison (L2)

## 2026-07-01

- mflow-026: config(yaml) — Configure MLflow tracking server with SQLite backend and S3 artifact store (L1)
- mflow-026: notes — Follow the official MLflow quickstart and write up what tripped me up (L2)
- mflow-027: snippet(python) — Minimal model training with MLflow autologging (L2)
- wnb-030: snippet(python) — Log my first W&B run with metrics and config (L1)

## 2026-06-30

- mflow-012: snippet(python) — Install MLflow and log my first experiment with the Python SDK (L1)
- mflow-013: notes — Explore the MLflow UI — what's there (L1)

## 2026-06-29

- kub-017: script(python) — Reusable KFP pipeline component factory with resource config and caching (L4)

## 2026-06-25

- con-012: snippet(python) — Practice: experiment tracking fundamentals exercises (L2)
- con-013: script(python) — Applying experiment tracking to compare ML training runs (L2)
- con-014: snippet(python) — Practice: model registry fundamentals exercises (L2)

## 2026-06-24

- con-004: notes(primer) — Pipeline Orchestration — what it is and why it matters for ML workflows (L1)
- con-005: notes(primer) — Feature Store — what it is and why it matters in production ML (L1)
- con-006: notes(primer) — Model Serving — what it is and why it matters for ML deployment (L1)
- con-007: notes(primer) — Containerization — what it is and why it matters in MLOps (L1)
- con-008: notes(primer) — Monitoring & Drift — what it is and why it matters for model reliability (L1)

## 2026-06-23

- con-001: notes(primer) — Experiment Tracking — what it is and why it matters for MLOps (L1)
- con-002: notes(primer) — Model Registry — what it is and why it matters in ML pipelines (L1)
- con-003: notes(primer) — Data Versioning — what it is and why it matters for reproducible ML (L1)

## 2026-06-22

- clml-001: notes(primer) — What is ClearML Orchestration? — quick primer (L1)
- clml-002: snippet(python) — Install ClearML and run my first task from a Python script (L1)
- clml-003: notes — ClearML Web UI — first look at projects, experiments, and dashboards (L1)
- evid-001: notes(primer) — What is Evidently AI? — quick primer (L1)
- evid-002: snippet(python) — Install Evidently and generate my first data drift report (L1)

## 2026-06-21

- mfl-017: docs — Metaflow + W&B integration: tracking artifacts and metrics across flows (L4)
- mfl-016: manifest(yaml) — Infrastructure-as-code for Metaflow flows on AWS Batch (L4)
- wnb-018: template — Project scaffold: W&B experiment tracking with CI/CD pipeline (L4)

## 2026-06-20

- wnb-017: manifest(yaml) — Docker Compose for W&B Launch agent with local worker setup (L4)
- wnb-016 (rework): docs — W&B Model Registry end-to-end workflow with corrected link_artifact APIs (L4)
- wnb-015: script(python) — Reusable sweep + evaluation pipeline with W&B Python SDK (L4)

## 2026-06-19

- zenml-002: snippet(python) — Create and run my first ZenML pipeline with a training step (L1)
- mfl-014: docs — foreach vs @batch in Metaflow: comparing fan-out and resource scaling approaches (L3)
- zenml-003: notes — Explore the ZenML dashboard and configure my first stack (L1)
- kub-016: docs — Wiring Kubeflow Pipelines to an in-cluster MLflow tracking server (L4)
- zenml-001 (rework): notes(primer) — What is ZenML? — quick primer (L1) — removed "production" from stack definition, kept L1 first-person voice

## 2026-06-18

- kub-015: manifest(yaml) — Katib hyperparameter tuning job with random search and PyTorch training (L4)
- kub-014: dockerfile — Custom Kubeflow Pipelines component Dockerfile with scikit-learn and cloudpickle (L4)
- kub-013: template — Project scaffold: Kubeflow Pipelines + MLflow tracking integration (L4)

## 2026-06-17

- mfl-013: notebook — Compare Metaflow full run vs resume workflow during iterative model development (L3)
- wnb-014: notes — Explore the W&B dashboard: runs, projects, and experiment comparison (L1)
- wnb-013: config(yaml) — Declarative hyperparameter sweep config with W&B YAML (L3)

## 2026-06-16

- mfl-012: docs — Metaflow resource management: @conda, @resources, and timeout configuration (L3)
- kub-012: notebook — KFP hyperparameter tuning: Katib vs custom ParallelFor comparison (L3)
- kub-011 (rework): docs — Kubeflow pipeline debugging: infrastructure failures and pod log analysis (L3)
- wnb-012: notebook — W&B sweep config vs Python API for hyperparameter optimization (L3)

## 2026-06-15

- kub-011 (rework): docs — Kubeflow pipeline debugging: infrastructure failures and pod log analysis (L3)
- wnb-010: script(python) — Build a hyperparameter sweep with W&B from scratch (L3)
- wnb-011: docs — How I wired W&B artifact tracking into a data pipeline (L3)
- mfl-008: notes — How Metaflow's @step decorator enforces DAG ordering (L2)
- kub-010: snippet(python) — Kubeflow pipeline with conditional branching and resource constraints (L3)

## 2026-06-14

- gen-020: docs — Root layout audit for README (L1)
- gen-019: docs — Empty root item pass for README Layout (L1)
- gen-018: docs — README.md layout pass and root item check (L1)
- gen-016: docs — Document dvc/configs/ folder in README Layout and Coverage sections
- kub-009: snippet(python) — Minimal KFP v2 pipeline with the Python SDK (L2)
- mflow-012: snippet(python) — Install MLflow and log my first run with metrics and parameters (L1)

## 2026-06-13

- gen-015: docs — Document 00_index/ folder in README Layout section
- kub-008: snippet(python) — Minimal Kubeflow Pipelines component with Python SDK — just adds two numbers (L1)
- gen-014: docs — Actually added CHANGELOG.md to README Layout section (second pass after auditor UF flag)

## 2026-06-12

- mfl-011 (rework): script(python) — Build a 5-step ML pipeline with Metaflow from scratch (load → clean → feature engineering → train → evaluate) (L3)
- mfl-010: notes — How I wired Metaflow into a CI/CD workflow with GitHub Actions (L2)
- mflow-008: snippet(python) — Build an end-to-end training pipeline with MLflow autologging (L3) — wine dataset, model comparison, Model Registry registration

## 2026-06-11

- mflow-013: config(yaml) — Define mlflow_tracking.yaml with local backend store configuration (L1)
- mflow-008: snippet(python) — Build an end-to-end training pipeline with MLflow autologging (L3)
- wnb-009: snippet(python) — Minimal W&B artifact logging with Python API (L2)
- mfl-009: snippet(python) — Parameterize a Metaflow flow with @parameters decorator (L2)
- mflow-009: docs — Production MLflow tracking server deployment with Nginx auth proxy (L3)

## 2026-06-10

- mflow-007: snippet(python) — Minimal model serving with MLflow Python API (L2)

## 2026-06-09

- kub-010: notes — KFP v2 SDK gotchas and first component exploration (L2)
- kub-011: snippet(python) — Minimal KFP v2 pipeline end-to-end with Python SDK (L2)
- kub-003 (rework): notes — Third pass through Kubeflow Pipelines quickstart: component output artifact behavior, SDK client API drift, and minikube image pulling
- gen-019: config(yaml) — Populate feast/configs/ with Feast feature_store.yaml and related configs
- gen-017: docs — Document feast/configs/ folder in README Layout and Coverage sections

## 2026-06-08

- gen-011: docs — Document feast/ folder in README Layout and Coverage sections
- kub-003: notes — Second pass through Kubeflow Pipelines quickstart and what tripped me up
- mfl-008: notes — How Metaflow's @step decorator enforces DAG ordering (L2)
- wnb-007 (rework): config(yaml) — Define a W&B hyperparameter sweep with a sweep config YAML (L2)
- kub-004: manifest(yaml) — Deploy a Kubeflow pipeline with Kubernetes Job set (L2)
- gen-011: docs — Document feast/ folder in README Layout and Coverage sections
- kub-003: notes — Second pass through Kubeflow Pipelines quickstart and what tripped me up

## 2026-06-07

- wnb-006: snippet(python) — Minimal experiment tracking with Weights & Biases Python API (L2)
- gen-013: docs — Document General/ folder in README Layout section
- kub-005 (rework): notes(primer) — Fix Kubeflow primer: reduced to ≤300 words, removed "production", kept L1 first-person scratch voice

## 2026-06-06 (Round 2)

- gen-012 (rework): docs — Add feast/ root folder to README Layout section and Coverage table

## 2026-05-25

- wnb-001: notes(primer) — What is W&B? — quick primer
- wnb-002: notes — Install wandb and log my first run
- wnb-003: script(python) — Train a tiny model with W&B metric tracking
- gen-001: docs(markdown) — Add mlflow/ directory to README Repository Structure
- gen-002: docs(markdown) — Add wnb/ directory to README Repository Structure
- gen-003: docs(markdown) — Add 00_index/ directory to README Repository Structure
- kf-001: notes(primer) — What is Kubeflow? — quick primer
- kf-002: notes — Install Kubeflow locally and explore the UI — what's there
- kf-003: manifest(yaml) — Deploy a minimal Kubeflow component/workflow and inspect the dashboard

## 2026-05-26

- gen-004: docs(markdown) — Add CHANGELOG.md reference to README documented files
- meta-001: notes(primer) — What is Metaflow? — quick primer
- meta-002: config(yaml) — Install Metaflow and set up my first project scaffold
- mlf-005: snippet(python) — Minimal model training with MLflow autologging and model registration
- mlf-006: config(yaml) — Define an MLflow Project with conda environment and parameters
- dvc-001: notes(primer) — What is DVC? — quick primer
- dvc-002: notes — Install DVC and version my first dataset
- dvc-003: snippet(bash) — Track a data pipeline end-to-end with DVC

## 2026-05-26 (Round 2)

- wnb-002: snippet(python) — Minimal experiment tracking with W&B SDK: log metrics and artifacts
- wnb-003: config(yaml) — Configure a W&B hyperparameter sweep with search strategy

## 2026-05-27

- meta-003: notes — Run my first end-to-end Metaflow flow and record what happened
- mlf-004: notes — Follow the official MLflow quickstart and write up what tripped me up
- wnb-001: docs — Follow the official W&B quickstart and write up what tripped me up

## 2026-05-27 (Round 2)

- kub-004: notes — Set up a local Kind cluster for Kubeflow and verify CRDs
- gen-003: docs — Document CHANGELOG.md and wnb/ subdirectories in MLOps-Kit README structure
- mlf-005: notes — Install MLflow and run my first tracking experiment
- mlf-006: snippet(python) — Log my first metrics and parameters with MLflow Tracking
- gen-001: docs — Document mlflow/configs/ in README structure

## 2026-05-27 (Round 3)

- wnb-003: notes — Install W&B and run my first experiment tracking
- wnb-004: snippet(python) — Log my first metrics and parameters with W&B
- gen-002: docs — Document CHANGELOG.md in MLOps-Kit README

## 2026-05-27 (Round 4)

- kub-001: notes — Follow the official Kubeflow Pipelines quickstart and document what tripped me up
- kub-002: snippet(python) — Minimal pipeline with Kubeflow Pipelines V2 SDK

## 2026-05-27 (Round 5)

- kub-003: script(bash) — Diagnose Kubeflow backend service health with a verification script
- mfl-001: notes — Follow the official Metaflow quickstart and document what tripped me up
- gen-001: docs — Document kubeflow/snippets/ directory in README layout

## 2026-05-28

- mfl-003: notebook — Step through a basic Metaflow flow end-to-end with data and decisions

## 2026-05-28 (Round 2)

- mflow-005: config(yaml) — Define an MLflow Project with MLproject and conda environment
- mflow-004: notes — Follow the official MLflow Tracking quickstart and write up what tripped me up

## 2026-05-30

- kub-006: config(yaml) — Configure Kubeflow pipeline resource requests and limits
- wnb-006: config(yaml) — Configure W&B project settings and tracking environment

## 2026-05-30 (Round 2)

- kub-004: notes — Install Kubeflow on a local Kind cluster and document what tripped me up
- kub-005: script(bash) — Script to verify Kubeflow component readiness after local deployment

## 2026-05-30 (Round 3)

- dvc-005: script(bash) — Initialize a DVC project and track my first dataset
- mfl-004: notes — Install Metaflow and set up my dev environment

## 2026-05-30 (Round 4)

- mflow-001: script(python) — Build a custom MLflow model flavor from scratch

## 2026-05-31

- mflow-002: docs — Comparing registered model versions with MLflow Model Registry
- wnb-004: notes — Install W&B and run my first experiment tracking session

## 2026-06-01

- wnb-002: notes(primer) — What is Weights & Biases? — quick primer
- wnb-004: notes — Install W&B and run my first experiment tracking session
- feast-001: notes(primer) — What is Feast? — quick primer

## 2026-06-03

- feast-002: notes — Install Feast and run my first feature retrieval
- feast-003: snippet(python) — Define and apply my first feature view with Feast

## 2026-06-03 (Round 2)

- mfl-005: snippet(python) — My first linear Metaflow DAG with parameters
- wnb-003: snippet(python) — Log my first metrics and parameters with W&B SDK
- gen-001: docs — Document metaflow/notebooks/ folder in README Layout section

## 2026-06-04

- kub-002: snippet(python) — Deploy my first Kubeflow pipeline with Python SDK
- gen-002: docs — Document kubeflow/configs/ folder in README Layout section
- gen-003: docs — Document dvc/scripts/ folder in README Layout section

## 2026-06-05

- dvc-001: notes — Follow the official DVC Get Started guide and document what tripped me up
- dvc-002: snippet(python) — Minimal data versioning with DVC Python API
- dvc-003: config(yaml) — Define a DVC pipeline with dvc.yaml from scratch
- mfl-001: notes — Install Metaflow and run my first flow end-to-end
- wnb-005: notes — Configure W&B settings and run first team experiment
- gen-004: docs — Document mlflow/scripts/ folder in README Layout section

## 2026-06-05 (Round 2)

- gen-004 (rework): docs — Document mlflow/scripts/ folder in README Layout section

## 2026-06-06

- gen-005: docs — Document mlflow/docs/ folder in README Layout section
- gen-006: docs — Document 00_index/topics.md file in README Layout section
- gen-007: docs — Document mlflow/notebooks/ folder in README Layout section
- gen-011: docs — Restructure MLOps-Kit: document feast/ folder in README Layout and Coverage sections
- gen-012: docs — Add feast/ root folder to README Layout section and Coverage table
- gen-013: docs — Document General/ folder in README Layout section
- gen-014: docs — Document CHANGELOG.md in README Layout section
- kub-006: notes — Install minikube and Kubeflow CLI, verify local setup
- kub-007: notes — Explore the Kubeflow Central Dashboard — what's there
- mfl-002: notes — Explore Metaflow UI and inspect a completed flow run
- mfl-008: snippet(python) — Minimal first flow with Metaflow Python SDK
- wnb-004: notes — Run my first model training experiment with W&B and review the dashboard
- wnb-005: notes — Follow the official Weights & Biases quickstart and document what tripped me up
- wnb-006: snippet(python) — Minimal experiment tracking with Weights & Biases Python API
- wnb-007: config(yaml) — Define a W&B hyperparameter sweep with a sweep config YAML
- mfl-006: notes — Follow the official Metaflow quickstart and document what tripped me up
- mfl-007: snippet(python) — Minimal model serving with Metaflow Python API
- wnb-009: snippet(python) — Minimal experiment tracking with Weights & Biases Python API (first cut)
