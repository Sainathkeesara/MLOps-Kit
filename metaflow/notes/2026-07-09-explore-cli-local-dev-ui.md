# mfl-026 — Trying the Metaflow CLI and local dev UI

After `pip install metaflow`, I ran the CLI commands listed in `--help` to see what's available, then tried the local dev stack.

## CLI commands I ran

- `metaflow --help` — lists subcommands: run, resume, show, status, step, etc.
- `python flow.py run` — executes the flow locally, no external service needed.
- `python flow.py show` — prints the flow DAG and latest run state to the terminal.
- `python flow.py status` — shows run state for the current flow.
- `metaflow resume <run-id>` — reruns a failed flow from the failed step.
- `metaflow run --help` — flags like `--with kubernetes` switch execution to Kubernetes without code changes.

## Local dev UI

`metaflow-dev up` downloads Minikube and uses Tilt to deploy the metadata service, Postgres, and Metaflow UI. I left the shell running because it keeps port-forwards alive. `metaflow-dev shell` opens a new session with `METAFLOW_SERVICE_URL` pre-set so flows log to the local metadata service automatically.

## Gotchas I hit

**Gotcha 1:** `metaflow-dev up` runs a `check-docker` Make target that calls `open -a Docker` on macOS. Orbstack users with a working daemon get `Unable to find application named 'Docker'`. Fix: comment out the target or skip it; Orbstack's Docker-compatible socket works for Tilt.

**Gotcha 2:** The generated `start.sh` contains `set -g`, invalid in `fish` and POSIX `sh`. Wrapping the Make invocation with `SHELL=/bin/bash` before running fixes it.

**Gotcha 3:** `pip install psycopg2-binary` is needed before `metaflow-dev up` completes — the metadata service build fails with `pg_config not found` if only `psycopg2` is installed.
