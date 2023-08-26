import json

import aws_cdk as cdk
from aws_cdk import integ_tests_alpha as integ_tests
from aws_cdk.cloud_assembly_schema import CdkCommands, DestroyCommand, DestroyOptions

from cdk.root_stack import RootStack

app = cdk.App()
stack = RootStack(app, "test")
integ = integ_tests.IntegTest(
    scope=app,
    id="integ_test",
    test_cases=[stack],
    regions=[stack.region],
    cdk_command_options=CdkCommands(
        destroy=DestroyCommand(args=DestroyOptions(force=True)),
    ),
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

app.synth()
