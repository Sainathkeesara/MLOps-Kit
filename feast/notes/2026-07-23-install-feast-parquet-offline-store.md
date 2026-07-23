---
last_verified: 2026-07-23
tool_version: n/a
sources:
  - https://github.com/feast-dev/feast/issues/6295
  - https://docs.feast.dev/getting-started/quickstart
  - https://dibi8.com/resources/data-science/feast-feature-store-ml/
---

# Feast — setup with a Parquet offline store

Installed Feast with `pip install feast` into a fresh virtualenv. No issues on Python 3.11.

Ran `feast init product_features` to get the scaffold. That built the expected `feature_store.yaml`, `repo.py`, and a `data/` directory. I noticed the sample feature view in the scaffold reads from a Parquet file, which is exactly the offline-store pattern I wanted to practice.

I created my own `product_sales.parquet` instead of using the demo data:

```python
import pandas as pd
pd.DataFrame({
    "product_id": [101, 102, 103],
    "category": ["electronics", "groceries", "electronics"],
    "return_rate": [0.02, 0.08, 0.05]
}).to_parquet("data/product_sales.parquet")
```

Then I edited `repo.py` to point the `product_sales` feature view at that file. After `feast apply` registered everything, I queried the offline store with `get_historical_features`:

```python
features = store.get_historical_features(
    entity_df=pd.DataFrame({"product_id": [101, 102]}),
    features=["product_sales:category", "product_sales:return_rate"]
).to_df()
print(features)
```

Pulled "electronics" and the 0.02 return rate back for `product_id=101`.

What tripped me up: I renamed the feature view but forgot to update the feature list in the Python query. `feast apply` passed, but the retrieval raised a `FeatureViewNotFoundException` until the names matched.
