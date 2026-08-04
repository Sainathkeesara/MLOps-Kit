# last_verified: 2026-08-04 · kubeflow v26.03

# I installed the KFP SDK and compiled my first pipeline
# Source: https://www.kubeflow.org/docs/started/installing-kubeflow/

import kfp
from kfp import dsl

client = kfp.Client()

@dsl.pipeline(name='first-pipeline')
def my_pipeline():
    pass

client.create_pipeline_from_func(my_pipeline, package_path='pipeline.yaml')
