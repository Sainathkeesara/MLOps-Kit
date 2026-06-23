# Evidently AI — quick primer

> First-day notes for someone who's never used Evidently AI. Personal voice, plain language.

## What is it?

Evidently AI is an open-source Python library for checking whether your ML model's data or predictions are drifting over time. Think of it like a health monitor for your model in production: you feed it recent data, and it tells you whether things still look like they did during training. It's not a full monitoring platform — it's a toolkit that produces reports and test suites you can run in a notebook, a CI pipeline, or a scheduled job.

I've heard people compare it to Great Expectations, but focused specifically on drift and performance rather than general data validation. It works with tabular data, text, and embeddings, though the tabular drift detection is the most mature part.

## What does it do?

You point it at two datasets — a reference (usually your training data) and a current batch — and it computes statistical tests to see if the distributions have drifted. It can also detect target drift, prediction drift, and data quality issues. The output is a self-contained HTML report or a structured JSON result that you can plug into dashboards or alerting.

## Why does it exist?

Before tools like Evidently, I'd have to write custom scripts comparing histograms or KS-test p-values and email myself PDFs. That gets old fast when you have dozens of models. Evidently exists because ML teams need a repeatable way to answer one question: "did my data change since I trained this model?" — without building a bespoke monitoring stack from scratch. It's used by data scientists and ML engineers who need drift checks in notebooks and CI, not necessarily a full Prometheus/Grafana setup.

## Key terminology

- **Data drift** — When the distribution of input features in production differs from the training set. Example: age distribution shifts from 25–45 to 18–65 after a new marketing campaign.
- **Target drift** — When the distribution of the target variable changes. Example: fraud rate jumps from 2% to 8% after a policy change.
- **Reference dataset** — The baseline data you compare against, usually the training or validation set.
- **Current dataset** — The new data you're checking for drift.
- **Test Suite** — A structured set of checks with pass/fail conditions, rendered as HTML or JSON. Example: a suite that runs 5 drift tests and 3 data quality tests.
- **Report** — A richer visual output with distributions, metrics, and descriptions. Good for sharing with stakeholders.
- **Drift detection method** — The statistical test used (PSI, KS-test, Wasserstein distance, etc.). Different methods catch different kinds of drift.
- **Data Quality** — Checks for missing values, duplicates, and type mismatches, separate from drift.
- **Integration** — Evidently can push metrics to Prometheus, Grafana, or Weights & Biases so drift is visible in existing dashboards.
- **Profile** — The computed summary of a dataset (means, quantiles, type info) that powers drift detection.

## A tiny example

```python
import pandas as pd
from evidently.report import Report
from evidently.metric_presets import DataDriftPreset

ref = pd.read_csv("train.csv")
curr = pd.read_csv("prod_batch.csv")

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=ref, current_data=curr)
report.save_html("drift_report.html")
```

This loads a reference and current dataset, runs a drift check, and saves an HTML report. Open the file in a browser to see feature-by-feature drift scores.

## What I'll cover next

I want to dig into the Test Suite for structured pass/fail results and figure out how to pipe metrics into Prometheus so drift shows up on a real dashboard. I also want to understand which drift detection methods make sense for different feature types.
