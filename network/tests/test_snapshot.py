import pytest
import aws_cdk as cdk
import json
from cdk_ascella_dev.network_stack import NetworkStack

from aws_cdk.assertions import Template

ENVIRONMENT = cdk.Environment(
    account='testing',
    region='testing'
)


def test_match_with_snapshot(snapshot):
    app = cdk.App()
    stack = NetworkStack(app, 'NetworkStack', env=ENVIRONMENT)
    template = Template.from_stack(stack)
    snapshot.assert_match(
        json.dumps(
            template.to_json(),
            indent=4,
            sort_keys=True
        ),
        'network_stack_template.json'
    )
