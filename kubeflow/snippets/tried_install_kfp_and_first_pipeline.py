"""Install kfp SDK and compile my first hello-world pipeline."""

from kfp import dsl, compiler


@dsl.component
def say_hello(message: str) -> str:
    print(message)
    return message


@dsl.pipeline
def hello_pipeline():
    say_hello(message="Hello from KFP v2!")


compiler.Compiler().compile(hello_pipeline, "hello-pipeline.yaml")
