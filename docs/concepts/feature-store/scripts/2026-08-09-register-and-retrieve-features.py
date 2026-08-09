# last_verified: 2026-08-09 · feast 0.65.0

"""
Practice: register features in a local Feast store, then retrieve them
as a historical training set and as live online features.

I'm using the local provider (SQLite) so this runs without any remote
registry or Redis. The workflow: define schema -> apply (register) ->
materialize -> get_historical_features / get_online_features.
"""

import datetime
import os

import pandas as pd
from feast import FeatureStore, Entity, FeatureView, Field, ValueType
from feast.infra.offline_stores.file_source import FileSource
from feast.types import Float32, Int64

# ── 1. Dummy data ────────────────────────────────────────────────────────
# In real life this lives in a data warehouse or S3 Parquet.
STATS = pd.DataFrame({
    "driver_id": [1001, 1002, 1003],
    "rating": [4.7, 4.2, 4.9],
    "trips": [12, 8, 15],
    "event_timestamp": [
        datetime.datetime(2026, 7, 1, 10, 0, 0),
        datetime.datetime(2026, 7, 1, 10, 0, 0),
        datetime.datetime(2026, 7, 1, 10, 0, 0),
    ],
    "created": [
        datetime.datetime(2026, 7, 1, 10, 0, 0),
        datetime.datetime(2026, 7, 1, 10, 0, 0),
        datetime.datetime(2026, 7, 1, 10, 0, 0),
    ],
})

os.makedirs("data", exist_ok=True)
STATS.to_parquet("data/driver_stats.parquet")

# ── 2. Register the feature view ─────────────────────────────────────────
# apply() writes the entity/feature-view definitions into the registry DB.
driver = Entity(name="driver", value_type=ValueType.INT64, join_keys=["driver_id"])

source = FileSource(
    path="data/driver_stats.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created",
)

driver_stats = FeatureView(
    name="driver_stats",
    entities=[driver],
    ttl=datetime.timedelta(days=1),
    schema=[
        Field(name="rating", dtype=Float32),
        Field(name="trips", dtype=Int64),
    ],
    source=source,
)

store = FeatureStore(repo_path=".")
store.apply([driver, driver_stats])

# ── 3. Materialize offline -> online ─────────────────────────────────────
# Without this, get_online_features() returns empty rows because nothing
# has been pushed from Parquet into SQLite yet.
store.materialize(
    start_date=datetime.datetime(2026, 7, 1),
    end_date=datetime.datetime(2026, 7, 2),
)

# ── 4. Retrieve features ─────────────────────────────────────────────────
# Historical: point-in-time join against the offline Parquet source.
hist = store.get_historical_features(
    entity_df=pd.DataFrame({
        "driver_id": [1001, 1002],
        "event_timestamp": [
            datetime.datetime(2026, 7, 1, 11, 0, 0),
            datetime.datetime(2026, 7, 1, 11, 0, 0),
        ],
    }),
    features=["driver_stats:rating", "driver_stats:trips"],
).to_df()

print("Historical features:")
print(hist)

# Online: low-latency lookup from the SQLite online store.
online = store.get_online_features(
    features=["driver_stats:rating", "driver_stats:trips"],
    entity_rows=[{"driver_id": 1001}],
).to_dict()

print("Online features:")
print(online)
