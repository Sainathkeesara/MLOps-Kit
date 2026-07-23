---
last_verified: 2026-07-22
tool_version: "n/a"
sources:
  - https://github.com/feast-dev/feast/issues/6295
  - https://docs.feast.dev/getting-started/quickstart
---

# Feast — install, configure a Parquet offline store, and query my first feature vector

I installed Feast today using `pip install feast`. Straightforward — no surprises.

I wanted to go beyond the default `feast init` scaffold though. The quickstart gives you SQLite for both registry and online store, but I wanted to point the offline store at a real Parquet file so I could see how Feast reads historical data.

The thing that tripped me up right away: `feast init` clones a demo repo via `git clone`. If `git` isn't installed, the command exits silently and `feast apply` later fails with `Can't find feature repo configuration file` because the expected directory was never created. I already had git, but I can see how that would stump someone in a minimal container.

Here's what I did:

1. Created a feature repo directory and `cd` into it.
2. Defined an entity (`driver_id`) and a feature view (`driver_hourly_stats`) pointing to a Parquet file via `FileSource(path="data/driver_stats.parquet")`.
3. Set `offline_store` and `online_store` in `feature_store.yaml`. For local dev I pointed offline at a local path.
4. Ran `feast apply` to register everything with the local registry.
5. Ran `feast materialize-incremental <timestamp>` to push the latest features to the online store.
6. Pulled my first feature vector:

```python
import pandas as pd
from feast import FeatureStore

store = FeatureStore(repo_path=".")
entity_df = pd.DataFrame({"driver_id": [1001, 1002, 1003]})
training_df = store.get_historical_features(
    entity_df=entity_df,
    features=["driver_hourly_stats:conv_rate", "driver_hourly_stats:avg_daily_trips"],
).to_df()
print(training_df)
```

Got stuck on: the `feast apply` step failed the first time because my `feature_store.yaml` was using a provider name that didn't match Feast's config schema. Fixed by explicitly setting `offline_store` and `online_store` with valid type names, and leaving `provider` unset so Feast picks up the defaults.

## What I'd try next

I want to define my own Entity and FeatureView without the scaffold, call `get_historical_features()` programmatically, and then swap in a remote online store to see what breaks.