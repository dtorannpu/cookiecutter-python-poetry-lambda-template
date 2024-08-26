from http import HTTPStatus

from aws_lambda_powertools.utilities.typing import LambdaContext

def handler(event: dict, context: LambdaContext) -> dict:
    return {
        "statusCode": HTTPStatus.OK,
        "body": "ok",
    }
