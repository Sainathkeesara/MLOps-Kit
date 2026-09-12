---
last_verified: 2026-09-12
tool_version: "0.66.0"
sources:
  - https://github.com/feast-dev/feast/releases/tag/v0.66.0
---

# Feast companion data files

> Data files referenced by Feast notes for local development.

## Files

| File | Description |
|------|-------------|
| `registry.db` | SQLite metadata registry used by Feast for local feature store tracking |

## Usage

The Feast notes reference `registry: "data/registry.db"` in `feature_store.yaml` for local dev. This file is the actual SQLite database that Feast uses to store entity, feature view, and data source metadata.

When running `feast apply`, Feast reads `feature_store.yaml` and populates this registry with the defined entities and feature views. The registry is what makes `feast features` and `feast materialize` work against a local store without requiring a remote metadata service.
