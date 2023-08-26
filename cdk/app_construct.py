from typing import Any, Self

from constructs import Construct

from cdk.lmd_construct import LambdaConstruct


class AppConstruct(Construct):
    def __init__(
        self: Self,
        scope: Construct,
        construct_id: str,
        **kwargs: Any,  # noqa: ANN401
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.hello = LambdaConstruct(self, "hello")
