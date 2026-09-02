---
last_verified: 2026-09-02
tool_version: n/a
sources: []
---

# Comparing Automated and Manual Model Promotion Strategies

> Two ways to move a model from staging to serving — one driven by pipeline thresholds, the other by human review — and how to choose between them as deployment cadence grows.

## Purpose

Registering a model creates a new version in staging. Promotion is the decision to make that version the serving baseline. This document compares automated promotion, where a pipeline evaluates metrics against a threshold and transitions the stage, with manual promotion, where a reviewer inspects validation artifacts before promoting. It builds on the workflow in `scripts/automated-model-promotion-workflow.py` and offers guidance on when each strategy fits.

## Automated Promotion

### How It Works

1. Training finishes and registers the model as a new version in the registry, initially in staging.
2. A validation job loads the staging version and evaluates it on a held-out set, producing one or more metric scores.
3. A promotion gate compares the scores to a configured threshold (for example, `val_accuracy >= 0.85`).
4. If the gate passes, the pipeline calls the registry API to transition the version to production, optionally archiving the prior production version. If it fails, the version remains in staging and the run is marked accordingly.

This pattern is suited for integration into CI: the threshold check and stage transition run without human intervention.

### When It Fits

- Retraining is frequent (daily or more) and manual review cannot keep pace.
- Validation metrics are a reliable proxy for business outcomes.
- The team has a stable validation set and agreed thresholds that have been tuned over several iterations.

### What to Watch

- A lenient threshold can let a subtly degraded model through. Teams often pair automated promotion with shadow or canary steps that route a small fraction of live traffic to the new version before full promotion.
- Thresholds need tuning. Starting conservative and tightening as confidence grows avoids early false promotions.
- Metrics alone miss qualitative issues — label drift, fairness gaps, or data leakage — that a human might catch.

## Manual Promotion

### How It Works

1. Training finishes and registers the model in staging.
2. A reviewer opens the run in the registry UI, compares metrics to the current production version, and inspects validation artifacts such as confusion matrices, residual plots, or drift reports.
3. If satisfied, the reviewer triggers the stage transition through the UI or CLI. The action is logged for audit.

### When It Fits

- Models update infrequently (weekly or monthly) and each promotion carries significant business risk.
- The validation suite is still maturing and metrics alone are not yet trusted.
- Regulatory or governance requirements demand a human approval step.

### What to Watch

- Review becomes a bottleneck as deployment frequency increases.
- Different reviewers may apply inconsistent standards unless a checklist is shared.
- Feedback is slower: a failing candidate may sit in staging until someone reviews it, delaying the next iteration.

## Comparison

| Aspect | Automated | Manual |
|---|---|---|
| Decision maker | Pipeline + threshold | Human reviewer |
| Review latency | Seconds after validation | Hours to days |
| Depth of review | Limited to predefined metrics | Can catch subtle, non-metric issues |
| Scalability | High — no human bottleneck | Low — reviewer constrained |
| Audit trail | API call with threshold and metric | Approval entry with reviewer identity |
| Best for | Frequent, low-regret updates | Infrequent, high-stakes releases |

## Choosing a Path

A common progression is to start manual and layer automation over time:

1. Begin with manual promotion when deployments are weekly or less. Keep the process lightweight.
2. Add automated gates even while manual review remains: run threshold checks first so reviewers only see candidates that clear the bar.
3. Move to fully automated promotion once thresholds are stable and a monitoring feedback loop confirms that promoted models perform as expected in production. Keep a manual override available for incidents.

Some teams add a canary stage on top of either approach, routing a small percentage of traffic to the new version before completing the promotion.

## Verify

- **Automated**: run the pipeline with a threshold higher than the staging metric and confirm the version stays in staging. Lower the threshold below the metric and confirm the transition to production occurs. The script `scripts/automated-model-promotion-workflow.py` supports both checks via the `--threshold` flag.
- **Manual**: confirm that the registry audit log records who approved the transition and which metric justified it. Without that entry, the promotion lacks traceability.

## Related Material

- `scripts/automated-model-promotion-workflow.py` implements the automated path end-to-end using the MLflow registry client.
- `automated-vs-manual-promotion.md` in this directory covers the same comparison from a lifecycle perspective; this document adds a gate-tuning perspective and explicit verification steps.

