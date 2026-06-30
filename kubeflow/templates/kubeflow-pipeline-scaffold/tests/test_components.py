"""Tests for Kubeflow pipeline scaffold components."""

import sys
from pathlib import Path

# Add scripts directory to path for importing extracted logic
scripts_path = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(scripts_path))


def test_train_model_returns_valid_predictions():
    """Verify training produces predictions of correct shape."""
    from train_logic import train_model

    predictions, rmse, mae = train_model(alpha=0.5, l1_ratio=0.1)
    assert len(predictions) == 442
    assert 0.0 < rmse < 100.0
    assert 0.0 < mae < 50.0


def test_train_model_different_parameters():
    """Verify different hyperparameters produce different results."""
    from train_logic import train_model

    _, rmse_1, _ = train_model(alpha=0.1, l1_ratio=0.5)
    _, rmse_2, _ = train_model(alpha=1.0, l1_ratio=0.1)
    assert rmse_1 != rmse_2


def test_evaluate_predictions_consistent():
    """Verify evaluation metrics are consistent."""
    from train_logic import train_model
    from evaluate_logic import evaluate_predictions

    predictions, rmse_1, mae_1 = train_model(alpha=0.5, l1_ratio=0.1)
    rmse_2, mae_2 = evaluate_predictions(predictions)

    assert abs(rmse_1 - rmse_2) < 1e-10
    assert abs(mae_1 - mae_2) < 1e-10


def test_get_data_shapes():
    """Verify the diabetes dataset loads correctly."""
    from train_logic import get_data

    data = get_data()
    assert data.data.shape == (442, 10)
    assert len(data.target) == 442