# wnb-004 — Run my first model training experiment with W&B and review the dashboard

Ran a training script with W&B today and actually looked at the dashboard to see what happened.

**what I did**

Used the existing training script I built earlier:

```python
import numpy as np
import wandb
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

wandb.init(project="wnb-demo", name="logreg-synthetic")

X = np.random.randn(200, 5)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(solver="liblinear", max_iter=1, warm_start=True)

for epoch in range(1, 11):
    model.max_iter = epoch
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    wandb.log({"epoch": epoch, "accuracy": acc})

wandb.finish()
```

**what I saw in the dashboard**

- The run appeared immediately under the project with a timestamp
- Accuracy chart showed the curve from 0.5 to ~0.85 over 10 epochs
- The "Charts" tab auto-sorted metrics into time-series plots
- Clicked into the run and saw:
  - Config section with the model params I could have logged
  - The system tab shows CPU/GPU usage (all zeros since this was tiny)
  - Summary tab shows final metric values

**what I noticed**

- Runs update in real-time — I left the dashboard open and watched the curve grow
- The project defaults to "Personal" but I can switch to a team later
- W&B tracked the git hash and Python version automatically — nice for reproducibility
- Hovering over any point on the chart shows the exact metric values at that epoch

**next thing I'll try**

Add logging for the model artifact itself — save the fitted LogisticRegression and attach it to the run.