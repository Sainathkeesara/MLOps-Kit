import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import mlflow
from register import register_and_promote, list_versions


def test_register_and_list_versions():
    with tempfile.TemporaryDirectory() as tmp:
        tracking_uri = f"file://{tmp}"

        mlflow.set_tracking_uri(tracking_uri)
        with mlflow.start_run() as run:
            mlflow.log_param("test", True)
            mlflow.sklearn.log_model(
                mlflow.sklearn.EmptyModel(),
                artifact_path="model",
            )

        version = register_and_promote(
            tracking_uri=tracking_uri,
            run_id=run.info.run_id,
            model_name="TestModel",
            stage="None",
        )
        assert isinstance(version, int)
        assert version >= 1

        versions = list_versions(tracking_uri, "TestModel")
        assert len(versions) >= 1
