"""Reusable Metaflow batch inference flow with configurable parallel splits.

Run locally:
  python batch_inference_splits.py run --input_path data.csv --splits 4 --output_path out

Run on AWS Batch:
  python batch_inference_splits.py run --with batch --input_path s3://bucket/data.csv --splits 16 --output_path out
"""

import json
import os

import joblib
import numpy as np
import pandas as pd
from metaflow import FlowSpec, Parameter, batch, step


def _load_model(model_path):
    if not model_path:
        return None
    return joblib.load(model_path)


def _score_records(records, model_path, threshold):
    frame = pd.DataFrame(records)
    model = _load_model(model_path)

    if model is not None:
        if hasattr(model, "predict_proba"):
            scores = model.predict_proba(frame)[:, 1]
        else:
            scores = model.predict(frame)
    else:
        numeric = frame.select_dtypes(include=[np.number])
        if numeric.empty:
            raise ValueError("No numeric columns found for the built-in scoring fallback")
        scores = numeric.mean(axis=1)

    scores = np.asarray(scores, dtype=float)
    return pd.DataFrame(
        {
            "score": scores,
            "prediction": (scores >= threshold).astype(int),
        }
    )


class BatchInferenceFlow(FlowSpec):
    """Score a CSV file by sharding it into N parallel Metaflow tasks."""

    input_path = Parameter("input_path", help="Path to the input CSV file")
    output_path = Parameter("output_path", default="batch-inference-output", help="Directory for prediction CSVs")
    splits = Parameter("splits", default=4, type=int, help="Number of parallel inference shards")
    threshold = Parameter("threshold", default=0.5, type=float, help="Score threshold for binary predictions")
    model_path = Parameter("model_path", default="", help="Optional joblib model with predict or predict_proba")

    @step
    def start(self):
        frame = pd.read_csv(self.input_path)
        if frame.empty:
            raise ValueError(f"Input file is empty: {self.input_path}")
        if self.splits < 1:
            raise ValueError("splits must be >= 1")

        frame = frame.reset_index(drop=True)
        frame["__row_index"] = frame.index
        shards = []
        for shard_id, shard in enumerate(np.array_split(frame, self.splits)):
            if len(shard) == 0:
                continue
            shards.append(
                {
                    "shard_id": shard_id,
                    "row_indices": shard["__row_index"].tolist(),
                    "rows": shard.drop(columns=["__row_index"]).to_dict(orient="records"),
                }
            )

        self.shards = shards
        self.next(self.score_split, foreach="shards")

    @batch(cpu=2, memory=4096, image="python:3.10")
    @step
    def score_split(self):
        shard = self.input
        predictions = _score_records(shard["rows"], self.model_path, self.threshold)
        predictions.insert(0, "row_index", shard["row_indices"])

        self.part_predictions = predictions
        self.part_count = len(predictions)
        self.next(self.join)

    @step
    def join(self, inputs):
        parts = [input.part_predictions for input in inputs]
        self.predictions = pd.concat(parts, ignore_index=True)
        self.predictions = self.predictions.sort_values("row_index").reset_index(drop=True)

        self.output_file = os.path.join(self.output_path, "predictions.csv")
        self.predictions.to_csv(self.output_file, index=False)
        self.summary = {
            "splits": len(parts),
            "rows": int(len(self.predictions)),
            "output_file": self.output_file,
            "part_counts": [int(input.part_count) for input in inputs],
        }
        print(json.dumps(self.summary, sort_keys=True))


if __name__ == "__main__":
    BatchInferenceFlow().run()
