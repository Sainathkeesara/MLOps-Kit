# last_verified: 2026-07-10 · python

"""con-020 — Feature store fundamentals exercises (L2)

Feature stores separate feature engineering from training/serving
so the same features power both. These exercises reproduce the key
ideas — a feature definition, an offline batch pull, an online
point lookup, and a point-in-time-correct join — without requiring
a real store (e.g. Feast). I wrote them to make the mental model
solid before wiring a store into a project.
"""

from datetime import datetime
from collections import defaultdict


# --- Exercise 1: define a feature and its source ---


def exercise_1_define_feature() -> dict:
    """Exercise 1: a feature is a name + entity + transformation."""
    feature = {
        "name": "user_avg_spend_30d",
        "entity": "user_id",
        "source": "transactions",
        "transform": "AVG(amount) WHERE event_ts >= now() - 30d",
    }
    print("Defined feature:", feature["name"])
    assert feature["entity"] == "user_id"
    return feature


# --- Exercise 2: pull features for a batch of entities (offline) ---


def exercise_2_offline_pull(features: list, entity_ids: list) -> dict:
    """Exercise 2: simulate an offline store returning one row per entity."""
    store = {
        "u1": {"user_avg_spend_30d": 42.5},
        "u2": {"user_avg_spend_30d": 18.0},
    }
    out = {eid: store.get(eid, {f: 0.0 for f in features}) for eid in entity_ids}
    print("Offline pull:", out)
    return out


# --- Exercise 3: point lookup from the online store (serving) ---


def exercise_3_online_lookup(entity_id: str) -> dict:
    """Exercise 3: low-latency single-entity read for inference."""
    online = {"u1": {"user_avg_spend_30d": 42.5}}
    row = online.get(entity_id)
    print(f"Online lookup {entity_id}: {row}")
    return row


# --- Exercise 4: point-in-time join keeps training leakage-free ---


def exercise_4_point_in_time_join(events: list, features_by_ts: dict) -> list:
    """Exercise 4: attach only features available BEFORE each event ts."""
    rows = []
    for ev in events:
        ts = ev["event_ts"]
        # pick the latest feature snapshot strictly before the event
        avail = [v for t, v in features_by_ts.items() if t <= ts]
        snap = avail[-1] if avail else {"user_avg_spend_30d": 0.0}
        rows.append({**ev, "feature": snap})
    print("Point-in-time rows:")
    for r in rows:
        print(f"  {r['event_ts']} {r['entity']} -> {r['feature']}")
    # the future snapshot must NOT leak into the earlier event
    assert rows[0]["feature"]["user_avg_spend_30d"] < 99.0
    return rows


if __name__ == "__main__":
    feat = exercise_1_define_feature()
    exercise_2_offline_pull([feat["name"]], ["u1", "u2"])
    exercise_3_online_lookup("u1")
    events = [
        {"entity": "u1", "event_ts": datetime(2026, 1, 1)},
        {"entity": "u1", "event_ts": datetime(2026, 2, 1)},
    ]
    snapshots = {
        datetime(2026, 1, 1): {"user_avg_spend_30d": 10.0},
        datetime(2026, 2, 1): {"user_avg_spend_30d": 99.0},
    }
    exercise_4_point_in_time_join(events, snapshots)
    print("All feature store exercises passed.")
