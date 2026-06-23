"""Data loading and preprocessing helpers extracted from the Metaflow flow.

Kept separate from flow.py so they can be unit-tested without the Metaflow runtime.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_and_split_data(test_size=0.2, random_state=42):
    """Load Iris dataset and split into train/test sets."""
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data,
        iris.target,
        test_size=test_size,
        random_state=random_state,
        stratify=iris.target,
    )
    return X_train, X_test, y_train, y_test, list(iris.target_names)


def scale_features(X_train, X_test):
    """Fit a StandardScaler on the training set and transform both sets."""
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled
