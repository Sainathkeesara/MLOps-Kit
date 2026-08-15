---
last_verified: 2026-08-15
tool_version: n/a
---

# Comparing online vs offline feature serving with Feast

> Third-person overview of when to use online versus offline feature retrieval and how each mode fits into an ML workflow.

## Purpose

Feast exposes features through two retrieval modes: offline serving for training and online serving for inference. Choosing the right mode depends on whether the consumer needs historical context or low-latency, point-in-time values.

## Offline serving

Offline serving reads from batch data sources such as Parquet files, BigQuery, or Snowflake. It returns a dataframe of historical feature values aligned to an entity dataframe, making it the natural choice for training pipelines. The typical flow is:

1. Define entities and feature views in a feature repository.
2. Materialize features from the offline store into the online store.
3. Pull historical features with `get_historical_features()` and join them to training labels.

Offline serving is tolerant of latency because training jobs run asynchronously and can process large entity windows.

## Online serving

Online serving reads from a low-latency store such as Redis or SQLite. It returns the latest feature value for each entity key at serving time, which is what a model endpoint needs during inference. The typical flow is:

1. Materialize features from the offline store into the online store.
2. Call `get_online_features()` with entity rows and a feature list.
3. Return the result to the inference service.

Online serving requires that the online store is kept up to date. If materialization lags, inference requests read stale values.

## When to use which

Use offline serving when building training datasets, evaluating feature importance, or backfilling predictions. Use online serving when the model needs real-time feature values at request time, such as in a REST API or streaming pipeline.

## Verification

Confirm offline serving by printing a dataframe returned from `get_historical_features()` and checking row counts match the input entity dataframe. Confirm online serving by inspecting the dictionary returned from `get_online_features()` and verifying each entity key has the expected feature keys.

## Common errors

- **Registry path mismatch:** running `feast apply` from the wrong directory writes to a different `registry.db`, causing "no feature views found" errors.
- **Missing materialization:** online serving returns stale or empty values if `feast materialize` has not been run after feature view updates.
- **Timestamp field mismatch:** if `timestamp_field` on a `FileSource` does not match the actual column name, Feast silently ignores the feature data during historical retrieval.
