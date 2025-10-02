import aws_cdk as cdk

from constructs import Construct

from aws_cdk.aws_chatbot import SlackChannelConfiguration

from aws_cdk.aws_sns import Topic

from cdk_ascella_dev.constructs.slack import SlackWebhook

from typing import Any


class NotificationStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.encode_dcc_chatbot: SlackChannelConfiguration = SlackChannelConfiguration(
            self,
            'encode-dcc-aws-chatbot',
            slack_channel_configuration_name='ascella-chatbot',
            slack_workspace_id='DNZS22NLX',
            slack_channel_id='C09JE732G94',
        )
        self.alarm_notification_topic = Topic(
            self,
            'AlarmNotificationTopic',
        )
        self.encode_dcc_chatbot.add_notification_topic(
            self.alarm_notification_topic
        )
        self.encode_dcc_slack_webhook: SlackWebhook = SlackWebhook(
            self,
            'AwsAscellaDevSlackWebhook',
        )
