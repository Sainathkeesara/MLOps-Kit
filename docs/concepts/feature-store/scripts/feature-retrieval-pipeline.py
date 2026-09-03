# last_verified: 2026-09-03 · feast 0.66.0

"""Feature retrieval pipeline with Feast SDK.

Defines driver entity and feature views, materializes from offline to online,
and demonstrates both batch (historical) and real-time (online) retrieval patterns.

Usage:
    python feature-retrieval-pipeline.py --repo-dir . --entity-ids driver_001 driver_002
    python feature-retrieval-pipeline.py --repo-dir . --mode historical --start 2026-01-01 --end 2026-09-01
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Optional

try:
    from feast import FeatureStore, Entity, Field, ValueType
    from feast.infra.offline_stores.file_source import FileSource
    from feast.types import Float32, Int64, String
except ImportError:
    print("feast is not installed. Install with: pip install feast", file=sys.stderr)
    sys.exit(1)


def create_feature_definitions(repo_path: Path) -> None:
    """Write the feature repo definitions (entities, views, services) to disk.

    This is a one-time setup step. In a real project these files live in
    a feature_repo/ directory and are checked into git.
    """
    from feast import FeatureView, RepoConfig, FileOnlineStoreConfig
    from datetime import timedelta

    driver = Entity(
        name="driver_id",
        join_keys=["driver_id"],
        value_type=ValueType.INT64,
        description="Unique driver identifier",
    )

    driver_stats_source = FileSource(
        path=str(repo_path / "data" / "driver_stats.parquet"),
        timestamp_field="event_timestamp",
    )

    driver_features = FeatureView(
        name="driver_stats",
        entities=[driver],
        ttl=timedelta(days=1),
        schema=[
            Field(name="conv_rate", dtype=Float32),
            Field(name="acc_rate", dtype=Float32),
            Field(name="avg_daily_trips", dtype=Int64),
        ],
        source=driver_stats_source,
        online=True,
    )

    config = RepoConfig(
        project="driver_metrics",
        registry=str(repo_path / "registry.db"),
        provider="local",
        online_store=FileOnlineStoreConfig(path=str(repo_path / "online_store")),
        entity_key_serialization_version=2,
    )

    store = FeatureStore(config=config)
    store.apply([driver, driver_stats_source, driver_features])
    print(f"Applied feature definitions to {repo_path}")


def materialize_features(
    repo_path: Path,
    start: Optional[str] = None,
    end: Optional[str] = None,
) -> None:
    """Materialize features from the offline store to the online store.

    Without arguments, materializes the last 24 hours (incremental).
    With start/end, does a full materialization of the specified range.
    """
    store = FeatureStore(repo_path=str(repo_path))

    if start and end:
        start_dt = datetime.fromisoformat(start)
        end_dt = datetime.fromisoformat(end)
        store.materialize(start_dt, end_dt)
        print(f"Materialized from {start} to {end}")
    else:
        store.materialize_incremental(datetime.now())
        print("Materialized incrementally (last 24 hours)")


def retrieve_online_features(
    repo_path: Path,
    entity_ids: List[int],
) -> dict:
    """Fetch the latest feature values for a set of entity IDs from the online store.

    Returns a dict with entity keys and their corresponding feature values.
    This is the path a serving endpoint would take at inference time.
    """
    store = FeatureStore(repo_path=str(repo_path))

    feature_refs = [
        "driver_stats:conv_rate",
        "driver_stats:acc_rate",
        "driver_stats:avg_daily_trips",
    ]

    response = store.get_online_features(
        features=feature_refs,
        entity_rows=[{"driver_id": eid} for eid in entity_ids],
    )

    return response.to_dict()


def retrieve_historical_features(
    repo_path: Path,
    entity_df_path: str,
) -> "pd.DataFrame":
    """Pull point-in-time-correct feature values for training.

    The entity DataFrame must have a driver_id column and an event_timestamp
    column. Feast joins features available at or before each row's timestamp,
    preventing future data leakage.
    """
    import pandas as pd

    store = FeatureStore(repo_path=str(repo_path))
    entity_df = pd.read_csv(entity_df_path, parse_dates=["event_timestamp"])

    feature_refs = [
        "driver_stats:conv_rate",
        "driver_stats:acc_rate",
        "driver_stats:avg_daily_trips",
    ]

    training_df = store.get_historical_features(
        entity_df=entity_df,
        features=feature_refs,
    ).to_df()

    return training_df


def validate_online_serving(repo_path: Path, entity_ids: List[int]) -> bool:
    """Quick health check: verify online features return non-null values.

    Returns True if all requested entities have feature values in the online store.
    Catches the most common beginner mistake — forgetting to materialize.
    """
    result = retrieve_online_features(repo_path, entity_ids)

    all_valid = True
    for i, eid in enumerate(entity_ids):
        conv_rate = result["conv_rate"][i]
        if conv_rate is None:
            print(f"WARNING: driver_id={eid} has no online features (materialize first?)")
            all_valid = False
        else:
            print(f"  driver_id={eid}: conv_rate={conv_rate:.4f}, "
                  f"acc_rate={result['acc_rate'][i]:.4f}, "
                  f"avg_daily_trips={result['avg_daily_trips'][i]}")

    return all_valid


def main() -> None:
    parser = argparse.ArgumentParser(description="Feature retrieval pipeline with Feast")
    parser.add_argument("--repo-dir", default=".", help="Feature repo root directory")
    parser.add_argument(
        "--mode",
        choices=["setup", "materialize", "online", "historical", "validate"],
        default="validate",
        help="Pipeline step to run",
    )
    parser.add_argument("--entity-ids", nargs="+", type=int, default=[1001, 1002, 1003],
                        help="Driver IDs for online retrieval")
    parser.add_argument("--start", default=None, help="Materialization start date (ISO)")
    parser.add_argument("--end", default=None, help="Materialization end date (ISO)")
    parser.add_argument("--entity-csv", default=None,
                        help="Path to entity CSV for historical retrieval")
    args = parser.parse_args()

    repo_path = Path(args.repo_dir).resolve()

    if args.mode == "setup":
        create_feature_definitions(repo_path)

    elif args.mode == "materialize":
        materialize_features(repo_path, args.start, args.end)

    elif args.mode == "online":
        result = retrieve_online_features(repo_path, args.entity_ids)
        for i, eid in enumerate(args.entity_ids):
            print(f"driver_id={eid}: {result}")

    elif args.mode == "historical":
        if not args.entity_csv:
            print("ERROR: --entity-csv required for historical mode", file=sys.stderr)
            sys.exit(1)
        df = retrieve_historical_features(repo_path, args.entity_csv)
        print(df.head(10).to_string())

    elif args.mode == "validate":
        ok = validate_online_serving(repo_path, args.entity_ids)
        sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
