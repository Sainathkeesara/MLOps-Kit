import pandas as pd
from evidently.report import Report
from evidently.metric_presets import DataDriftPreset

ref = pd.read_csv("train.csv")
curr = pd.read_csv("production.csv")

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=ref, current_data=curr)
report.save_html("drift_report.html")
print("done")
