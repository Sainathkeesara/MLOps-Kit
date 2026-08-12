---
last_verified: 2026-08-11
tool_version: n/a
---

# Monitoring and drift detection patterns for ML pipelines

> What I learned about keeping an eye on models after they leave the training notebook.

## What is it?

Monitoring and drift detection is the practice of watching a deployed model to make sure its inputs and outputs still look like what it was trained on. Data drift means the feature distributions in inference have shifted away from the training set — maybe user behavior changed, a new marketing campaign launched, or a sensor got recalibrated. Concept drift goes deeper: the relationship between features and target itself has changed, so even if the input looks familiar, the model's assumptions are wrong.

I've started thinking of it as a smoke detector. You don't notice it until something is already burning. The goal is to catch the shift early enough to retrain before predictions degrade into garbage.

## Why does it matter for ML pipelines?

A model that scores 92% accuracy on validation can quietly produce 60% accuracy in inference if the input data drifted and nobody noticed. Without monitoring, that gap only shows up when stakeholders complain about bad predictions. With monitoring, you get an alert and a trigger to retrain before users are affected.

The patterns below are what I've picked up from building small monitoring jobs and reading through Evidently's docs. They are not full observability stacks — just the patterns I'd reach for first when wiring drift checks into a pipeline.

## Key patterns

**Baseline snapshots**
Save a reference dataset at training time — the exact feature values the model saw during validation. This becomes your comparison point. Every drift check compares the current batch against this frozen baseline, not against the previous day's data. That way you catch cumulative drift, not just day-to-day noise.

**Scheduled batch checks**
Run drift detection on a rolling window (e.g., every 24 hours on the last 7 days of predictions). A scheduled job is simpler than a real-time stream and good enough for most batch-prediction use cases. The job outputs a pass/fail result and writes metrics to a log or dashboard.

**Threshold-based alerting**
Set drift thresholds per feature. A common approach: use the Kolmogorov-Smirnov test with a p-value cutoff (e.g., p < 0.05), or compute Population Stability Index (PSI) where PSI > 0.2 signals meaningful drift. Only alert when the threshold is crossed — raw drift scores without thresholds generate noise.

**Retraining trigger**
Wire the drift check result into your pipeline orchestrator. When drift exceeds the threshold, trigger a retraining pipeline run. Metaflow, Kubeflow, and Airflow all support event-based or scheduled triggers. The monitoring job becomes the input that decides when the next training run kicks off.

**Drift report archive**
Persist every drift report (HTML or JSON) with a timestamp and the dataset hash that was checked. Over time this archive becomes your evidence for when drift started and how fast it progressed. It is also what you hand to a stakeholder when they ask "why did we retrain last month?"

## A concrete pattern

The flow I use looks like this:

1. At training time, save `reference_data.parquet` alongside the trained model.
2. A daily job loads the last 24 hours of live features into `current_data.parquet`.
3. The job runs a drift test (KS test per feature) against the reference.
4. If any feature crosses the threshold, the job writes a drift alert and triggers a retraining pipeline.
5. Every report is saved to a `drift_reports/` directory with the run date in the filename.

## How this connects to what's next

I want to wire this into Evidently for richer test suites (null checks, value ranges, prediction drift alongside feature drift) and pipe the metrics into Prometheus so drift shows up on a real dashboard. After that I want to see how pipeline orchestration tools like Metaflow or Kubeflow handle the retraining trigger when drift is detected.
