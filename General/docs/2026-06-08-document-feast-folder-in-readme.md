# Documenting the feast/ folder in the README

The README Coverage table and Layout section needed the `feast/` directory listed. Feast has a primer, install notes, and one snippet — enough content that it should show up in the same docs as every other tool.

I added a Feast row to the Coverage table:

```
| Feast | 2 | 1 | — | — | — | — | — |
```

Notes: the primer and install notes. Snippets: the first feature view. The rest are empty because there aren't any scripts, configs, manifests, docs, or notebooks yet.

I also added a Layout entry between dvc/ and kubeflow/ to keep alphabetical order:

```
- **`feast/`** — Feast feature store notes, snippets, and configs
```

That's all — both table and layout list are now complete and consistent.
