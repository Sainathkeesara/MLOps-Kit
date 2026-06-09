# feast/configs/

Configuration files for Feast feature stores. This folder contains feature store definitions that configure offline and online stores, entity mappings, and feature view registrations.

## What's here

- **`feature_store.yaml`** — Main configuration defining the offline store (local files/S3), online store (SQLite/Redis), and registry location

The feature store config ties together where features live (the offline store), where they're served from (the online store), and how they're registered for discovery. With SQLite as the online store, you can run a local Feast setup without external infrastructure.