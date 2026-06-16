"""kub-010 — Kubeflow pipeline with conditional branching and resource constraints.

Demonstrates training a model, evaluating it, then conditionally deploying
or triggering a retrain notification based on the accuracy threshold.
Each component sets explicit CPU and memory limits.

This is one way to structure conditional logic in KFP v2; the docs also
show dsl.OneOf for mutually-exclusive branches, but Condition gives you
finer control when you need both branches to do something.
"""

from kfp import dsl, compiler
import kfp


@dsl.component(base_image="python:3.9-slim")
def preprocess_data(raw_text: str) -> str:
    per_line = raw_text.strip().splitlines()
    cleaned = [l for l in per_line if l and not l.startswith("#")]
    result = "\n".join(cleaned)
    print(f"preprocessed: {len(result)} chars from {len(per_line)} lines")
    return result


@dsl.component(base_image="python:3.9-slim")
def train_model(
    train_data: str,
    learning_rate: float,
    epochs: int,
) -> str:
    # ── simulating training ──
    n = len(train_data)
    model_ref = f"model-lr={learning_rate}-epochs={epochs}-samples={n}"
    print(f"trained {model_ref}")
    return model_ref


@dsl.component(base_image="python:3.9-slim")
def evaluate_model(model_path: str, test_data: str) -> float:
    # ── mock eval; a real component would load the model and run predictions ──
    score = min(0.5 + len(test_data) * 0.01, 0.95)
    print(f"eval: {model_path} → accuracy={score:.3f}")
    return score


@dsl.component(base_image="python:3.9-slim")
def deploy_model(model_path: str):
    print(f"deploying {model_path} to staging endpoint")
    # For a real deployment this would call KServe / Seldon or apply a k8s manifest.


@dsl.component(base_image="python:3.9-slim")
def request_retraining(accuracy: float):
    print(f"accuracy={accuracy:.3f} below threshold — scheduling retrain")


@dsl.pipeline(
    name="conditional-branching-pipeline",
    description="Train → eval → conditionally deploy or retrain, with resource limits",
    pipeline_root="s3://my-bucket/kfp-pipelines",
)
def conditional_pipeline(
    raw_text: str = "x,1\ny,2\n#comment\nz,3",
    learning_rate: float = 0.01,
    epochs: int = 10,
):
    prep = preprocess_data(raw_text=raw_text)
    prep.set_cpu_limit("500m").set_memory_limit("512Mi")

    train = train_model(
        train_data=prep.output,
        learning_rate=learning_rate,
        epochs=epochs,
    )
    train.set_cpu_limit("2").set_memory_limit("4Gi")

    evaluate = evaluate_model(
        model_path=train.output,
        test_data=prep.output,
    )
    evaluate.set_cpu_limit("1").set_memory_limit("2Gi")

    with dsl.Condition(evaluate.output > 0.8):
        deploy = deploy_model(model_path=train.output)
        deploy.set_cpu_limit("500m").set_memory_limit("1Gi")

    with dsl.Condition(evaluate.output <= 0.8):
        retrain = request_retraining(accuracy=evaluate.output)
        # no special resources needed for a notification step


if __name__ == "__main__":
    compiler.Compiler().compile(conditional_pipeline, "conditional-pipeline.yaml")

    # Port-forward the ml-pipeline service to localhost:8080 first:
    #   kubectl port-forward -n kubeflow svc/ml-pipeline 8080:80
    client = kfp.Client(host="http://localhost:8080")
    run = client.create_run_from_pipeline_func(
        conditional_pipeline,
        arguments={
            "raw_text": "a,1\nb,2\nc,3",
            "learning_rate": 0.05,
            "epochs": 20,
        },
        experiment_name="kub-010-test",
    )
    print(f"Submitted run: {run.run_id}")
