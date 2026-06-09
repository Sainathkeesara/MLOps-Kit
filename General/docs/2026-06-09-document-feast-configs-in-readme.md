# Documenting feast/configs/ in README

The feast/configs/ folder was created by Repo Auditor but hadn't been documented in the README Layout section. There's now a feature_store.yaml with SQLite online store configuration.

## Changes to Layout section

Added a subsection under feast/:

```
- **`feast/configs/`** — Feast feature store YAML configurations
```

## Changes to Coverage table

Updated the Feast row to show Configs: 1:

```
| Feast | 2 | 1 | — | 1 | — | — | — |
```

## Changes to Quick Links

Added under the Define features section:

```
- [Feast feature store config](../feast/configs/feature_store.yaml) — Feature store configuration with SQLite online store
```

That's all — both table and layout list are now consistent with the present files.