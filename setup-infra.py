import os

# Needed to avoid circular imports
import prefect

from prefect_aws.ecs import ECSTask
from prefect_aws import AwsCredentials


def setup_prefect_blocks():
  # Create an ECS Task Infra Block w/ cloudwatch logs set up
  aws_credentials_block = AwsCredentials.load("ecstask-credentials")

  ecs = ECSTask(
    aws_credentials=aws_credentials_block,
    image=f"hello-world",
    cpu=256,
    memory=512,
    stream_output=True,
    configure_cloudwatch_logs=True,
    execution_role_arn=os.environ.get('PREFECT_AGENT_EXECUTION_ROLE'),
  )
  print('made ecs task')

  ecs.save('prefect-ecs-cwl-repro-task', overwrite=True)
  print('saved it')

if __name__ == "__main__":
  setup_prefect_blocks()
