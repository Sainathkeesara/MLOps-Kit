# Monitoring & Drift — quick primer

> First-day notes on Monitoring & Drift. What it is, why it matters, and the key ideas to know.

## What is it?

Monitoring and drift detection is the practice of watching your ML model in production to ensure it's behaving correctly. Think of it like a smoke detector for your model: you set up tests that check whether input distributions, predictions, or accuracy have shifted significantly since training. When something looks wrong, you get an alert instead of discovering months later that predictions were garbage.

Before dedicated tools, I'd manually compare histograms once a month or wait for a business stakeholder to complain. That's catastrophically late — models can silently degrade for weeks. Drift detection automates this by continuously comparing live data to what the model expects.

## Why does it matter for MLOps?

Models are not "set and forget" — data in the wild changes. Monitoring matters because:
- Feature drift can signal your model sees input it wasn't trained on.
- Prediction drift can catch concept drift before accuracy plummets.
- Data quality issues (missing values, schema changes) break predictions silently.
- Alerts let you trigger retraining before the model fails completely.

Without monitoring, you're flying blind. With it, you can build self-healing pipelines that automatically retrain when drift exceeds thresholds.

## Key terminology

- **Data drift** — When feature distributions in production differ from training data. Example: user ages shift from 25-45 to 18-65 after a marketing campaign.
- **Concept drift** — When the relationship between features and target changes. Example: spending patterns shift during a pandemic.
- **Prediction drift** — When the distribution of model outputs changes unexpectedly. Example: fraud scores suddenly spike across all transactions.
- **Reference data** — The baseline dataset (usually training) to compare against. Example: last week's clean data batch.
- **Current data** — The live data being monitored. Example: today's prediction requests.
- **Drift threshold** — A cutoff for when drift becomes concerning. Example: PSI > 0.2 triggers an alert.
- **PSI (Population Stability Index)** — A statistical measure of distribution shift. Example: PSI of 0.1 is minor, 0.25 is significant.
- **KS test (Kolmogorov-Smirnov)** — A statistical test for comparing distributions. Example: p-value < 0.05 signals drift.
- **Alert** — A notification when drift exceeds the threshold. Example: Slack message or CI pipeline trigger.
- **Window** — The time period over which drift is calculated. Example: rolling 24-hour window.

## A concrete example

```python
# Pseudo-code for drift detection
import evidently
from evidently.monitor import DriftMonitor

monitor = DriftMonitor(
    reference_data=train_df,
    threshold={"psi": 0.2, "ks": 0.05}
)

result = monitor.check(current_data=prod_batch_df)
if result.has_drift:
    send_alert("Feature drift detected!")
    trigger_retraining()
```

This checks incoming data against the training baseline and triggers action if drift exceeds configured thresholds.

## How this connects to what's next

Monitoring plugs into pipeline orchestration (trigger retraining when drift detected) and model serving (wrap drift checks around live endpoints). Next I want to set up Evidently to pipe drift metrics into Prometheus and see how that integrates with real alerting.