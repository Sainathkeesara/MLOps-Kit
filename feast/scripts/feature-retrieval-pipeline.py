# last_verified: 2026-08-15 · Feast n/a

import pandas as pd
from datetime import timedelta
from feast import FeatureStore, Entity, FeatureView, FileSource


def build_feature_store(repo_path: str = ".") -> FeatureStore:
    """Initialize a Feast feature store for the given repository path."""
    try:
        store = FeatureStore(repo_path=repo_path)
        return store
    except Exception as e:
        raise RuntimeError(f"Failed to initialize FeatureStore at '{repo_path}': {e}") from e


def register_entities_and_views(store: FeatureStore) -> None:
    """Register an entity and feature view, then apply them to the store."""
    driver = Entity(name="driver_id", value_type="INT64", description="driver identifier")

    source = FileSource(
        path="data/driver_stats.parquet",
        timestamp_field="event_timestamp",
    )

    fv = FeatureView(
        name="driver_hourly_stats",
        entities=[driver],
        ttl=timedelta(days=1),
        source=source,
    )

    try:
        store.apply([driver, fv])
    except Exception as e:
        raise RuntimeError(f"Failed to apply entity/feature view: {e}") from e


def get_training_features(store: FeatureStore) -> pd.DataFrame:
    """Pull historical features for model training."""
    entity_df = pd.DataFrame({"driver_id": [1001, 1002, 1003]})
    features = [
        "driver_hourly_stats:conv_rate",
        "driver_hourly_stats:avg_daily_trips",
    ]

    try:
        response = store.get_historical_features(
            entity_df=entity_df,
            features=features,
        )
        return response.to_df()
    except Exception as e:
        raise RuntimeError(f"Historical feature retrieval failed: {e}") from e


def get_online_features(store: FeatureStore) -> dict:
    """Pull online features for real-time serving inference."""
    entity_rows = [
        {"driver_id": 1001},
        {"driver_id": 1002},
    ]
    features = [
        "driver_hourly_stats:conv_rate",
        "driver_hourly_stats:avg_daily_trips",
    ]

    try:
        response = store.get_online_features(
            entity_rows=entity_rows,
            features=features,
        )
        return response.to_dict()
    except Exception as e:
        raise RuntimeError(f"Online feature retrieval failed: {e}") from e


def main() -> None:
    """End-to-end pipeline: register entities, then serve offline and online features."""
    store = build_feature_store()
    register_entities_and_views(store)

    training_df = get_training_features(store)
    print("Training features:")
    print(training_df)

    online_result = get_online_features(store)
    print("\nOnline features:")
    print(online_result)


if __name__ == "__main__":
    main()
