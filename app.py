from pathlib import Path

import aws_cdk as cdk
import tomllib
from aws_cdk import Tags

from cdk.root_stack import RootStack


def add_name_tag(scope):  # noqa: ANN001, ANN201
    for child in scope.node.children:
        if cdk.Resource.is_resource(child):
            Tags.of(child).add("Name", child.node.path.replace("/", "-"))
        add_name_tag(child)


pyproject_path = Path.cwd() / "pyproject.toml"
with pyproject_path.open("rb") as f:
    pyproject_tmol = tomllib.load(f)

app = cdk.App()

RootStack(
    scope=app,
    construct_id=pyproject_tmol["project"]["name"].replace("_", "-"),
)

Tags.of(app).add("Project", pyproject_tmol["project"]["name"])
add_name_tag(app)

app.synth()
