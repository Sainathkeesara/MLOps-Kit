# Choosing between KFP v1 and v2 DSL: migration patterns and breaking changes

## Purpose

Kubeflow Pipelines (KFP) has two major SDK generations in active use. v1 (`kfp.dsl`) targets stable Kubernetes-native pipelines but is in maintenance mode. v2 (`kfp`) introduces a compiler-driven execution model, remote compilation, and first-class artifact handling. This document compares the two DSLs, documents breaking changes, and provides migration guidance for teams transitioning from v1 to v2.

## When to use this reference

- Evaluating whether to start a new project in KFP v1 or v2.
- Migrating an existing v1 pipeline to v2 while preserving step semantics and artifact lineage.
- Debugging behavioral differences between the two SDKs during a parallel-development period.
- Planning a phased upgrade across a shared pipeline library.

## Prerequisites

- Python 3.8+ installed.
- `kfp` (v2 SDK) and `kfp-server-api` (v1 client) available in the working environment.
- Access to a running Kubeflow Pipelines backend (v1.7+ recommended for v2 compatibility).
- Basic familiarity with decorator-based pipeline authoring (`@dsl.pipeline` / `@pipeline`).

## Version overview

### KFP v1 DSL

- Package: `kfp.dsl`
- Pipeline definition uses `@dsl.pipeline` with `dsl.ContainerOp` or `dsl.Component` steps.
- Artifacts are implicit; data passing relies on output `File` or `Model` artifacts referenced by path.
- Caching is opt-in per step via `@dsl.component` with `cache=True`, but caching logic is shallow.
- Deployment targets a KFP standalone backend installed via `kubeflow/pipelines` manifests.

### KFP v2 SDK

- Package: `kfp`
- Pipeline definition uses `@kfp.dsl.pipeline` with type-safe input/output annotations.
- Artifacts are first-class: `kfp.dsl.Artifact`, `kfp.dsl.Metrics`, and typed datasets (e.g. `Dataset`, `Model`) flow through the compiler.
- The v2 compiler produces a workflow YAML that conforms to Argo Workflows with KFP-specific annotations.
- Remote compilation is supported via `kfp.Client().create_experiment` and `kfp.Client().upload_pipeline`.

## Breaking changes

### 1. Component and pipeline decorators

| Aspect | v1 | v2 |
|--------|----|----|
| Decorator import | `from kfp.dsl import pipeline` | `from kfp import dsl; @dsl.pipeline` |
| Step definition | `@dsl.component` or inline `ContainerOp` | `@dsl.component` (strongly typed) |
| Return types | Weak; outputs declared in `outputs` dict | Typed return values or `dsl.Output[...]` parameter |
| Artifact outputs | `OutputArtifact` or `OutputPath` | `dsl.Output[dsl.Artifact]` with explicit uri assignment |

### 2. Artifact handling

In v1, outputs are discovered by the executor writing to a predefined path. In v2, the component must explicitly assign the artifact URI before exiting:

```python
from kfp import dsl
from kfp.dsl import Input, Output, Artifact, Dataset

@dsl.component
def process_data(
    input_csv: Input[Dataset],
    output_data: Output[Dataset],
):
    import pandas as pd
    df = pd.read_csv(input_csv.path)
    df["processed"] = True
    df.to_csv(output_data.path, index=False)
    output_data.metadata["rows"] = str(len(df))
```

### 3. Caching and execution

- v1 caching is metadata-driven and often ignored for container components.
- v2 caching is managed at the pipeline level via `Caching` options in the pipeline spec. Disable it explicitly for deterministic testing:

```python
@dsl.pipeline(name="caching-demo")
def my_pipeline():
    step = process_data()
    step.set_caching_options(False)
```

### 4. Client API differences

- v1 uses `kfp.Client(host=...)` with `runs.create_experiment` and `pipelines.upload_pipeline`.
- v2 uses `kfp.Client()` with `client.create_run_from_pipeline_func`, which compiles the pipeline on the fly if a func is passed, or accepts a compiled YAML path.

```python
import kfp

client = kfp.Client(host="https://<kfp-endpoint>")
client.create_run_from_pipeline_func(
    pipeline_func=my_pipeline,
    arguments={"input_csv": "minio://bucket/data.csv"},
    experiment_name="migration-tests",
)
```

## Migration steps

1. **Inventory existing v1 pipelines.** List `@dsl.pipeline` functions and catalog `ContainerOp` steps that rely on implicit output artifacts.
2. **Upgrade type hints.** Convert `OutputPath` and `InputArtifact` to typed `kfp.dsl.Output` and `Input` annotations.
3. **Rewrite component bodies.** Ensure every artifact output receives `output_x.path` and optional metadata before the function returns.
4. **Update caching logic.** Replace `@dsl.component(cache=True)` with explicit `set_caching_options(True/False)` at the call site.
5. **Adjust client scripts.** Swap `kfp.Client(host=...)` and `run_pipeline` for `create_run_from_pipeline_func`. If remote compilation is desired, pass the pipeline function directly; otherwise pre-compile with `kfp.compiler.Compiler().compile`.
6. **Validate in a staging namespace.** Run a subset of migrated pipelines against a test KFP backend. Compare execution DAGs and artifact URIs between v1 and v2 runs.

## Verify migration

- Compile the v2 pipeline locally and confirm no `CompilerError` is raised:
  ```python
  from kfp import compiler
  compiler.Compiler().compile(my_pipeline, "pipeline_v2.yaml")
  ```
- Submit the compiled YAML and inspect the resulting Argo workflow in the Kubeflow UI.
- Confirm that all artifact URIs are resolvable and that downstream steps consume the expected paths.
- Run a v1 baseline and a v2 candidate with identical inputs; compare run duration, cache hit rates, and final outputs.

## Common errors

- **Missing output path assignment.** v2 components that declare `Output[Artifact]` but never set `.path` fail compilation with "Output artifact URI is not set".
- **Stale import paths.** Migrating incrementally can leave mixed `from kfp.dsl import ...` and `from kfp import dsl` imports. Stick to `from kfp import dsl` for v2 code.
- **Metadata type mismatches.** v2 stores metadata as strings; callers that parse `int(metadata["rows"])` without a fallback can raise `KeyError` or `ValueError`.
- **Cache invalidation confusion.** v2 caching keys incorporate artifact URIs and metadata. Changing the component image version invalidates the cache automatically, but code-only changes do not unless `set_caching_options(False)` is used.
- **KFP backend version skew.** v2 features require KFP backend >= 1.7. Older backends reject v2 workflows with a schema validation error.

## Rollback strategy

Keep v1 pipeline code in a versioned branch alongside the v2 replacement. If the v2 execution path shows latency regressions or unexpected artifact resolution failures, revert client scripts to point at the v1 pipeline YAML while the v2 code is patched. Do not delete v1 compiled artifacts until v2 parity is confirmed in production traffic.

## References

- [KFP v2 SDK documentation](https://www.kubeflow.org/docs/components/pipelines/v2/compile-a-pipeline/)
- [KFP v1 to v2 migration guide](https://www.kubeflow.org/docs/components/pipelines/v2/migrate-from-v1/)
- [KFP component authoring guide](https://www.kubeflow.org/docs/components/pipelines/v2/compile-a-pipeline/)
- [KFP GitHub repository](https://github.com/kubeflow/pipelines)
- [Argo Workflows specification](https://argoproj.github.io/argo-workflows/)
