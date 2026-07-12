# last_verified: 2026-07-12 · n/a

"""
Practice: writing features to an online feature store and reading them
with a point-in-time join query.

I used Feast's local (SQLite) online store so I could iterate without a
remote Redis or DynamoDB.  The point-in-time join is the key idea that
separates a feature store from a plain key-value table.
"""

import datetime
import pandas as pd
from feast import FeatureStore, Entity, FeatureView, Field, ValueType
from feast.infra.offline_stores.file_source import FileSource
from feast.types import Float32, Int64

# ── 1. Define a dummy data source ──────────────────────────────────────
# In real usage this would point at Parquet files in S3/GCS.
driver_hourly_stats = pd.DataFrame(
    {
        "driver_id": [1001, 1002, 1003],
        "avg_daily_trips": [12, 8, 15],
        "avg_rating": [4.7, 4.2, 4.9],
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
    }
)

# Save as Parquet so Feast can read it.
driver_hourly_stats.to_parquet("driver_stats.parquet")

# ── 2. Define the feature view ─────────────────────────────────────────
driver = Entity(name="driver", value_type=ValueType.INT64, join_keys=["driver_id"])

driver_stats_source = FileSource(
    path="driver_stats.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created",
)

driver_hourly_stats_view = FeatureView(
    name="driver_hourly_stats",
    entities=[driver],
    ttl=datetime.timedelta(days=1),
    schema=[
        Field(name="avg_daily_trips", dtype=Float32),
        Field(name="avg_rating", dtype=Float32),
    ],
    source=driver_stats_source,
)

# ── 3. Apply to the local (SQLite) online store ─────────────────────────
fs = FeatureStore(repo_path=".")
fs.apply([driver, driver_hourly_stats_view])
fs.materialize(
    start_date=datetime.datetime(2026, 7, 1),
    end_date=datetime.datetime(2026, 7, 2),
)

# ── 4. Point-in-time online read ───────────────────────────────────────
# The key: I pass the *entity ID* and a *timestamp* so Feast returns the
# latest feature row that existed *at or before* that timestamp.
feature_vector = fs.get_online_features(
    features=["driver_hourly_stats:avg_rating"],
    entity_rows=[{"driver_id": 1001, "event_timestamp": datetime.datetime(2026, 7, 1, 11, 0, 0)}],
).to_dict()

print("Online features:", feature_vector)
# → {'driver_id': [1001], 'avg_rating': [4.7]}
