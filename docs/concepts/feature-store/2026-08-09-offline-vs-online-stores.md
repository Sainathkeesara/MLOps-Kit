---
last_verified: 2026-08-09
tool_version: n/a
sources:
  - https://docs.feast.dev/getting-started/quickstart
  - https://neelmishra.github.io/blog/mlops/feature-stores/point-in-time.html
  - https://vife.ai/blog/taming-data-beast-feature-stores-feast-tutorial
---

# Feature Store — Offline vs online stores and point-in-time joins

> Learning where the two stores sit and why the join logic matters.

## What I was trying to do

I kept hearing about offline and online stores in feature-store talks, but the distinction felt fuzzy until I tried using Feast. I wanted to understand when each store is used and why point-in-time joins are the thing that makes the whole system worth having.

## Offline vs online

The offline store holds every feature value ever computed — historical Parquet files or warehouse tables. You use it when building training datasets. The online store holds the latest feature per entity in a low-latency store like Redis or SQLite. You use it when a model needs a fast lookup at inference time.

Materialization bridges the two: a batch job copies new feature rows from offline to online. Without it, online reads return empty because nothing has been pushed into the low-latency store yet.

## Point-in-time joins

A point-in-time join prevents future leakage during training. If you naively join a user's transaction count to a prediction timestamp, you might pull transactions that happened *after* the prediction. `get_historical_features()` uses the entity's event timestamp to ensure only features available at or before prediction time are joined.

I hit this when I first replicated Feast's quickstart with plain pandas. My training accuracy looked great, but it was artificially high because I was training on features that wouldn't exist at inference time. Point-in-time joins fixed that.

## Got stuck on

**Materialization timing.** I ran `store.apply()` and immediately called `get_online_features()`, expecting results. It returned empty because materialization hadn't run yet. Forgetting this step is the most common beginner mistake.

**TTL side effects.** I set a 1-day TTL on my feature view and then tried to materialize a week of history. Feast only kept the most recent day because older rows expired. The TTL controls how far back the online store looks, so I had to align it with my materialization window.

## What I'd try next

I want to try Redis as the online store instead of SQLite to see how latency changes, and then compare incremental versus full-refresh materialization. I also want to wire this into a training script so the feature store becomes a real dependency rather than a standalone demo.
