---
last_verified: 2026-08-10
tool_version: n/a
sources: []
---

# Automated vs manual model promotion

> A comparison of two strategies for moving model versions through the
> registry. Automated promotion is the direction most teams migrate toward,
> but manual review still has a place for high-stakes or low-frequency
> models.

## Purpose

Once a model is registered, it has to move from a staging area to a serving
state. The question is: who decides when that move happens, and how? This
document compares the two main approaches so a team can pick the one that
matches their deployment cadence and risk tolerance. One caveat: the
"right" choice is not static — most teams start manual and add automation
as they mature.

## Automated promotion

An automated pipeline evaluates the candidate model and promotes it without
human intervention.

### How it works

1. A training job finishes and logs the model to the registry.
2. The pipeline loads the staging version and evaluates it on a held-out
   validation set, producing one or more metric scores.
3. If the score clears a configurable threshold, the pipeline calls the
   registry API to transition the version to the serving state.
4. If the threshold is not met, the run fails and the version stays in
   staging.

This is the pattern implemented in
[automated-model-promotion-workflow.py](scripts/automated-model-promotion-workflow.py).

### When it fits

- The model is retrained frequently (daily or more) and the cost of manual
  review outweighs the risk.
- Validation metrics are a reliable proxy for real-world performance.
- The team has invested in a validation suite — metric thresholds, regression
  tests, data-drift checks.

### What to watch

- **Metric gaming**: a threshold that is too lenient can let a subtly
  degraded model through. Teams pair auto-promotion with shadow deployments
  or canary checks for higher-stakes models.
- **Cold start**: the first few promotions may need tuning. Start with a
  conservative threshold and tighten it as data accumulates.

## Manual promotion

A human reviews the candidate and transitions it to the serving state.

### How it works

1. A training job finishes and logs the model to the registry.
2. A reviewer inspects the run metrics, compares against the current
   serving version, and checks validation artifacts (confusion matrices,
   drift reports, etc.).
3. If satisfied, they transition the version to the serving state — either
   through a UI click or a CLI command.

### When it fits

- The model is updated infrequently (weekly or monthly).
- The business impact of a bad promotion is high — a false positive in fraud
  detection, for example — and a human eye is warranted.
- The team does not yet have confidence in its automated validation suite.

### What to watch

- **Bottlenecks**: as deployment frequency grows, manual review becomes a
  constraint.
- **Inconsistency**: different reviewers may apply different standards.
- **Slow feedback**: signals that could block promotion are only noticed
  after a human has already spent time reviewing.

## Comparison

| Aspect | Automated | Manual |
|---|---|---|
| Who decides? | Pipeline + threshold | Human reviewer |
| Review speed | Seconds after training | Hours to days |
| Review depth | Limited to predefined metrics | Can catch subtle, non-metric issues |
| Scalability | High — no human bottleneck | Low — reviewer is the bottleneck |
| Best for | Frequent retraining, low-regret deploys | Infrequent updates, high-stakes decisions |

## Steps to choose

1. **Start where you are**: if deployments are weekly or less and the team
   is small, manual promotion is fine. The overhead of building automated
   gates is not justified yet.
2. **Add automated gates early**: even with manual promotion, run the
   threshold checks as a pre-gate so reviewers only see candidates that pass
   the bar.
3. **Go fully automated** once you have reliable validation metrics and a
   monitoring feedback loop — but keep a manual override for emergencies.

This is one way to structure the decision; some teams also layer a "canary"
step (route 1 % of traffic to the new version) on top of either approach.

## Verify

- **Automated**: the pipeline fails when the staging metric is below the
  threshold, and the version stays in staging. Confirm by checking the
  registry that no new version was promoted to the serving state.
- **Manual**: a human reviewed the run before promotion. Confirm by checking
  the audit log for a comment or approval entry tied to the stage transition.
