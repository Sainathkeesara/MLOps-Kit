---
last_verified: 2026-08-22
tool_version: "—"
---

# Install ZenML and explore the CLI

> First-day notes for someone installing ZenML for the first time. Personal voice, plain language.

## What I did

Ran `pip install zenml` and then `zenml init` to create the local repository. It set up a `.zenml` directory with SQLite metadata and local artifact stores by default. Ran `zenml stack list` and saw the local stack with orchestrator, artifact store, and metadata store all pointing at local paths.

## Exploring the CLI

Ran `zenml pipeline list` after creating a simple pipeline to verify the run registered. Hit a permissions issue when pushing artifacts to the local store; fixed it by making sure the `.zenml` directory was writable. `zenml stack describe local` helped me understand what each component does without opening the docs.

## What tripped me up

Running `zenml init` inside a nested directory once failed silently. Moving to the project root and re-running fixed it. Also, the dashboard port defaults to 8237 — if that's already in use, `zenml up` fails with a cryptic bind error.
