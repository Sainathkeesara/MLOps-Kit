"""Extracted evaluation logic for unit testing without KFP runtime."""


def evaluate_predictions(predictions, random_state: int = 42):
    """Evaluate predictions against ground truth.

    This function encapsulates the core evaluation logic without KFP dependencies,
    enabling unit testing of the evaluation behavior.

    Args:
        predictions: Model predictions to evaluate.
        random_state: Random seed for reproducibility.

    Returns:
        Tuple of (rmse, mae) metrics.
    """
    import numpy as np
    from sklearn.datasets import load_diabetes
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, mean_absolute_error

    data = load_diabetes()
    _, X_test, _, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=random_state
    )

    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    mae = mean_absolute_error(y_test, predictions)

    return rmse, mae