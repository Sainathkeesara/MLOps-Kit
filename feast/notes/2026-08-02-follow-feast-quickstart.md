---
last_verified: 2026-08-02
tool_version: n/a
---

# Feast — follow the quickstart and document what tripped me up

> Following the official Feast quickstart, here's what worked and where I got stuck.

## What I did

I started by installing Feast with `pip install feast` and running `feast init my_repo` to scaffold a new project. The command created a directory with a `feature_store.yaml`, a `data/` folder with sample Parquet files, and a `registry/` directory. I followed the quickstart to define an entity and a feature view, then tried to materialize the features into the online store.

The first thing that tripped me up was the `feature_store.yaml` configuration. The quickstart uses `provider: local`, which is fine for experimentation, but I didn't realize it defaults the registry path relative to where I ran the command from. When I ran `feast apply` from a different directory than the repo root, it created a new registry file instead of using the existing one, and my feature views didn't show up.

## What worked

Defining entities and feature views with the Python SDK was straightforward. I used `FileSource` to point at the sample Parquet files and created a `FeatureView` with a TTL. Running `feast apply` registered everything correctly once I was in the right directory. Pulling historical features with `store.get_historical_features()` returned a clean dataframe ready for training.

## What tripped me up

The registry path issue was the main gotcha. I kept getting "no feature views found" errors until I realized `feast apply` was writing to a different `registry.db` than the one my `FeatureStore` was reading from. The fix was to always run Feast commands from the repo root or set `FEAST_REPO_PATH` explicitly.

Another thing that caught me out: the sample Parquet files use a timestamp column, but I didn't set the `timestamp_field` correctly on the `FileSource`. Feast silently ignored the feature data until I fixed the column name to match what was actually in the file.

## What I'd try next

I want to try pulling features for online serving with `store.get_online_features()` and then swap the local provider for a Redis online store to see how the configuration changes. I'd also like to experiment with multiple feature views sharing the same entity to understand how Feast joins them during retrieval.