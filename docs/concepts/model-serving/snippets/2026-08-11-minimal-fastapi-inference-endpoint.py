# last_verified: 2026-08-11 · n/a

"""
Practice: deploy a minimal FastAPI inference endpoint.

I wrote this to see the smallest thing that counts as "serving a model" —
a trained classifier loaded from disk, wrapped in a REST API with two
routes: /health so a load balancer can probe it, and /predict that turns
JSON in / JSON out.
"""

import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# A dummy model so the snippet runs anywhere. Swap for your own:
#   model = joblib.load("my_trained_model.joblib")
class DummyModel:
    def predict(self, X):
        return X.sum(axis=1, keepdims=True) * 0.5


model = DummyModel()

app = FastAPI(title="minimal-inference")


class PredictRequest(BaseModel):
    features: list[float]


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/predict")
async def predict(req: PredictRequest):
    if len(req.features) == 0:
        raise HTTPException(status_code=422, detail="need at least one feature")
    X = np.array(req.features, dtype=float).reshape(1, -1)
    result = model.predict(X)[0][0]
    return {"prediction": float(result)}