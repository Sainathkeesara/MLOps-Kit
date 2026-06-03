# Feast — install and first feature retrieval

I installed Feast with `pip install feast` into a fresh virtualenv. Worked fine — no surprises.

Followed the quickstart in the docs. The idea is: define a feature view, apply it to a local SQLite store, then pull features back out for training.

I started with `feast init my_feast_repo` to get a scaffold. That created a directory with `feature_store.yaml`, `example_repo.py`, and a `data/` folder.

The main thing I had to understand was the object model:

- **Entity** — the key (e.g. `driver_id`)
- **Feature View** — a group of features + their data source
- **Feature Service** — a named group of feature views for serving

I edited `example_repo.py` to define a simple entity and feature view pointing at the sample parquet file in `data/`. Then ran `feast apply` to register everything with the local registry.

Getting features back was straightforward:

```python
import pandas as pd
from feast import FeatureStore

store = FeatureStore(repo_path=".")
entity_df = pd.DataFrame({"driver_id": [1001, 1002, 1003]})
features = store.get_historical_features(
    entity_df=entity_df,
    features=["driver_hourly_stats:conv_rate"]
).to_df()
print(features)
```

Got stuck on: the `feast apply` step failed at first because my `feature_store.yaml` pointed at a remote store path. Fixed by setting `registry: "data/registry.db"` for local dev.

## What I'd try next

Next I want to define my own feature view from scratch — not just edit the example file — and understand how offline vs online serving works differently.
