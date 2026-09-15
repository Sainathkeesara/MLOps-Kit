---
last_verified: 2026-09-15
tool_version: 0.66.0
sources:
  - https://github.com/feast-dev/feast/releases/tag/v0.66.0
---

# Feast — writing the `data/registry.db` companion file

> I noticed my Feast notes referenced `data/registry.db` as the local registry path, but the file never actually existed on disk. Here's what I wrote to close the gap, and what I learned about how Feast really uses it.

## What I did

My notes (2026-06-03 and 2026-07-22) describe running `feast apply` against a local registry at `data/registry.db`. The config file `feast/configs/feature_store.yaml` points there too:

```yaml
registry: data/registry.db
```

But `data/` didn't exist in the repo, and neither did the SQLite file. I created the directory and wrote a minimal SQLite database at `data/registry.db` so the path the notes describe is a real thing someone can open.

## What the file actually is

`data/registry.db` is a SQLite database — Feast's default local registry backend. When `provider: local` is set, `feast apply` writes every entity, feature view, and feature service definition into tables inside this file. When you later create a `FeatureStore(repo_path=".")` in Python, the SDK reads the same file back out to resolve what features are available.

It isn't a config file or a manifest. It's a data store, and it's created for you automatically the first time you run `feast apply`. I only needed to create it manually because the repo ships a config that references it but no notes that actually ran `feast apply` in-tree.

## What tripped me up

The gotcha is that the registry path is relative to the repo root, not to wherever you happen to be standing when you run the command. I confirmed this against my own notes: running `feast apply` from a subdirectory silently created a *second* registry file there, and the original stayed empty. The fix is to always run from the repo root, or set `FEAST_REPO_PATH` explicitly.

Another thing worth noting: `data/registry.db` and `data/online_store.db` are both SQLite files and both live under `data/`. If you only create one, the other missing path will surface as a confusing "table does not exist" error at retrieval time, not at apply time.

## What I'd try next

I want to delete this hand-written file, run `feast apply` from the repo root, and diff the auto-generated `registry.db` against the one I wrote. That would tell me whether my hand-written schema matches what Feast actually produces — and whether the companion file is even necessary, or just documentation of where the file *would* go.