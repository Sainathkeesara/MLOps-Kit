"""Extracted training logic for unit testing without KFP runtime."""


def train_model(alpha: float, l1_ratio: float, random_state: int = 42):
    """Train an ElasticNet model and return predictions.

    This function encapsulates the core training logic without KFP dependencies,
    enabling unit testing of the model training behavior.

    Args:
        alpha: ElasticNet regularization strength.
        l1_ratio: ElasticNet mixing parameter (0 for ridge, 1 for lasso).
        random_state: Random seed for reproducibility.

    Returns:
        Tuple of (predictions, rmse, mae) for validation.
    """
    import numpy as np
    from sklearn.linear_model import ElasticNet
    from sklearn.datasets import load_diabetes
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, mean_absolute_error

    data = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=random_state
    )

    model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    mae = mean_absolute_error(y_test, predictions)

    return predictions, rmse, mae


def get_data():
    """Load the diabetes dataset for pipeline testing.

    Returns:
        Bunch object with data and target arrays.
    """
    from sklearn.datasets import load_diabetes
    return load_diabetes()