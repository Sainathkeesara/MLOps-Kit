import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from train import train


def test_train_returns_run_id():
    with tempfile.TemporaryDirectory() as tmp:
        run_id = train(
            tracking_uri=f"file://{tmp}",
            experiment_name="test-exp",
            n_estimators=10,
            max_depth=3,
            test_size=0.3,
            random_state=42,
        )
    assert isinstance(run_id, str)
    assert len(run_id) > 0


def test_train_default_params_succeed():
    with tempfile.TemporaryDirectory() as tmp:
        run_id = train(
            tracking_uri=f"file://{tmp}",
            experiment_name="test-exp-default",
            n_estimators=50,
            max_depth=5,
            test_size=0.2,
            random_state=0,
        )
    assert run_id is not None
