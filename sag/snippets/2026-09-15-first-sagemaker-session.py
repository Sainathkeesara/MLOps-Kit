# last_verified: 2026-09-15 · sagemaker n/a
import sagemaker

session = sagemaker.Session()
# TODO: still fuzzy on how default bucket is picked — worked anyway
est = sagemaker.estimator.Estimator(image_uri, role, instance_count=1, instance_type="ml.m5.large", sagemaker_session=session)
est.fit({"training": "s3://my-bucket/my-data/"})
predictor = est.deploy(initial_instance_count=1, instance_type="ml.t2.medium")
print(predictor.predict({"features": [5.1, 3.5, 1.4, 0.2]}))
