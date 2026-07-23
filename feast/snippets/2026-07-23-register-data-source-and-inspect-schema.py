# last_verified: 2026-07-23

from feast import FeatureStore, FileSource

src = FileSource(path="data/daily_metrics.parquet", timestamp_field="event_timestamp")
store = FeatureStore(repo_path=".")
store.apply([src])

ds = store.get_data_source("daily_metrics_source")
print(ds.to_dict())
