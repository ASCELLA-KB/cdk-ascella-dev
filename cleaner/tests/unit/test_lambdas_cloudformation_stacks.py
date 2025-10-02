import pytest

from moto import mock_cloudformation
from moto import mock_sqs

from dateutil.parser import isoparse


@pytest.fixture(scope='function')
def aws_credentials():
    import os
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'
    os.environ['AWS_DEFAULT_REGION'] = 'us-west-1'


@pytest.fixture
def raw_stacks():
    return [
        {
            'StackId': 'arn:aws:cloudformation:us-west-2:116837888204:stack/igvf-ui-IGVF-246-remove-uuid-as-unique-key-for-treatments-DeployDevelopment-FrontendStack/c1f10110-27e3-11ed-b366-0add85ad3a49',
            'StackName': 'igvf-ui-IGVF-246-remove-uuid-as-unique-key-for-treatments-DeployDevelopment-FrontendStack',
            'ChangeSetId': 'arn:aws:cloudformation:us-west-2:116837888204:changeSet/PipelineChange/a70c18f4-7e13-4b25-87d0-1084ad6c0db7',
            'Parameters': [
                {
                    'ParameterKey': 'BootstrapVersion',
                    'ParameterValue': '/cdk-bootstrap/hnb659fds/version',
                    'ResolvedValue': '12'
                }
            ],
            'CreationTime': isoparse('2022-08-29T21:44:28.625000+00:00'),
            'LastUpdatedTime': '2022-08-29T21:45:09.301000+00:00',
            'RollbackConfiguration': {},
            'StackStatus': 'CREATE_COMPLETE',
            'DisableRollback': False,
            'NotificationARNs': [],
            'Capabilities': [
                'CAPABILITY_NAMED_IAM',
                'CAPABILITY_AUTO_EXPAND'
            ],
            'Outputs': [],
            'RoleARN': 'arn:aws:iam::116837888204:role/cdk-hnb659fds-cfn-exec-role-116837888204-us-west-2',
            'Tags': [
                {
                    'Key': 'environment',
                    'Value': 'demo'
                },
                {
                    'Key': 'project',
                    'Value': 'igvf-ui'
                },
                {
                    'Key': 'branch',
                    'Value': 'IGVF-246-remove-uuid-as-unique-key-for-treatments'
                },
                {
                    'Key': 'time-to-live-hours',
                    'Value': '72'
                },
                {
                    'Key': 'turn-off-on-friday-night',
                    'Value': 'yes'
                }
            ],
            'DriftInformation': {
                'StackDriftStatus': 'NOT_CHECKED'
            }
        },
        {
            'StackId': 'arn:a897-0200bc55add5',
            'StackName': 'igvf-ui-IGVF-246-remove-uuid-as-unique-key-for-treatments-DemoDeploymentPipelineStack',
            'ChangeSetId': 'arn:aw-660f9d9ebbe2',
            'Parameters': [
                {
                    'ParameterKey': 'BootstrapVersion',
                    'ParameterValue': '/cdk-bootstrap/hnb659fds/version',
                    'ResolvedValue': '12'
                }
            ],
            'CreationTime': isoparse('2022-08-29T21:37:45.616000+00:00'),
            'LastUpdatedTime': '2022-08-29T21:42:23.621000+00:00',
            'RollbackConfiguration': {},
            'StackStatus': 'UPDATE_COMPLETE',
            'DisableRollback': False,
            'NotificationARNs': [],
            'Capabilities': [
                'CAPABILITY_IAM',
                'CAPABILITY_NAMED_IAM',
                'CAPABILITY_AUTO_EXPAND'
            ],
            'RoleARN': 'arn:aws:i2',
            'Tags': [
                {
                    'Key': 'environment',
                    'Value': 'demo'
                },
                {
                    'Key': 'project',
                    'Value': 'igvf-ui'
                },
                {
                    'Key': 'branch',
                    'Value': 'IGVF-246-remove-uuid-as-unique-key-for-treatments'
                },
                {
                    'Key': 'time-to-live-hours',
                    'Value': '72'
                },
                {
                    'Key': 'turn-off-on-friday-night',
                    'Value': 'yes'
                }
            ],
            'DriftInformation': {
                'StackDriftStatus': 'NOT_CHECKED'
            }
        },
        {
            'StackId': 'arn:awployDevelopment-B79b-06581a792431',
            'StackName': 'igvfd-IGVF-t-BackendStack',
            'ChangeSetId': 'arn:aws:cloudformat26a6c2-26a5-469a-9d2a-f928092916ff',
            'Parameters': [
                {
                    'ParameterKey': 'BootstrapVersion',
                    'ParameterValue': '/cdk-bootstrap/hnb659fds/version',
                    'ResolvedValue': '12'
                }
            ],
            'CreationTime': isoparse('2022-08-29T21:30:01.345000+00:00'),
            'LastUpdatedTime': '2022-08-29T21:33:25.901000+00:00',
            'RollbackConfiguration': {},
            'StackStatus': 'CREATE_COMPLETE',
            'DisableRollback': False,
            'NotificationARNs': [],
            'Capabilities': [
                'CAPABILITY_NAMED_IAM',
                'CAPABILITY_AUTO_EXPAND'
            ],
            'Outputs': [],
            'RoleARN': 'arn:aws:iam::153-us-west-2',
            'Tags': [
                {
                    'Key': 'environment',
                    'Value': 'demo'
                },
                {
                    'Key': 'project',
                    'Value': 'igvfd'
                },
                {
                    'Key': 'branch',
                    'Value': 'IGVF-246-remove-uuid-as-unique-key-for-treatments'
                },
                {
                    'Key': 'time-to-live-hours',
                    'Value': '72'
                },
                {
                    'Key': 'turn-off-on-friday-night',
                    'Value': 'yes'
                }
            ],
            'DriftInformation': {
                'StackDriftStatus': 'NOT_CHECKED'
            }
        },
        {
            'StackId': 'arn:awsf-0a3616eba9df',
            'StackName': 'igvfd-IGVF-246-remove-uuid-as-unique-key-for-treatments-DeployDevelopment-PostgresStack',
            'ChangeSetId': 'arn:aws:clo96f6783a6d',
            'Parameters': [
                {
                    'ParameterKey': 'BootstrapVersion',
                    'ParameterValue': '/cdk-bootstrap/hnb659fds/version',
                    'ResolvedValue': '12'
                }
            ],
            'CreationTime': isoparse('2022-08-29T21:11:51.331000+00:00'),
            'LastUpdatedTime': '2022-08-29T21:14:18.227000+00:00',
            'RollbackConfiguration': {},
            'StackStatus': 'CREATE_COMPLETE',
            'DisableRollback': False,
            'NotificationARNs': [],
            'Capabilities': [
                'CAPABILITY_NAMED_IAM',
                'CAPABILITY_AUTO_EXPAND'
            ],
            'Outputs': [],
            'RoleARN': 'arn:aws:ias-west-2',
            'Tags': [
                {
                    'Key': 'environment',
                    'Value': 'demo'
                },
                {
                    'Key': 'project',
                    'Value': 'igvfd'
                },
                {
                    'Key': 'branch',
                    'Value': 'IGVF-246-remove-uuid-as-unique-key-for-treatments'
                },
                {
                    'Key': 'time-to-live-hours',
                    'Value': '72'
                },
                {
                    'Key': 'turn-off-on-friday-night',
                    'Value': 'yes'
                }
            ],
            'DriftInformation': {
                'StackDriftStatus': 'NOT_CHECKED'
            }
        },
        {
            'StackId': 'arn:aws:clo08aa3b72b',
            'StackName': 'igvfd-IGVF-246-remove-uuid-as-unique-key-for-treatments-DemoDeploymentPipelineStack',
            'ChangeSetId': 'arn:aws:cloafa4-490a4ffe80ed',
            'Parameters': [
                {
                    'ParameterKey': 'BootstrapVersion',
                    'ParameterValue': '/cdk-bootstrap/hnb659fds/version',
                    'ResolvedValue': '12'
                }
            ],
            'CreationTime': isoparse('2022-08-29T21:01:00.414000+00:00'),
            'LastUpdatedTime': '2022-08-29T21:06:37.189000+00:00',
            'RollbackConfiguration': {},
            'StackStatus': 'UPDATE_COMPLETE',
            'DisableRollback': False,
            'NotificationARNs': [],
            'Capabilities': [
                'CAPABILITY_IAM',
                'CAPABILITY_NAMED_IAM',
                'CAPABILITY_AUTO_EXPAND'
            ],
            'RoleARN': 'arn:aws:asdf',
            'Tags': [
                {
                    'Key': 'environment',
                    'Value': 'demo'
                },
                {
                    'Key': 'project',
                    'Value': 'igvfd'
                },
                {
                    'Key': 'branch',
                    'Value': 'IGVF-246-remove-uuid-as-unique-key-for-treatments'
                },
                {
                    'Key': 'time-to-live-hours',
                    'Value': '72'
                },
                {
                    'Key': 'turn-off-on-friday-night',
                    'Value': 'yes'
                }
            ],
            'DriftInformation': {
                'StackDriftStatus': 'NOT_CHECKED'
            }
        },
        {
            'StackId': 'arn:aws:cloud-11ed-9f05-025e315deee1',
            'StackName': 'ADemoCleaner',
            'ChangeSetId': 'arn:aws:cloudforma815-97df088bcc57',
            'Parameters': [
                {
                    'ParameterKey': 'BootstrapVersion',
                    'ParameterValue': '/cdk-bootstrap/hnb659fds/version',
                    'ResolvedValue': '12'
                }
            ],
            'CreationTime': isoparse('2022-08-27T00:29:50.795000+00:00'),
            'LastUpdatedTime': '2022-08-27T01:48:07.103000+00:00',
            'RollbackConfiguration': {},
            'StackStatus': 'UPDATE_COMPLETE',
            'DisableRollback': False,
            'NotificationARNs': [],
            'Capabilities': [
                'CAPABILITY_IAM',
                'CAPABILITY_NAMED_IAM',
                'CAPABILITY_AUTO_EXPAND'
            ],
            'RoleARN': 'arn:aws:i09189702753-us-west-2',
            'Tags': [],
            'DriftInformation': {
                'StackDriftStatus': 'NOT_CHECKED'
            }
        },
        {
            'StackId': 'arn:aws:11ed-a287-06b070a61763',
            'StackName': 'igvfd-dev-PipelineStack',
            'ChangeSetId': 'arn:b9-4a57-a88e-db637304de4c',
            'Parameters': [
                {
                    'ParameterKey': 'BootstrapVersion',
                    'ParameterValue': '/cdk-bootstrap/hnb659fds/version',
                    'ResolvedValue': '12'
                }
            ],
            'CreationTime': isoparse('2022-08-06T01:10:09.377000+00:00'),
            'LastUpdatedTime': '2022-08-27T01:25:47.997000+00:00',
            'RollbackConfiguration': {},
            'StackStatus': 'UPDATE_COMPLETE',
            'DisableRollback': False,
            'NotificationARNs': [],
            'Capabilities': [
                'CAPABILITY_IAM',
                'CAPABILITY_NAMED_IAM',
                'CAPABILITY_AUTO_EXPAND'
            ],
            'RoleARN': 'arn:aws:iam::116837888204:role/cdk-hnb659fds-cfn-exec-role-116837888204-us-west-2',
            'Tags': [
                {
                    'Key': 'environment',
                    'Value': 'dev'
                },
                {
                    'Key': 'project',
                    'Value': 'igvfd'
                },
                {
                    'Key': 'branch',
                    'Value': 'dev'
                }
            ],
            'DriftInformation': {
                'StackDriftStatus': 'NOT_CHECKED'
            }
        },
        {
            'StackId': 'arn:ab3f2-02e5320c21fd',
            'StackName': 'igvf-ui-dev-FrontendStack',
            'ChangeSetId': 'arcb873e9a19',
            'Parameters': [
                {
                    'ParameterKey': 'BootstrapVersion',
                    'ParameterValue': '/cdk-bootstrap/hnb659fds/version',
                    'ResolvedValue': '12'
                }
            ],
            'CreationTime': isoparse('2022-07-01T23:23:04.501000+00:00'),
            'LastUpdatedTime': '2022-08-27T01:24:22.655000+00:00',
            'RollbackConfiguration': {},
            'StackStatus': 'UPDATE_COMPLETE',
            'DisableRollback': False,
            'NotificationARNs': [],
            'Capabilities': [
                'CAPABILITY_NAMED_IAM',
                'CAPABILITY_AUTO_EXPAND'
            ],
            'Outputs': [],
            'RoleARN': 'arn:aws:iam::116837888204:role/cdk-hnb659fds-cfn-exec-role-116837888204-us-west-2',
            'Tags': [
                {
                    'Key': 'environment',
                    'Value': 'dev'
                },
                {
                    'Key': 'project',
                    'Value': 'igvf-ui'
                },
                {
                    'Key': 'branch',
                    'Value': 'dev'
                }
            ],
            'DriftInformation': {
                'StackDriftStatus': 'NOT_CHECKED'
            }
        },
        {
            'StackId': 'arn:a31df5fe15',
            'StackName': 'igvf-ui-dev-PipelineStack',
            'ChangeSetId': 'arn:a9-8134-7e9bd915c913',
            'Parameters': [
                {
                    'ParameterKey': 'BootstrapVersion',
                    'ParameterValue': '/cdk-bootstrap/hnb659fds/version',
                    'ResolvedValue': '12'
                }
            ],
            'CreationTime': isoparse('2022-07-01T23:16:24.747000+00:00'),
            'LastUpdatedTime': '2022-08-27T01:18:45.261000+00:00',
            'RollbackConfiguration': {},
            'StackStatus': 'UPDATE_COMPLETE',
            'DisableRollback': False,
            'NotificationARNs': [],
            'Capabilities': [
                'CAPABILITY_IAM',
                'CAPABILITY_NAMED_IAM',
                'CAPABILITY_AUTO_EXPAND'
            ],
            'RoleARN': 'arn:aws:iam::116837888204:role/cdk-hnb659fds-cfn-exec-role-116837888204-us-west-2',
            'Tags': [
                {
                    'Key': 'environment',
                    'Value': 'dev'
                },
                {
                    'Key': 'project',
                    'Value': 'igvf-ui'
                },
                {
                    'Key': 'branch',
                    'Value': 'dev'
                }
            ],
            'DriftInformation': {
                'StackDriftStatus': 'NOT_CHECKED'
            }
        },
        {
            'StackId': 'arn:awfe-028fd645e8bb',
            'StackName': 'igvfd-dev-BackendStack',
            'ChangeSetId': 'arn:aws:ce21e23716',
            'Parameters': [
                {
                    'ParameterKey': 'BootstrapVersion',
                    'ParameterValue': '/cdk-bootstrap/hnb659fds/version',
                    'ResolvedValue': '12'
                }
            ],
            'CreationTime': '2022-07-01T21:51:21.750000+00:00',
            'LastUpdatedTime': '2022-08-27T01:36:39.056000+00:00',
            'RollbackConfiguration': {},
            'StackStatus': 'UPDATE_COMPLETE',
            'DisableRollback': False,
            'NotificationARNs': [],
            'Capabilities': [
                'CAPABILITY_NAMED_IAM',
                'CAPABILITY_AUTO_EXPAND'
            ],
            'Outputs': [],
            'RoleARN': 'arn:aws:iam::116837888204:role/cdk-hnb659fds-cfn-exec-role-116837888204-us-west-2',
            'Tags': [
                {
                    'Key': 'environment',
                    'Value': 'dev'
                },
                {
                    'Key': 'project',
                    'Value': 'igvfd'
                },
                {
                    'Key': 'branch',
                    'Value': 'dev'
                }
            ],
            'DriftInformation': {
                'StackDriftStatus': 'NOT_CHECKED'
            }
        },
        {
            'StackId': 'arn:c-996e-02221f54d185',
            'StackName': 'igvfd-dev-PostgresStack',
            'ChangeSetId': 'arn:aws-2f8e-4efc-b990-ec5335be288d',
            'Parameters': [
                {
                    'ParameterKey': 'BootstrapVersion',
                    'ParameterValue': '/cdk-bootstrap/hnb659fds/version',
                    'ResolvedValue': '12'
                }
            ],
            'CreationTime': '2022-07-01T21:43:56.081000+00:00',
            'LastUpdatedTime': '2022-08-27T01:33:35.628000+00:00',
            'RollbackConfiguration': {},
            'StackStatus': 'UPDATE_COMPLETE',
            'DisableRollback': False,
            'NotificationARNs': [],
            'Capabilities': [
                'CAPABILITY_NAMED_IAM',
                'CAPABILITY_AUTO_EXPAND'
            ],
            'Outputs': [
            ],
            'RoleARN': 'arn:aws:iam::116837888204:role/cdk-hnb659fds-cfn-exec-role-116837888204-us-west-2',
            'Tags': [
                {
                    'Key': 'environment',
                    'Value': 'dev'
                },
                {
                    'Key': 'project',
                    'Value': 'igvfd'
                },
                {
                    'Key': 'branch',
                    'Value': 'dev'
                }
            ],
            'DriftInformation': {
                'StackDriftStatus': 'NOT_CHECKED'
            }
        },
        {
            'StackId': 'ar7',
            'StackName': 'igvfd-dev-ContinuousIntegrationStack',
            'ChangeSetId': 'arn:a0da6f11e84c',
            'Parameters': [
                {
                    'ParameterKey': 'BootstrapVersion',
                    'ParameterValue': '/cdk-bootstrap/hnb659fds/version',
                    'ResolvedValue': '12'
                }
            ],
            'CreationTime': '2022-05-06T18:54:10.925000+00:00',
            'LastUpdatedTime': '2022-08-27T01:31:39.445000+00:00',
            'RollbackConfiguration': {},
            'StackStatus': 'UPDATE_COMPLETE',
            'DisableRollback': False,
            'NotificationARNs': [],
            'Capabilities': [
                'CAPABILITY_NAMED_IAM',
                'CAPABILITY_AUTO_EXPAND'
            ],
            'RoleARN': 'arnt-2',
            'Tags': [
                {
                    'Key': 'environment',
                    'Value': 'dev'
                },
                {
                    'Key': 'project',
                    'Value': 'igvfd'
                },
                {
                    'Key': 'branch',
                    'Value': 'dev'
                }
            ],
            'DriftInformation': {
                'StackDriftStatus': 'NOT_CHECKED'
            }
        },
        {
            'StackId': 'a-b948-026296963731',
            'StackName': 'ationStack',
            'ChangeSetId': 'ac-e6373929fa3e',
            'Parameters': [
            ],
            'CreationTime': '2022-04-27T02:45:49.120000+00:00',
            'LastUpdatedTime': '2022-08-18T22:13:24.847000+00:00',
            'RollbackConfiguration': {},
            'StackStatus': 'UPDATE_IN_PROGRESS',
            'DisableRollback': False,
            'NotificationARNs': [],
            'Capabilities': [
                'CAPABILITY_IAM',
                'CAPABILITY_NAMED_IAM',
                'CAPABILITY_AUTO_EXPAND'
            ],
            'RoleARN': '9189702753-us-west-2',
            'Tags': [],
            'DriftInformation': {
                'StackDriftStatus': 'NOT_CHECKED'
            }
        },
        {
            'StackId': 'c-8d62-02c473568391',
            'StackName': 'astack',
            'ChangeSetId': 'a-42d5-9d53-2902915adeb8',
            'Parameters': [
                {
                    'ParameterKey': 'BootstrapVersion',
                    'ParameterValue': '/cdk-bootstrap/hnb659fds/version',
                    'ResolvedValue': '12'
                }
            ],
            'CreationTime': '2022-04-23T02:42:01.444000+00:00',
            'LastUpdatedTime': '2022-04-23T02:42:07.317000+00:00',
            'RollbackConfiguration': {},
            'StackStatus': 'CREATE_COMPLETE',
            'DisableRollback': False,
            'NotificationARNs': [],
            'Capabilities': [
                'CAPABILITY_IAM',
                'CAPABILITY_NAMED_IAM',
                'CAPABILITY_AUTO_EXPAND'
            ],
            'RoleARN': 'arn:3-us-west-2',
            'Tags': [],
            'DriftInformation': {
                'StackDriftStatus': 'NOT_CHECKED'
            }
        },
        {
            'StackId': 'abc',
            'StackName': 'cdet',
            'ChangeSetId': 'adf6',
            'Description': 'This stack includes resources needed to deploy AWS CDK apps into this environment',
            'Parameters': [
            ],
            'CreationTime': '2022-04-23T01:04:35.229000+00:00',
            'LastUpdatedTime': '2022-04-23T01:04:41.056000+00:00',
            'RollbackConfiguration': {},
            'StackStatus': 'CREATE_COMPLETE',
            'DisableRollback': False,
            'NotificationARNs': [],
            'Capabilities': [
                'CAPABILITY_IAM',
                'CAPABILITY_NAMED_IAM',
                'CAPABILITY_AUTO_EXPAND'
            ],
            'Outputs': [],
            'Tags': [],
            'DriftInformation': {
                'StackDriftStatus': 'NOT_CHECKED'
            }
        }
    ]


