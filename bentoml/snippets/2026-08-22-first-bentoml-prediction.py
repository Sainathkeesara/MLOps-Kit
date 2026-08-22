# last_verified: 2026-08-22 · BentoML 1.4.39

import numpy as np
from bentoml import models

# Load a saved model — BentoML stores models by name + tag
# This assumes you've already saved one with `bentoml.sklearn.save_model("iris", clf)`
# TODO: swap the tag for whatever you saved locally
model_ref = models.get("iris:latest")
model = model_ref.load_model()

# Run a prediction — just pass in a numpy array
sample = np.array([[5.1, 3.5, 1.4, 0.2]])
prediction = model.predict(sample)

print("Prediction:", prediction)
