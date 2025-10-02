#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_ascella_dev.network_stack import NetworkStack
from cdk_ascella_dev.config import config


ENVIRONMENT = cdk.Environment(
    account=config['account'],
    region=config['region'],
)

app = cdk.App()

NetworkStack(
    app,
    'NetworkStack',
    env=ENVIRONMENT,
    termination_protection=True,
)

app.synth()