@mock_cloudformation
def test_lambdas_cloudformation_stacks_get_cloudformation_client(aws_credentials):
    from cleaner.lambdas.cloudformation.stacks import get_cloudformation_client
    client = get_cloudformation_client()
    assert hasattr(client, 'describe_stacks')


@mock_cloudformation
def test_lambdas_cloudformation_stacks_get_describe_stacks_paginator(aws_credentials):
    from cleaner.lambdas.cloudformation.stacks import get_cloudformation_client
    from cleaner.lambdas.cloudformation.stacks import get_describe_stacks_paginator
    client = get_cloudformation_client()
    paginator = get_describe_stacks_paginator(client)
    assert paginator.__class__.__name__ == 'CloudFormation.Paginator.DescribeStacks'
    assert hasattr(paginator, 'paginate')


@mock_cloudformation
def test_lambdas_cloudformation_stacks_get_all_stacks(aws_credentials):
    from cleaner.lambdas.cloudformation.stacks import get_cloudformation_client
    from cleaner.lambdas.cloudformation.stacks import get_describe_stacks_paginator
    from cleaner.lambdas.cloudformation.stacks import get_all_stacks
    client = get_cloudformation_client()
    paginator = get_describe_stacks_paginator(client)
    stacks = get_all_stacks(paginator)
    assert stacks == []


