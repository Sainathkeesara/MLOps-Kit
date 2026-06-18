import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


def parse_args():
    parser = argparse.ArgumentParser(description="KFP component: train a sklearn model")
    parser.add_argument(
        "--data-path",
        type=str,
        default="/data/dataset.csv",
        help="Path to the input CSV dataset",
    )
    parser.add_argument(
        "--target-col",
        type=str,
        default="target",
        help="Name of the target column in the dataset",
    )
    parser.add_argument(
        "--model-dir",
        type=str,
        default="/model",
        help="Directory where the trained model artifacts are written",
    )
    parser.add_argument(
        "--metrics-path",
        type=str,
        default="/metrics.json",
        help="Path to write evaluation metrics as JSON",
    )
    parser.add_argument(
        "--n-estimators",
        type=int,
        default=100,
        help="Number of trees in the random forest",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=None,
        help="Maximum tree depth (None for unlimited)",
    )
    parser.add_argument(
        "--test-size",
        type=float,
        default=0.2,
        help="Fraction of data to hold out for evaluation",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    data_path = Path(args.data_path)
    if not data_path.exists():
        print(f"ERROR: data file not found at {data_path}", file=sys.stderr)
        sys.exit(1)

    print(f"[train] Loading dataset from {data_path}")
    df = pd.read_csv(data_path)

    if args.target_col not in df.columns:
        print(
            f"ERROR: target column '{args.target_col}' not found in dataset. "
            f"Available columns: {list(df.columns)}",
            file=sys.stderr,
        )
        sys.exit(1)

    X = df.drop(columns=[args.target_col])
    y = df[args.target_col]

    numeric_cols = X.select_dtypes(include=[np.number]).columns
    X = X[numeric_cols]

    if X.shape[1] == 0:
        print("ERROR: no numeric feature columns found after dropping target", file=sys.stderr)
        sys.exit(1)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=args.test_size, random_state=42
    )

    print(f"[train] Training RandomForest with {args.n_estimators} trees, max_depth={args.max_depth}")
    model = RandomForestClassifier(
        n_estimators=args.n_estimators,
        max_depth=args.max_depth,
        random_state=42,
        n_jobs=-1,
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    model_dir = Path(args.model_dir)
    model_dir.mkdir(parents=True, exist_ok=True)

    import cloudpickle

    model_path = model_dir / "model.pkl"
    with open(model_path, "wb") as f:
        cloudpickle.dump(model, f)
    print(f"[train] Model saved to {model_path}")

    metrics = {
        "accuracy": accuracy,
        "n_estimators": args.n_estimators,
        "max_depth": args.max_depth,
        "test_size": args.test_size,
        "n_features": X.shape[1],
        "classification_report": report,
    }
    metrics_path = Path(args.metrics_path)
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"[train] Metrics written to {metrics_path}")

    print(f"[train] Accuracy: {accuracy:.4f}")
    print("[train] Component finished successfully")


if __name__ == "__main__":
    main()
