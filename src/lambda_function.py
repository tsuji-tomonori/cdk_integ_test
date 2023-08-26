import json
from typing import Any


def lambda_handler(
    event: dict[str, Any],
    context: Any,  # noqa: ANN401
) -> dict[str, Any]:
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, DELETE",
            "Access-Control-Allow-Credentials": True,
            "Access-Control-Allow-Headers": "origin, x-requested-with",
        },
        "body": json.dumps(
            {
                "message": "hello",
            },
        ),
        "isBase64Encoded": False,
    }
