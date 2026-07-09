---
last_verified: 2026-07-06
tool_version: "2.19.35"
sources:
  - https://pypi.org/project/metaflow/
  - https://docs.metaflow.org/getting-started/install
  - https://community.outerbounds.com/t/26887578
  - https://github.com/netflix/metaflow/issues/2737
  - https://github.com/Netflix/metaflow/issues/2704
---

# mfl-026 — Trying the Metaflow CLI and local dev stack

After installing Metaflow (`pip install metaflow`), I poked around the CLI and tried spinning up the local dev UI.

## CLI commands I ran

- `metaflow --help` — lists subcommands: run, resume, show, status, step, etc.
- `python flow.py run` — executes the flow locally (runs in-process, no external service needed)
- `python flow.py show` — opens the flow browser in the browser on port 8050
- `metaflow status` — shows the latest run for each flow
- `metaflow step --help` — inspect individual step parameters

I got tripped up on `metaflow step` at first — it needs a run ID which I had to look up from the UI or from `metaflow status output`.

## Local dev stack

I tried `metaflow-dev up` to get the full metadata service. It crashed with a Docker Desktop check — I run Orbstack, not Docker Desktop. The workaround was commenting out the `check-docker` section in the Makefile.

The sandbox at https://docs.metaflow.org/getting-started/install was useful for trying flows without installing anything. Good for quick experiments before committing to a local install.

## Gotchas I hit

- `metaflow-dev up` also had a shell compatibility issue with my zsh setup — it outputs bash-specific syntax. Wrapping with `SHELL=/bin/bash` before running fixed it.
- If I wanted the full local metadata service, I'd need `psycopg2-binary` installed first — without it the service build fails with `pg_config not found`.
