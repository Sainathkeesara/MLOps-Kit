---
last_verified: 2026-07-27
tool_version: n/a
---

# Feast — quick primer

> First-day notes for someone who's never used Feast. Personal voice, plain language.

## What is it?

Feast is an open-source feature store for ML. It lets you define, store, and retrieve features for training and serving in one place.

## What does it do?

Feast lets you register a feature repository, point it at data sources like Parquet files, and pull feature values for training or serving. I installed Feast with `pip install feast`, initialized a repo, and pulled historical features into a training dataframe in a few lines of Python.

## Why does it exist?

Before Feast, teams wrote feature logic in notebooks for training then mirrored it in serving code. It drifted. Feast keeps definitions in one place.

## Key terminology

- **Feature** — An input variable to a model. Example: `user_age`.
- **Feature View** — A named group of features from a data store. Example: a view reading from BigQuery.
- **Entity** — The identifier for feature lookup. Example: `user_id`.
- **Offline Store** — Historical features for training (BigQuery, Snowflake).
- **Online Store** — Latest features for real-time serving (Redis, DynamoDB).
- **Feature Service** — An API endpoint serving online features for inference.

## A tiny example

```python
import feast

store = feast.FeatureStore(repo_path=".")

training_df = store.get_historical_features(
    entity_df=pd.DataFrame({"user_id": [1, 2, 3]}),
    features=["user_features:age", "user_features:account_status"],
).to_df()
```

This fetches historical features for three users and returns a dataframe ready for training.

## What I'll cover next

After this primer I'll define my first feature view, register it with Feast, and verify both offline and online serving work.