def test_lambdas_cloudformation_stacks_filter_stacks_by_statuses(raw_stacks):
    from cleaner.lambdas.cloudformation.stacks import filter_stacks_by_statuses
    assert len(raw_stacks) == 15
    filtered_stacks = filter_stacks_by_statuses(raw_stacks)
    assert len(filtered_stacks) == 14


def test_lambdas_cloudformation_stacks_get_tag_by_key(raw_stacks):
    from cleaner.lambdas.cloudformation.stacks import get_tag_by_key
    tag = get_tag_by_key(raw_stacks[0], 'time-to-live-hours')
    assert tag == {'Key': 'time-to-live-hours', 'Value': '72'}
    tag = get_tag_by_key(raw_stacks[0], 'key-that-does-not-exist')
    assert tag is None


def test_lambdas_cloudformation_stacks_get_time_to_live_hours_tag_or_none(raw_stacks):
    from cleaner.lambdas.cloudformation.stacks import get_time_to_live_hours_tag_or_none
    assert get_time_to_live_hours_tag_or_none(
        raw_stacks[0]) == {'Key': 'time-to-live-hours', 'Value': '72'}
    assert get_time_to_live_hours_tag_or_none(raw_stacks[10]) is None


def test_lambdas_cloudformation_stacks_stack_has_time_to_live_hours_tag(raw_stacks):
    from cleaner.lambdas.cloudformation.stacks import stack_has_time_to_live_hours_tag
    assert stack_has_time_to_live_hours_tag(raw_stacks[0])
    assert not stack_has_time_to_live_hours_tag(raw_stacks[10])


