---
last_verified: 2026-07-22
tool_version: 3.x
sources:
  - https://theneuralbase.com/mlops-fundamentals/learn/beginner/dvc-for-data-version-control/
---

# 2026-07-22 Remote `dvc push` vs `dvc pull` gotchas

I set up a local remote with `dvc remote add myremote /tmp/dvc-remote` and pushed my first dataset. Then I tried `dvc pull` on a second clone. Two things caught me off guard.

First, `dvc pull` silently falls back to the local cache when the remote is unreachable. A teammate won't realize data is stale until rebuild time. The safer pattern is `dvc fetch` to explicitly pull from the remote.

Second, DVC 3.x pushes to ALL configured remotes by default when you run bare `dvc push`. The right way is `dvc push -r <remotename>` so I only hit the remote I intend.

Remote config lives in `.dvc/config` (or `.dvc/config.local` for secrets). `dvc remote list` shows what's configured. `dvc status check` is a quick way to verify whether the cache is missing or the remote is unreachable before running a full pipeline.