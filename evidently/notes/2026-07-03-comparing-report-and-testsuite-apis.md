# What I learned comparing Report and TestSuite APIs in Evidently

Evidently ships two main ways to run drift checks: the `Report` class and the `TestSuite` class. I set up both and ran them against the same reference and current datasets to see what felt different in practice.

## Report API: the visual-first path

I started with the Report API because the docs lead with it.

```python
from evidently.report import Report
from evidently.metric_presets import DataDriftPreset

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=ref, current_data=curr)
report.save_html("drift_report.html")
```

The output is a self-contained HTML file with histograms per feature, drift scores, and a summary table. It's good for sharing with stakeholders or reviewing interactively. The API is simple: build a Report with metric presets or individual metrics, run it, save it. The downside is the output is meant for human eyes — there's no structured pass/fail result you can act on in code or a CI gate. If I want to fail a build when a feature drifts, the Report alone doesn't give me that cleanly.

## TestSuite API: the programmatic path

The TestSuite is the answer to "I want results I can check in a script."

```python
from evidently.test_suite import TestSuite
from evidently.test_preset import DataDriftTestPreset

suite = TestSuite(tests=[DataDriftTestPreset()])
suite.run(reference_data=ref, current_data=curr)
suite.save_html("drift_tests.html")

for result in suite.as_dict()["tests"]:
    status = result["status"]
    name = result["name"]
    print(f"{status.upper()}: {name}")
```

The TestSuite runs the same statistical tests under the hood but wraps each one as a test with a `SUCCESS` or `FAIL` status. The `as_dict()` call gives me structured results I can parse in a CI job — fail the build, send an alert, open a ticket. You can also add custom thresholds per feature if you want tighter control on high-stakes columns.

## When to use which

I'd reach for Report when I'm exploring a new dataset or preparing a drift analysis for a human reviewer. I'd reach for TestSuite when I'm wiring this into a CI pipeline, a scheduled monitoring job, or any place where I need the code to make a binary decision (deploy / don't deploy).

The two APIs aren't mutually exclusive — a TestSuite can also render HTML, so you get both the structured result and a human-readable report from the same run.

## What tripped me up

The import path changed between Evidently 0.3.x and 0.4.x. In 0.3.x you'd use `from evidently.tests import *`, in 0.4.x it moved to `from evidently.test_suite import TestSuite` and `from evidently.test_preset import DataDriftTestPreset`. I wasted ten minutes chasing a stale tutorial that used the old import path. Pin your version in `requirements.txt`.