def test_lambdas_cloudformation_stacks_filter_stacks_with_time_to_live_hours_tag(raw_stacks):
    from cleaner.lambdas.cloudformation.stacks import filter_stacks_with_time_to_live_hours_tag
    filtered_stacks = filter_stacks_with_time_to_live_hours_tag(raw_stacks)
    assert len(filtered_stacks) == 5


def test_lambdas_cloudformation_stacks_get_turn_off_on_friday_night_tag_or_none(raw_stacks):
    from cleaner.lambdas.cloudformation.stacks import get_turn_off_on_friday_night_tag_or_none
    assert get_turn_off_on_friday_night_tag_or_none(
        raw_stacks[0]) == {'Key': 'turn-off-on-friday-night', 'Value': 'yes'}
    assert get_turn_off_on_friday_night_tag_or_none(raw_stacks[10]) is None


def test_lambdas_cloudformation_stacks_stack_has_turn_off_on_friday_night_tag(raw_stacks):
    from cleaner.lambdas.cloudformation.stacks import stack_has_turn_off_on_friday_night_tag
    assert stack_has_turn_off_on_friday_night_tag(raw_stacks[0])
    assert not stack_has_turn_off_on_friday_night_tag(raw_stacks[10])


def test_lambdas_cloudformation_stacks_filter_stacks_with_turn_off_on_friday_night_tag(raw_stacks):
    from cleaner.lambdas.cloudformation.stacks import filter_stacks_with_turn_off_on_friday_night_tag
    filtered_stacks = filter_stacks_with_turn_off_on_friday_night_tag(
        raw_stacks)
    assert len(filtered_stacks) == 5


