# last_verified: 2026-07-14 · databricks n/a

import mlflow
from mlflow.tracking import MlflowClient

TRACKING_URI = "databricks"
MODEL_NAME = "mlops_catalog.model_registry.sentiment_classifier"


def promote_to_staging(run_id: str) -> str:
    client = MlflowClient(tracking_uri=TRACKING_URI)
    model_uri = f"runs:/{run_id}/model"
    reg = mlflow.register_model(model_uri=model_uri, name=MODEL_NAME)
    print(f"Registered model version {reg.version} from run {run_id}")
    client.transition_model_version_stage(
        name=MODEL_NAME,
        version=reg.version,
        stage="Staging",
    )
    print(f"Promoted {MODEL_NAME} v{reg.version} → Staging")
    return reg.version


def promote_to_production(version: int) -> None:
    client = MlflowClient(tracking_uri=TRACKING_URI)
    current = client.get_latest_versions(MODEL_NAME, stages=["Production"])
    for mv in current:
        client.transition_model_version_stage(
            name=MODEL_NAME,
            version=mv.version,
            stage="Archived",
        )
        print(f"Archived previous Production version {mv.version}")
    client.transition_model_version_stage(
        name=MODEL_NAME,
        version=version,
        stage="Production",
    )
    print(f"Promoted {MODEL_NAME} v{version} → Production")


if __name__ == "__main__":
    with mlflow.start_run() as run:
        mlflow.log_param("model_type", "sentiment_classifier")
        mlflow.log_metric("val_accuracy", 0.92)
        run_id = run.info.run_id
    v = promote_to_staging(run_id)
    promote_to_production(v)
