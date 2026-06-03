from datetime import timedelta
import pandas as pd
from feast import Entity, FeatureView, FileSource, FeatureStore

driver = Entity(name="driver_id", value_type="INT64", description="driver id")

source = FileSource(
    path="data/driver_stats.parquet",
    timestamp_field="event_timestamp",
)

# TODO: not sure why I need to set ttl=timedelta here but it errors without it
fv = FeatureView(
    name="driver_hourly_stats",
    entities=[driver],
    ttl=timedelta(days=1),
    source=source,
)

store = FeatureStore(repo_path=".")
store.apply([driver, fv])

entity_df = pd.DataFrame({"driver_id": [1001, 1002]})
features = store.get_historical_features(
    entity_df=entity_df,
    features=["driver_hourly_stats:conv_rate", "driver_hourly_stats:avg_daily_trips"],
).to_df()
print(features)
