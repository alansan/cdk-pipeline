#!/usr/bin/env python3
from aws_cdk import core as cdk
from cdk_pipeline.cdk_pipeline_stack import MyPipelineStack
import os

app = cdk.App()
MyPipelineStack(app, "MyPipelineStack", 
    env=cdk.Environment(
        account=os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"]), 
        region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"]))
)

app.synth()