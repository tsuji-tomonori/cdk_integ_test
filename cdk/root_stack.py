from typing import Any, Self

from aws_cdk import Stack
from constructs import Construct

from cdk.app_construct import AppConstruct


class RootStack(Stack):
    def __init__(
        self: Self,
        scope: Construct,
        construct_id: str,
        **kwargs: Any,  # noqa: ANN401
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.app = AppConstruct(self, "app")
