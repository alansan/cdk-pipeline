#!/usr/bin/env python3
from aws_cdk import core as cdk
from cdk_pipeline.cdk_pipeline_stack import MyPipelineStack
import os

app = cdk.App()
MyPipelineStack(app, "MyPipelineStack", 
    env=cdk.Environment(
        account="644040437375", 
        region="eu-central-1")
)

app.synth()