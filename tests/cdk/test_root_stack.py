import json

import aws_cdk as cdk
from aws_cdk import assertions
from aws_cdk import integ_tests_alpha as integ_tests
from syrupy.matchers import path_type

from cdk.root_stack import RootStack


def test_snapshot(snapshot) -> None:
    app = cdk.Stack()
    stack = RootStack(app, "test")
    template = assertions.Template.from_stack(stack)

    matcher = path_type(
        {
            r".*\.S3Key$": (str,),
        },
        regex=True,
    )
    assert template.to_json() == snapshot(matcher=matcher)


def test_integ() -> None:
    app = cdk.Stack()
    stack = RootStack(app, "test")
    integ = integ_tests.IntegTest(
        scope=app,
        id="integ_test",
        test_cases=[stack],
        regions=[stack.region],
    )

    invoke = integ.assertions.invoke_function(
        function_name=stack.app.hello.function.function_name,
    )
    invoke.expect(
        integ_tests.ExpectedResult.object_like(
            expected={
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
            },
        ),
    )
