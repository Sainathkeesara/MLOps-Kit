# last_verified: 2026-08-11 · Monitoring & Drift concept

# I wrote this script to practice data drift detection the way I'd wire it
# into a scheduled monitoring job. It uses numpy to generate a reference
# dataset (my training baseline) and a simulated current dataset with a bit
# of shift baked in, then checks each feature with a simple z-score approach.

import numpy as np

np.random.seed(42)
reference = np.random.randn(500, 4)
current = np.random.randn(500, 4) + np.array([0.3, -0.2, 0.1, -0.15])

drift_threshold = 2.0

for i in range(4):
    ref_mean = reference[:, i].mean()
    ref_std = reference[:, i].std()
    cur_mean = current[:, i].mean()
    z_score = abs(cur_mean - ref_mean) / ref_std
    drifted = z_score > drift_threshold
    print(f"Feature {i}: ref_mean={ref_mean:.3f}, cur_mean={cur_mean:.3f}, "
          f"z_score={z_score:.3f}, drifted={drifted}")