def test_lambdas_cloudformation_stacks_get_stack_name(raw_stacks):
    from cleaner.lambdas.cloudformation.stacks import get_stack_name
    assert get_stack_name(
        raw_stacks[0]) == 'igvf-ui-IGVF-246-remove-uuid-as-unique-key-for-treatments-DeployDevelopment-FrontendStack'


def test_lambdas_cloudformation_stacks_get_creation_time(raw_stacks):
    from cleaner.lambdas.cloudformation.stacks import get_creation_time
    assert str(get_creation_time(
        raw_stacks[0])) == '2022-08-29 21:44:28.625000+00:00'


def test_lambdas_cloudformation_stacks_try_parse_time_to_live_hours_tag():
    from cleaner.lambdas.cloudformation.stacks import try_parse_time_to_live_hours_tag
    tag = {'Key': 'time-to-live-hours', 'Value': '72'}
    ttl = try_parse_time_to_live_hours_tag(tag)
    assert ttl == 72
    tag = {'Key': 'time-to-live-hours', 'Value': 'xyz72'}
    assert try_parse_time_to_live_hours_tag(tag) is None


def test_lambdas_cloudformation_stacks_get_current_utc_time():
    from cleaner.lambdas.cloudformation.stacks import get_current_utc_time
    import datetime
    now = get_current_utc_time()
    assert now.tzinfo == datetime.timezone.utc


