"""Submit the compiled pipeline to a Kubeflow Pipelines instance."""

import argparse
import kfp
from kfp import client


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="http://localhost:8080")
    parser.add_argument("--package", default="pipeline.yaml")
    parser.add_argument("--experiment", default="kubeflow-pipeline-demo")
    args = parser.parse_args()

    kfp_client = client.Client(host=args.host)
    run = kfp_client.create_run_from_pipeline_package(
        pipeline_file_path=args.package,
        experiment_name=args.experiment,
    )
    print(f"Run submitted — ID: {run.run_id}")


if __name__ == "__main__":
    main()
