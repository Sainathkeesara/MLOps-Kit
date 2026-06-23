# Learning Path — MLOps

> A suggested progression from beginner to confident practitioner. Each stage builds on the previous one. If a topic is listed but has no content yet, it's marked as ⏳ (coming soon).

## Stage 1: Foundations

Before picking up any tool, build a shared vocabulary for the four concepts that underpin this kit:
- **Experiment Tracking** — Capture, compare, and reproduce result sets from training runs. Unlocks: MLflow, W&B.
- **Data Versioning** — Track datasets and data lineage alongside code. Unlocks: DVC, Feast.
- **Pipeline Orchestration** — Define, schedule, and monitor multi-step ML workflows. Unlocks: Kubeflow, Metaflow, ZenML.
- **Monitoring & Drift** — Detect statistical or performance degradation in production inputs and predictions. Unlocks: Evidently AI.

Start with the primer for any tool you're already using — the primers (files prefixed `0000-`) are written as first-day walkthroughs and assume only basic Python familiarity.

## Stage 2: Core Tools

Pick one core tool and work through its primer, setup notes, and first runnable snippet before moving to the next.

- **MLflow** — Experiment tracking and model registry. Start with the primer, then install and log your first run. Content covers L1–L4: server setup, autologging, model serving, and registry workflows.
- **Weights & Biases** — Dashboard-driven experiment tracking with built-in hyperparameter sweeps. Content covers L1–L4: first experiment, sweep configs, artifact tracking, CI/CD templates, and dashboard exploration.
- **Kubeflow** — Kubernetes-native pipeline orchestration. Start with the Kind-cluster or minikube setup notes, then build your first pipeline component. Content covers L1–L4: KFP SDK, manifests, Katib HPO, debugging, and MLflow integration.

## Stage 3: Building Skills

Once the three core tools feel familiar, layer in workflow frameworks, feature stores, and drift monitoring.

- **Metaflow** — Human-friendly DAG orchestration with built-in versioning and resume. Content covers L1–L4: first flow, DAG ordering, resource management, foreach vs @batch, CI/CD wiring, and W&B integration.
- **Feast** — Feature store for consistent training and serving. Content covers L1: first feature view, feature store config, and online/offline store setup with SQLite.
- **ZenML** — Modular pipeline framework with pluggable stacks. Content covers L1–L2: dashboard exploration, S3 artifact store stack, and first training pipeline.
- **Evidently AI** — Data drift and model quality monitoring. Content covers L1: primer and first drift report generation.

## Stage 4: Advanced Tools

These tools reward users who have already built intuition for at least one core tool. Work through them in the order that matches your project needs.

- **ClearML** — Task orchestration and MLOps platform. Content covers L1: install, first task, and web UI walkthrough.
- **DVC** — Data versioning tied to Git. Content covers L1–L2: pipeline definition, dataset tracking, and get-started primer.

## Mastery

The tools below are catalogued in the hierarchy but have limited content on disk so far. Whenever new content lands, the learning path will be updated to point directly to it.

- **Model Serving** — Deploy models with KServe, Seldon Core, or SageMaker (⏳).
- **Containerization patterns** — Build and tune custom KFP component containers (Dockerfile reference available under kubeflow).
- **Advanced Monitoring** — Extend Evidently test suites beyond drift to model quality and data integrity (⏳).

## Progression Map

```
 Foundation concepts (Stage 1) unlock every Core Tool.
 The Core Tools (Stage 2) provide the vocabulary needed
 to work with Building-Skills tools (Stage 3).
 Advanced tools (Stage 4) layer on top of that foundation:
 ──────────────────────────────
   Concepts        ->  Stage 2
                            \       ->  Stage 3
                             \            \
                              Stage 4  (independent per project need)
 ──────────────────────────────
```
