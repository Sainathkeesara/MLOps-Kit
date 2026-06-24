# Feature Store — quick primer

> First-day notes on Feature Store. What it is, why it matters, and the key ideas to know.

## What is it?

A feature store is a centralized system for storing, computing, and serving ML features. Think of it as a shared library of precomputed columns that both your training pipelines and online models can use. Instead of manually joining tables in SQL for every experiment or rewriting preprocessing logic in both batch and real-time contexts, the feature store gives you a single source of truth for features.

Before feature stores, I'd copy-paste pandas transforms between notebooks, or write separate Spark jobs for batch features and REST endpoints for online features. Feature stores connect these worlds: train on historical features from the same place your model serves live features.

## Why does it matter for MLOps?

Training-serving skew is a constant headache. Your model trains on clean, historical data but gets garbage in production because the timestamp logic differs or a data source was temporarily offline. Feature stores solve this by:
- Ensuring training and inference use identical feature logic.
- Versioning features so you can reproduce a training run from months ago.
- Serving features at low latency for real-time predictions.
- Sharing features across teams so data scientists aren't reinventing the same column.

Every serious ML platform eventually builds one because you can't scale feature engineering without it.

## Key terminology

- **Feature** — An individual input variable used by a model. Example: `user_age_days_since_last_login` or `transaction_amount_usd`.
- **Feature view** — A logical grouping of features, similar to a table. Example: a `user_profile` view containing 15 user-related features.
- **Offline store** — The historical feature data used for training (usually a data warehouse). Example: a Spark table with daily snapshots.
- **Online store** — Low-latency feature data for real-time inference. Example: Redis or DynamoDB storing latest user state.
- **Feature computation** — The transform logic that creates a feature. Example: a SQL query or pandas function.
- **Feature materialization** — The process of populating the online store from batch sources. Example: nightly Spark job pushes user aggregates to Redis.
- **Point-in-time join** — Correctly stitching features to avoid future leakage during training. Example: joining only features available before a prediction timestamp.
- **Feature consistency** — Ensuring the same feature values used in training are available at inference time.
- **TTL (time-to-live)** — How long a feature value stays fresh in the online store. Example: user login count TTL of 1 hour.

## A concrete example

```python
# Conceptual feature store workflow
# Step 1: Define feature in batch
FEATURES = [
    {"name": "user_transaction_count_7d", "sql": "SELECT COUNT(*) FROM transactions WHERE user_id = ? AND ts > NOW() - INTERVAL '7 days'"}
]

# Step 2: Train using offline store
training_df = feature_store.get_batch_features(
    feature_refs=["user:transaction_count_7d"],
    timestamp_column="prediction_time"
)

# Step 3: Serve online
live_features = feature_store.get_online_features(
    feature_refs=["user:transaction_count_7d"],
    entity_values={"user_id": 12345}
)
```

This shows how the same feature reference works in both contexts — one for batch training, one for online inference.

## How this connects to what's next

Feature stores build on data versioning (features version with their sources) and feed into model serving (live features are the model's input). After this, I want to try Feast to see how their feature views and transformations map to this mental model.