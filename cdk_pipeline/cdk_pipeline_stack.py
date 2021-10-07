from aws_cdk import core as cdk
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep, ManualApprovalStep
from cdk_pipeline.pipeline_app_stage import MyPipelineAppStage
import os

class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline", 
                        pipeline_name="MyPipeline",
                        synth=ShellStep("Synth", 
                            input=CodePipelineSource.git_hub("timofeic/cdk-pipeline", "master"),
                            commands=["npm install -g aws-cdk", 
                                "python -m pip install -r requirements.txt",
                                "cdk synth"]
                        ),
                        cross_account_keys=True
                    )

        test_stage = pipeline.add_stage(MyPipelineAppStage(self, "test",
            env=cdk.Environment(account="823500142645", region="eu-west-2")))

        test_stage.add_post(ManualApprovalStep('approval'))

        prod_stage = pipeline.add_stage(MyPipelineAppStage(self, "prod",
            env=cdk.Environment(account="017056865457", region="eu-west-1")))

        test_stage.add_post(ManualApprovalStep('approval'))