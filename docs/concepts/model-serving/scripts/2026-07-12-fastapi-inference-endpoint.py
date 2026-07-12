# last_verified: 2026-07-12 · n/a

"""
Deploy a FastAPI inference endpoint with batching, caching, and health
checks.

I built this to practice the pattern for serving an sklearn model behind
a REST API that production clients can actually rely on — not just a
single /predict route.
"""

import asyncio
import json
import time
from functools import lru_cache

import numpy as np
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI(title="ml-inference")

# ── Dummy model (replace with pickle.load / joblib.load) ───────────────
class DummyModel:
    def predict(self, X: np.ndarray) -> np.ndarray:
        return X.sum(axis=1, keepdims=True) * 0.5

model = DummyModel()

# ── Request / response schemas ─────────────────────────────────────────
class PredictRequest(BaseModel):
    instances: list[list[float]]

class PredictResponse(BaseModel):
    predictions: list[float]
    model: str

# ── Health check (Kubernetes probes need this) ─────────────────────────
@app.get("/health")
async def health():
    return {"status": "ok"}

# ── Simple in-memory response cache ────────────────────────────────────
# LRU cache avoids recomputing for identical requests within the window.
cache_ttl = 60  # seconds

@lru_cache(maxsize=128)
def _cached_predict(input_hash: str, ts_bucket: int) -> list[float]:
    """Cache keyed on input hash + 60-second time bucket."""
    data = json.loads(input_hash)
    preds = model.predict(np.array(data)).flatten().tolist()
    return preds

# ── Inference endpoint ─────────────────────────────────────────────────
@app.post("/predict", response_model=PredictResponse)
async def predict(req: PredictRequest, request: Request):
    # simple request ID for tracing
    req_id = request.headers.get("X-Request-ID", "none")

    # batch the inputs
    batch = np.array(req.instances)
    print(f"[{req_id}] received batch of shape {batch.shape}")

    # ── Batching: chunk into groups of 32 and run sequentially ─────
    # This keeps memory predictable when clients send 10k rows at once.
    all_preds: list[float] = []
    chunk_size = 32
    for start in range(0, len(batch), chunk_size):
        chunk = batch[start : start + chunk_size]
        # cache lookup
        data_hash = json.dumps(chunk.tolist(), sort_keys=True)
        ts_bucket = int(time.time() // cache_ttl)
        preds = _cached_predict(data_hash, ts_bucket)
        all_preds.extend(preds)
        # yield control so other requests aren't starved
        await asyncio.sleep(0)

    return PredictResponse(predictions=all_preds, model="dummy-v1")

# ── Startup / shutdown hooks ───────────────────────────────────────────
@app.on_event("startup")
async def startup():
    print("inference server starting")

@app.on_event("shutdown")
async def shutdown():
    print("inference server shutting down")
