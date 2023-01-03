# prefect-ecs-cwl-error-repro

## Set up

1. Set up an environment file at `./env` with these variables filled in, or run in a shell with them already set.

    ```sh
    PREFECT_API_URL="your prefect setup"
    PREFECT_API_KEY="your prefect setup"
    AWS_SECRET_ACCESS_KEY="your secret creds"
    AWS_ACCESS_KEY_ID="your secret creds"
    PREFECT_AGENT_EXECUTION_ROLE="ARN of a role you'll use to start the ECS Task"
    ```

2. Install dependencies (will install via system, so maybe run this in a docker image or throwaway VM)

    ```sh
    # Export your env vars
    export $(cat env | xargs)

    # Install dependencies
    pip install -r requirements.txt

    # Setup prefect-aws
    prefect block register -m prefect_aws.credentials
    ```