def test_lambdas_cloudformation_stacks_get_current_pacific_time():
    from cleaner.lambdas.cloudformation.stacks import get_current_pacific_time
    import datetime
    from zoneinfo import ZoneInfo
    now = get_current_pacific_time()
    assert now.tzinfo == ZoneInfo('US/Pacific')


def test_lambdas_cloudformation_stacks_time_to_live_hours_exceeded(mocker):
    import datetime
    from dateutil.tz import tzutc
    from cleaner.lambdas.cloudformation.stacks import time_to_live_hours_exceeded
    from cleaner.lambdas.cloudformation.stacks import get_current_utc_time
    patched_current_time = mocker.patch(
        'cleaner.lambdas.cloudformation.stacks.get_current_utc_time')
    patched_current_time.return_value = datetime.datetime(
        2022, 8, 29, 21, 44, 28, 625000, tzinfo=tzutc())
    creation_time = datetime.datetime(
        2022, 8, 28, 21, 44, 28, 625000, tzinfo=tzutc())
    assert not time_to_live_hours_exceeded(creation_time, 26)
    assert time_to_live_hours_exceeded(creation_time, 24)


def test_lambdas_cloudformation_stacks_stack_is_alive_longer_than_time_to_live_hours(raw_stacks, mocker):
    import datetime
    from dateutil.tz import tzutc
    from cleaner.lambdas.cloudformation.stacks import stack_is_alive_longer_than_time_to_live_hours
    patched_current_time = mocker.patch(
        'cleaner.lambdas.cloudformation.stacks.get_current_utc_time')
    patched_current_time.return_value = datetime.datetime(
        2022, 8, 29, 21, 44, 28, 625000, tzinfo=tzutc())
    assert not stack_is_alive_longer_than_time_to_live_hours(raw_stacks[0])
    patched_current_time.return_value = datetime.datetime(
        2022, 9, 4, 21, 44, 28, 625000, tzinfo=tzutc())
    assert stack_is_alive_longer_than_time_to_live_hours(raw_stacks[0])


