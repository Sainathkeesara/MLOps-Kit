# last_verified: 2026-07-06 · kfp 2.7.0
# kub-025 — Verify kfp install and compile a minimal pipeline.

import kfp
print(f"kfp version: {kfp.__version__}")
from kfp import dsl, compiler

@dsl.component
def add(a: int = 1, b: int = 2) -> int:
    print(f"{a} + {b} = {a + b}")
    return a + b
@dsl.pipeline(name="first-pipeline")
def hello_world():
    add()
compiler.Compiler().compile(hello_world, "first-pipeline.yaml")
