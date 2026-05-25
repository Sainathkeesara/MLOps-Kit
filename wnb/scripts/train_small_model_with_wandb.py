"""wnb-003 — Train a tiny model with W&B metric tracking enabled.

Trains a logistic regression on synthetic data and logs
loss + accuracy per epoch to W&B.
"""

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
print("Done! Check your W&B dashboard.")
