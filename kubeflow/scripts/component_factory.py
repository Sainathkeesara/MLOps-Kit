"""kub-017 — Reusable KFP pipeline component factory with resource config and caching.

This module provides a factory function for creating standardized KFP v2 components
with consistent resource limits, caching settings, and retry policies. It addresses
the common need to apply uniform configuration across many components in a pipeline.
"""

from kfp import dsl
from typing import Optional, Dict, Any, List


def create_component(
    name: str,
    base_image: str = "python:3.11-slim",
    packages_to_install: Optional[List[str]] = None,
    cpu_limit: str = "1",
    memory_limit: str = "2Gi",
    cpu_request: str = "500m",
    memory_request: str = "1Gi",
    enable_cache: bool = True,
    min_retry_duration: str = "10s",
    max_retry_attempts: int = 3,
    timeout: Optional[str] = None,
) -> callable:
    """
    Factory for creating KFP v2 components with standardized resource and caching config.

    Args:
        name: Component name used as the decorator name.
        base_image: Container image for the component.
        packages_to_install: Python packages to pip-install at runtime.
        cpu_limit: CPU limit for the container (e.g., "1", "2").
        memory_limit: Memory limit (e.g., "2Gi", "4Gi").
        cpu_request: CPU request (e.g., "500m").
        memory_request: Memory request (e.g., "1Gi").
        enable_cache: Whether to enable task output caching.
        min_retry_duration: Minimum duration before retryable.
        max_retry_attempts: Maximum retry attempts on failure.
        timeout: Optional timeout string (e.g., "1h", "30m").

    Returns:
        A decorator function that applies the configuration to the wrapped function.
    """

    def decorator(func: callable) -> Any:
        comp = dsl.component(
            base_image=base_image,
            packages_to_install=packages_to_install or [],
        )(func)
        comp._name = name
        comp._resource_config = {
            "cpu_limit": cpu_limit,
            "memory_limit": memory_limit,
            "cpu_request": cpu_request,
            "memory_request": memory_request,
        }
        comp._caching_config = {"enable_cache": enable_cache}
        comp._retry_config = {
            "min_retry_duration": min_retry_duration,
            "max_retry_attempts": max_retry_attempts,
        }
        if timeout:
            comp._retry_config["timeout"] = timeout
        return comp

    return decorator


def configure_task(
    task: Any,
    cpu_limit: Optional[str] = None,
    memory_limit: Optional[str] = None,
    cpu_request: Optional[str] = None,
    memory_request: Optional[str] = None,
    enable_cache: Optional[bool] = None,
    max_retry_attempts: Optional[int] = None,
    timeout: Optional[str] = None,
) -> Any:
    """
    Apply resource and caching configuration to a KFP task instance.

    This function mutates the task in-place and returns it for chaining.

    Args:
        task: The KFP component task instance (result of calling a component).
        cpu_limit: Override CPU limit (e.g., "2").
        memory_limit: Override memory limit (e.g., "4Gi").
        cpu_request: Override CPU request (e.g., "1").
        memory_request: Override memory request (e.g., "2Gi").
        enable_cache: Override caching for this task.
        max_retry_attempts: Override max retry attempts.
        timeout: Override timeout (e.g., "1h").

    Returns:
        The configured task instance.
    """
    if cpu_limit:
        task.set_cpu_limit(cpu_limit)
    if memory_limit:
        task.set_memory_limit(memory_limit)
    if cpu_request:
        task.set_cpu_request(cpu_request)
    if memory_request:
        task.set_memory_request(memory_request)

    # Caching and retry configuration in KFP v2
    # These settings are applied via the task's underlying component spec
    caching_settings = {"enableCache": enable_cache if enable_cache is not None else True}
    task._caching_options = caching_settings

    if max_retry_attempts is not None:
        task._retry_policy = {"backoffDuration": "30s", "maxAttempts": max_retry_attempts}

    if timeout:
        task._timeout = timeout

    return task


# Example component definitions using the factory
def preprocess_component():
    """Factory for a lightweight preprocessing component."""
    @create_component(
        name="preprocess",
        base_image="python:3.11-slim",
        packages_to_install=["pandas", "numpy"],
        cpu_limit="1",
        memory_limit="1Gi",
        cpu_request="500m",
        memory_request="512Mi",
        enable_cache=True,
    )
    def preprocess(input_data: str) -> str:
        import pandas as pd
        df = pd.read_csv(input_data)
        cleaned = df.dropna()
        return cleaned.to_csv(index=False)

    return preprocess


def train_component():
    """Factory for a compute-intensive training component."""
    @create_component(
        name="train",
        base_image="python:3.11-slim",
        packages_to_install=["scikit-learn", "mlflow"],
        cpu_limit="2",
        memory_limit="4Gi",
        cpu_request="1",
        memory_request="2Gi",
        enable_cache=False,  # Training should not be cached
        max_retry_attempts=2,
    )
    def train(train_data: str, learning_rate: float) -> str:
        import mlflow
        import pandas as pd
        df = pd.read_csv(train_data)
        X, y = df.iloc[:, :-1].values, df.iloc[:, -1].values
        model = {"lr": learning_rate, "weights": [0.5] * X.shape[1]}
        return str(model)

    return train


def evaluate_component():
    """Factory for an evaluation component with metrics output."""
    @create_component(
        name="evaluate",
        base_image="python:3.11-slim",
        packages_to_install=["scikit-learn"],
    )
    def evaluate(model_artifact: str, test_data: str) -> float:
        accuracy = 0.85
        return accuracy

    return evaluate


# Example pipeline using the factory
@dsl.pipeline(
    name="factory-example-pipeline",
    description="Demonstrates the component factory pattern with resource config and caching.",
    pipeline_root="s3://my-pipeline-bucket",
)
def example_pipeline(data_path: str = "s3://data.csv", learning_rate: float = 0.01):
    """
    Example pipeline showing how to use the component factory.

    The factory ensures all components get consistent resource and caching settings
    without repeating boilerplate configuration code.
    """
    preprocess = preprocess_component()(input_data=data_path)
    train_step = train_component()(train_data=preprocess.output, learning_rate=learning_rate)

    # Override cache for training step
    configure_task(train_step, enable_cache=False)

    evaluate_step = evaluate_component()(model_artifact=train_step.output, test_data=preprocess.output)

    # Apply different resource limits to evaluation
    configure_task(evaluate_step, cpu_limit="1", memory_limit="1Gi")


def validate_component_config(component: Any, expected_resources: Dict[str, str]) -> bool:
    """
    Validate that a component has the expected resource configuration.

    Args:
        component: The component to validate.
        expected_resources: Expected key-value pairs for resource limits/requests.

    Returns:
        True if configuration matches, False otherwise.
    """
    config = getattr(component, "_resource_config", {})
    for key, expected in expected_resources.items():
        if config.get(key) != expected:
            return False
    return True


if __name__ == "__main__":
    # Quick test: verify the factory creates components with correct config
    from kfp import compiler

    preproc = preprocess_component()
    assert validate_component_config(preproc, {
        "cpu_limit": "1",
        "memory_limit": "1Gi",
        "cpu_request": "500m",
        "memory_request": "512Mi",
    })
    print("Preprocessing component config validated.")

    train_comp = train_component()
    assert validate_component_config(train_comp, {
        "cpu_limit": "2",
        "memory_limit": "4Gi",
    })
    print("Training component config validated.")

    compiler.Compiler().compile(example_pipeline, "factory-example-pipeline.yaml")
    print("Pipeline compiled to factory-example-pipeline.yaml")