def test_lambdas_cloudformation_stacks_filter_stacks_living_longer_than_time_to_live_hours(raw_stacks, mocker):
    import datetime
    from dateutil.tz import tzutc
    from cleaner.lambdas.cloudformation.stacks import filter_stacks_living_longer_than_time_to_live_hours
    from cleaner.lambdas.cloudformation.stacks import filter_stacks_with_time_to_live_hours_tag
    patched_current_time = mocker.patch(
        'cleaner.lambdas.cloudformation.stacks.get_current_utc_time')
    patched_current_time.return_value = datetime.datetime(
        2022, 9, 4, 21, 44, 28, 625000, tzinfo=tzutc()
    )
    filtered_stacks = filter_stacks_living_longer_than_time_to_live_hours(
        filter_stacks_with_time_to_live_hours_tag(
            raw_stacks
        )
    )
    assert len(filtered_stacks) == 5


def test_lambdas_cloudformation_stacks_stack_has_turn_off_on_friday_night_yes_tag(raw_stacks):
    from cleaner.lambdas.cloudformation.stacks import stack_has_turn_off_on_friday_night_yes_tag
    from copy import deepcopy
    stack = deepcopy(raw_stacks[0])
    assert stack_has_turn_off_on_friday_night_yes_tag(
        stack
    )
    stack['Tags'][4]['Value'] = 'no'
    assert not stack_has_turn_off_on_friday_night_yes_tag(
        stack
    )
    stack['Tags'] = []
    assert not stack_has_turn_off_on_friday_night_yes_tag(
        stack
    )


def test_lambdas_cloudformation_stacks_filter_stacks_by_turn_off_on_friday_night_is_yes(raw_stacks, mocker):
    import datetime
    from zoneinfo import ZoneInfo
    from cleaner.lambdas.cloudformation.stacks import filter_stacks_by_turn_off_on_friday_night_is_yes
    filtered_stacks = filter_stacks_by_turn_off_on_friday_night_is_yes(
        raw_stacks
    )
    assert len(filtered_stacks) == 5


def test_lambdas_cloudformation_stacks_is_it_friday_night_in_LA_it_is_not(mocker):
    import datetime
    from zoneinfo import ZoneInfo
    from cleaner.lambdas.cloudformation.stacks import is_it_friday_night_in_LA
    patched_current_time = mocker.patch(
        'cleaner.lambdas.cloudformation.stacks.get_current_pacific_time')
    patched_current_time.return_value = datetime.datetime(
        2022, 9, 13, 15, 4, 30, 213339, tzinfo=ZoneInfo('US/Pacific'))
    assert is_it_friday_night_in_LA() == False


def test_lambdas_cloudformation_stacks_is_it_friday_night_in_LA_it_is(mocker):
    import datetime
    from zoneinfo import ZoneInfo
    from cleaner.lambdas.cloudformation.stacks import is_it_friday_night_in_LA
    patched_current_time = mocker.patch(
        'cleaner.lambdas.cloudformation.stacks.get_current_pacific_time')
    patched_current_time.return_value = datetime.datetime(
        2022, 9, 17, 2, 2, 22,  222222, tzinfo=ZoneInfo('US/Pacific'))
    assert is_it_friday_night_in_LA() == True


@mock_cloudformation
def test_lambdas_cloudformation_stacks_get_stacks_to_delete_because_of_time_to_live_hours_tag(aws_credentials, raw_stacks, mocker):
    import datetime
    from dateutil.tz import tzutc
    from cleaner.lambdas.cloudformation.stacks import get_stacks_to_delete_because_of_time_to_live_hours_tag
    patched_current_time = mocker.patch(
        'cleaner.lambdas.cloudformation.stacks.get_current_utc_time'
    )
    patched_current_time.return_value = datetime.datetime(
        2022, 9, 4, 21, 44, 28, 625000, tzinfo=tzutc()
    )
    patched_stacks = mocker.patch(
        'cleaner.lambdas.cloudformation.stacks.get_all_stacks'
    )
    patched_stacks.return_value = raw_stacks
    stacks_to_delete = get_stacks_to_delete_because_of_time_to_live_hours_tag()
    assert len(stacks_to_delete) == 5


