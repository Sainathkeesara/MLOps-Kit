# Feast — quick primer

> First-day notes for someone who's never used Feast. Personal voice, plain language.

## What is it?

Feast (Feature Store) is an open-source tool that makes it easy to manage and serve features for machine learning models. Think of it as a centralized place to store, compute, and retrieve features — the input variables you actually train your models on. If you've ever dealt with "training-serving skew" where your model works in training but differently in production, Feast was built to solve that.

## What does it do?

Feast lets you define features once (as "feature views"), compute them from batch or streaming sources, and then fetch those features consistently for both training and inference with a simple Python API. No more rewriting SQL queries in different places or wondering if you're using the same logic for features in training versus production.

## Why does it exist?

Before feature stores, teams would write feature logic in notebooks for training, copy-paste it into different services for online inference, and inevitably drift. Features would change slightly between environments. Feast emerged from the need to have a single source of truth for features, making the same feature definitions reusable across training pipelines and production services.

## Key terminology

- **Feature** — An individual input variable to a model. Example: `user_age` or `transaction_count_last_7_days`.
- **Feature View** — A defined feature or group of features with their source and transformation logic. Example: a view that reads from PostgreSQL and computes rolling averages.
- **Entity** — The primary key or identifier for a feature. Example: `user_id` or `product_id`.
- **Feature Service** — The deployed server that serves features for online inference. Example: query `user_id=123` and get all online features back.
- **Offline Store** — Where historical features are stored (typically a data warehouse like BigQuery or Snowflake). Used for training.
- **Online Store** — Where the latest features live for real-time inference (typically Redis or DynamoDB).
- **Feature Registry** — The central metadata store that tracks all feature definitions.

## A tiny example

```python
import feast

store = feast.FeatureStore(repo_path=".")

# Fetch features for training
entity_df = pd.DataFrame({"user_id": [1, 2, 3]})
training_features = store.get_historical_features(
    entity_df=entity_df,
    features=["user_features:age", "user_features:account_status"]
).to_df()
```

This reads historical features from the offline store and returns them as a dataframe ready for model training.

## What I'll cover next

After this primer I want to install Feast with a local SQLite offline store, define my first feature view on some sample data, and pull features into a training dataframe to verify the whole flow works end to end.