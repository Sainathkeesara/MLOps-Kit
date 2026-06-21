# Exploring the ZenML dashboard and configuring my first stack

I installed ZenML and ran `zenml up` to start the dashboard. It opened at `http://127.0.0.1:8237`. The UI is pretty minimal — a runs list, a pipelines list, and a stack config page. No experiment comparison view like W&B. It's more of a metadata browser.

I ran the pipeline from the primer and it showed up in the dashboard under Runs. Each step displays its status (cached or executed), input artifact URIs, and output artifacts. Useful for debugging.

Next I tried registering a custom stack. By default ZenML uses a local stack with SQLite metadata store and local artifact store. I registered an S3 artifact store:

```bash
zenml artifact-store register my_s3_store --flavor=s3 --path=s3://my-bucket
zenml stack register my_first_stack \
    -o default \
    -a my_s3_store
zenml stack set my_first_stack
```

The dashboard's stack page reflected the change immediately.

One gotcha: I set up the S3 artifact store but forgot AWS credentials. The first pipeline run failed with a `ClientError` from boto3. Fixed by exporting `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in my shell.

The dashboard is functional for checking run status and artifact locations. For deeper analysis I'd use the post-execution API or export runs somewhere else.
