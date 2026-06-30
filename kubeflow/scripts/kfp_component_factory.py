"""Reusable KFP pipeline component factory with resource config and caching.

A factory helper that standardises how KFP v2 components are built —
applies consistent resource limits, caching policy, pip dependencies, and
container images so every component in a project shares the same defaults.

The factory does not own the component logic; it owns the *infrastructure
wrapping* around it. Component authors write pure Python handler functions
and the factory takes care of packaging, resources, and caching.

Usage:
    python kfp_component_factory.py                     # compile + submit demo
    python kfp_component_factory.py --compile-only      # compile YAML only
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from typing import Any, Callable

from kfp import compiler, dsl
import kfp


# ---------------------------------------------------------------------------
# Spec — one place to describe a component's infrastructure needs
# ---------------------------------------------------------------------------


@dataclass
class ComponentSpec:
    """Infrastructure profile for a KFP component.

    Attributes:
        image:          Container image (e.g. \"python:3.9-slim\").
        packages:       Pip packages the component needs at runtime.
        cpu_limit:      CPU limit string (e.g. \"2\", \"500m\").
        memory_limit:   Memory limit string (e.g. \"4Gi\", \"512Mi\").
        gpu_limit:      Number of GPUs to request (0 = none).
        cacheable:      Whether KFP may reuse a cached output for identical
                        inputs. Set to False for training steps whose results
                        should always be fresh.
    """

    image: str = "python:3.9-slim"
    packages: list[str] = field(default_factory=list)
    cpu_limit: str = "500m"
    memory_limit: str = "512Mi"
    gpu_limit: int = 0
    cacheable: bool = True


# ---------------------------------------------------------------------------
# apply_spec — configure a built task with its spec
# ---------------------------------------------------------------------------


def apply_spec(task: dsl.PipelineTask, spec: ComponentSpec) -> dsl.PipelineTask:
    """Apply *spec* resource and caching settings to *task*.

    Call this on every component task inside your pipeline function after
    the component has been invoked.
    """
    task.set_cpu_limit(spec.cpu_limit)
    task.set_memory_limit(spec.memory_limit)
    if spec.gpu_limit > 0:
        task.set_accelerator_limit(spec.gpu_limit)
    if not spec.cacheable:
        task.execution_options.caching_strategy.max_cache_staleness = "P0D"
    return task


def apply_specs(tasks: dict[str, tuple[dsl.PipelineTask, ComponentSpec]]) -> None:
    """Batch-apply specs.  Raises on the first failure with the task name."""
    for name, (task, spec) in tasks.items():
        try:
            apply_spec(task, spec)
        except Exception as exc:
            raise RuntimeError(f"failed to apply spec to '{name}': {exc}") from exc


# ---------------------------------------------------------------------------
# build_component — factory that wraps a plain Python function as a KFP
#                   component with the infrastructure from *spec*.
# ---------------------------------------------------------------------------


def build_component(
    handler: Callable[..., Any],
    spec: ComponentSpec,
) -> Callable[..., dsl.PipelineTask]:
    """Wrap *handler* as a KFP v2 component with *spec* infrastructure.

    The returned callable, when invoked inside a ``@dsl.pipeline``, creates
    a KFP task that runs *handler* with the image, packages, resources, and
    caching policy defined in *spec*.

    Example:

        def my_train(data: str, lr: float) -> str: ...

        train_component = build_component(my_train, trainer_spec)

        @dsl.pipeline(...)
        def pipe():
            task = train_component(data="...", lr=0.01)
            # task already has resources applied
    """

    handler_name = handler.__name__

    if spec.packages:
        wrapped = dsl.component(
            handler,
            base_image=spec.image,
            packages_to_install=spec.packages,
        )
    else:
        wrapped = dsl.component(
            handler,
            base_image=spec.image,
        )

    def wrapper(*args: Any, **kwargs: Any) -> dsl.PipelineTask:
        task = wrapped(*args, **kwargs)
        apply_spec(task, spec)
        return task

    wrapper.__name__ = handler_name
    wrapper.__qualname__ = handler_name
    wrapper.__doc__ = (
        f"KFP component wrapping ``{handler_name}``\n\n"
        f"Infrastructure: image={spec.image}, "
        f"cpu={spec.cpu_limit}, mem={spec.memory_limit}, "
        f"gpu={spec.gpu_limit}, cacheable={spec.cacheable}\n\n"
        f"{handler.__doc__ or ''}"
    )
    return wrapper


# ---------------------------------------------------------------------------
# Concrete components — plain Python handlers + specs
# ---------------------------------------------------------------------------


def _load_data(url: str) -> str:
    import pandas as pd
    df = pd.read_csv(url)
    row_count = len(df)
    print(f"loaded {row_count} rows from {url}")
    return f"{row_count} rows"


def _train_model(data_summary: str, lr: float = 0.01) -> str:
    import hashlib
    fingerprint = hashlib.sha256(data_summary.encode()).hexdigest()[:8]
    model_ref = f"model-lr={lr}-data={fingerprint}"
    print(f"trained {model_ref}")
    return model_ref


def _evaluate_model(model_ref: str, threshold: float = 0.8) -> float:
    import hashlib
    import random
    seed = int(hashlib.sha256(model_ref.encode()).hexdigest()[:8], 16)
    rng = random.Random(seed)
    score = round(rng.uniform(0.6, 0.99), 4)
    print(f"{model_ref} → accuracy={score}")
    if score < threshold:
        print(f"accuracy {score} below threshold {threshold}")
    return score


loader_spec = ComponentSpec(
    image="python:3.9-slim",
    packages=["pandas"],
    cpu_limit="500m",
    memory_limit="1Gi",
    cacheable=True,
)

trainer_spec = ComponentSpec(
    image="python:3.9-slim",
    packages=[],
    cpu_limit="2",
    memory_limit="4Gi",
    cacheable=False,
)

evaluator_spec = ComponentSpec(
    image="python:3.9-slim",
    packages=[],
    cpu_limit="1",
    memory_limit="2Gi",
    cacheable=True,
)


load_data = build_component(_load_data, loader_spec)
train_model = build_component(_train_model, trainer_spec)
evaluate_model = build_component(_evaluate_model, evaluator_spec)


# ---------------------------------------------------------------------------
# Demo pipeline
# ---------------------------------------------------------------------------


@dsl.pipeline(
    name="factory-demo-pipeline",
    description="Pipeline built with the component factory pattern",
    pipeline_root="s3://my-bucket/kfp-pipelines",
)
def demo_pipeline(url: str = "https://raw.githubusercontent.com/example/data.csv") -> float:
    load = load_data(url=url)
    train = train_model(data_summary=load.output, lr=0.01)
    eval_ = evaluate_model(model_ref=train.output, threshold=0.8)
    return eval_.output


# ---------------------------------------------------------------------------
# CLI — compile and optionally submit
# ---------------------------------------------------------------------------


def compile_and_run(compile_only: bool = False) -> None:
    compiler.Compiler().compile(demo_pipeline, "factory-demo-pipeline.yaml")
    print("Compiled factory-demo-pipeline.yaml")

    if compile_only:
        return

    try:
        client = kfp.Client(host="http://localhost:8080")
    except Exception as exc:
        print(f"Cannot reach KFP at localhost:8080: {exc}", file=sys.stderr)
        print("Compiled YAML is available locally.", file=sys.stderr)
        sys.exit(1)

    run = client.create_run_from_pipeline_func(
        demo_pipeline,
        arguments={"url": "s3://my-bucket/data/train.csv"},
        experiment_name="factory-demo",
    )
    print(f"Submitted run: {run.run_id}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="KFP component factory demo"
    )
    parser.add_argument(
        "--compile-only",
        action="store_true",
        help="Only compile pipeline YAML without submitting",
    )
    args = parser.parse_args()
    compile_and_run(compile_only=args.compile_only)


if __name__ == "__main__":
    main()