@mock_cloudformation
def test_lambdas_cloudformation_stacks_get_stacks_to_delete_because_it_is_friday_night(aws_credentials, raw_stacks, mocker):
    import datetime
    from zoneinfo import ZoneInfo
    from cleaner.lambdas.cloudformation.stacks import get_stacks_to_delete_because_it_is_friday_night
    patched_stacks = mocker.patch(
        'cleaner.lambdas.cloudformation.stacks.get_all_stacks')
    patched_stacks.return_value = raw_stacks
    stacks_to_delete = get_stacks_to_delete_because_it_is_friday_night()
    assert len(stacks_to_delete) == 5


@mock_cloudformation
def test_lambdas_cloudformation_stacks_maybe_get_stacks_to_delete_because_it_is_friday_night(aws_credentials, raw_stacks, mocker):
    import datetime
    from zoneinfo import ZoneInfo
    from cleaner.lambdas.cloudformation.stacks import maybe_get_stacks_to_delete_because_it_is_friday_night
    patched_current_time = mocker.patch(
        'cleaner.lambdas.cloudformation.stacks.get_current_pacific_time'
    )
    patched_current_time.return_value = datetime.datetime(
        2022, 9, 4, 21, 44, 28, 625000, tzinfo=ZoneInfo('US/Pacific')
    )
    patched_stacks = mocker.patch(
        'cleaner.lambdas.cloudformation.stacks.get_all_stacks'
    )
    patched_stacks.return_value = raw_stacks
    stacks_to_delete = maybe_get_stacks_to_delete_because_it_is_friday_night()
    assert len(stacks_to_delete) == 0
    patched_current_time.return_value = datetime.datetime(
        2022, 9, 3, 6, 44, 28, 625000, tzinfo=ZoneInfo('US/Pacific')
    )
    stacks_to_delete = maybe_get_stacks_to_delete_because_it_is_friday_night()
    assert len(stacks_to_delete) == 5


def test_lambdas_cloudformation_stacks_get_stack_names_from_stacks(raw_stacks):
    from cleaner.lambdas.cloudformation.stacks import get_stack_names_from_stacks
    assert get_stack_names_from_stacks(raw_stacks) == [
        'igvf-ui-IGVF-246-remove-uuid-as-unique-key-for-treatments-DeployDevelopment-FrontendStack',
        'igvf-ui-IGVF-246-remove-uuid-as-unique-key-for-treatments-DemoDeploymentPipelineStack',
        'igvfd-IGVF-t-BackendStack',
        'igvfd-IGVF-246-remove-uuid-as-unique-key-for-treatments-DeployDevelopment-PostgresStack',
        'igvfd-IGVF-246-remove-uuid-as-unique-key-for-treatments-DemoDeploymentPipelineStack',
        'ADemoCleaner',
        'igvfd-dev-PipelineStack',
        'igvf-ui-dev-FrontendStack',
        'igvf-ui-dev-PipelineStack',
        'igvfd-dev-BackendStack',
        'igvfd-dev-PostgresStack',
        'igvfd-dev-ContinuousIntegrationStack',
        'ationStack',
        'astack',
        'cdet'
    ]


@mock_cloudformation
@mock_sqs
def test_lambdas_cloudformation_stacks_get_stacks_to_delete(aws_credentials, raw_stacks, mocker):
    import os
    import datetime
    import boto3
    from dateutil.tz import tzutc
    mocker.patch.dict(os.environ, {'DELETE_BRANCH_QUEUE_URL': 'abc'})
    boto3.client('sqs').create_queue(QueueName='abc')
    from cleaner.lambdas.cloudformation.stacks import get_stacks_to_delete
    patched_current_time = mocker.patch(
        'cleaner.lambdas.cloudformation.stacks.get_current_utc_time')
    patched_current_time.return_value = datetime.datetime(
        2022, 9, 4, 21, 44, 28, 625000, tzinfo=tzutc())
    patched_stacks = mocker.patch(
        'cleaner.lambdas.cloudformation.stacks.get_all_stacks')
    patched_stacks.return_value = raw_stacks
    stacks_to_delete = get_stacks_to_delete({}, {})
    assert list(sorted(stacks_to_delete)) == list(sorted([
        'igvfd-IGVF-t-BackendStack',
        'igvfd-IGVF-246-remove-uuid-as-unique-key-for-treatments-DemoDeploymentPipelineStack',
        'igvf-ui-IGVF-246-remove-uuid-as-unique-key-for-treatments-DemoDeploymentPipelineStack',
        'igvfd-IGVF-246-remove-uuid-as-unique-key-for-treatments-DeployDevelopment-PostgresStack',
        'igvf-ui-IGVF-246-remove-uuid-as-unique-key-for-treatments-DeployDevelopment-FrontendStack'
    ]))
