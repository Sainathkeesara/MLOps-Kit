"""Submit the compiled pipeline to Kubeflow Pipelines."""

import argparse
import kfp
from kfp import client


def main():
    parser = argparse.ArgumentParser(description="Submit pipeline to Kubeflow")
    parser.add_argument("--host", default="http://localhost:8080", help="KFP API host URL")
    parser.add_argument("--package", default="pipeline.yaml", help="Pipeline package path")
    parser.add_argument("--experiment", default="kubeflow-pipeline-scaffold", help="Experiment name")
    parser.add_argument("--alpha", type=float, default=0.5, help="ElasticNet alpha parameter")
    parser.add_argument("--l1-ratio", type=float, default=0.1, help="ElasticNet l1_ratio parameter")
    args = parser.parse_args()

    kfp_client = client.Client(host=args.host)
    run = kfp_client.create_run_from_pipeline_package(
        pipeline_file_path=args.package,
        arguments={
            "alpha": args.alpha,
            "l1-ratio": args.l1_ratio,
        },
        experiment_name=args.experiment,
    )
    print(f"Run submitted — ID: {run.run_id}")


if __name__ == "__main__":
    main()