from aws_cdk import App
from aws_cdk import Stack
from aws_cdk import SecretValue

from aws_cdk.aws_iam import AccessKey
from aws_cdk.aws_iam import User
from aws_cdk.aws_iam import ManagedPolicy
from aws_cdk.aws_iam import PolicyStatement

from aws_cdk.aws_secretsmanager import Secret

from constructs import Construct

from bucket.bucket_storage import BucketStorage

from typing import Any


READ_ACCESSIBLE_PRODUCTION_RESOURCES = [
    'arn:aws:s3:::ascella-blobs',
    'arn:aws:s3:::ascella-blobs/*',
    'arn:aws:s3:::ascella-files',
    'arn:aws:s3:::ascella-files/*',
    'arn:aws:s3:::ascella-public',
    'arn:aws:s3:::ascella-public/*',
    'arn:aws:s3:::ascella-private',
    'arn:aws:s3:::ascella-private/*',
]


class BucketAccessPolicies(Stack):

    def __init__(
            self,
            scope: Construct,
            construct_id: str,
            bucket_storage: BucketStorage,
            **kwargs: Any
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.bucket_storage = bucket_storage

        self.download_ascella_files_policy_statement = PolicyStatement(
            sid='AllowReadFromFilesAndBlobsBuckets',
            resources=[
                self.bucket_storage.files_bucket.bucket_arn,
                self.bucket_storage.files_bucket.arn_for_objects('*'),
                self.bucket_storage.blobs_bucket.bucket_arn,
                self.bucket_storage.blobs_bucket.arn_for_objects('*'),
                self.bucket_storage.public_files_bucket.bucket_arn,
                self.bucket_storage.public_files_bucket.arn_for_objects('*'),
                self.bucket_storage.private_files_bucket.bucket_arn,
                self.bucket_storage.private_files_bucket.arn_for_objects('*'),
            ] + READ_ACCESSIBLE_PRODUCTION_RESOURCES,
            actions=[
                's3:GetObjectVersion',
                's3:GetObject',
                's3:GetBucketAcl',
                's3:ListBucket',
                's3:GetBucketLocation'
            ]
        )

        self.upload_ascella_files_policy_statement = PolicyStatement(
            sid='AllowReadAndWriteToFilesAndBlobsBuckets',
            resources=[
                self.bucket_storage.files_bucket.bucket_arn,
                self.bucket_storage.files_bucket.arn_for_objects('*'),
                self.bucket_storage.blobs_bucket.bucket_arn,
                self.bucket_storage.blobs_bucket.arn_for_objects('*'),
            ],
            actions=[
                's3:PutObject',
                's3:GetObjectVersion',
                's3:GetObject',
                's3:GetBucketAcl',
                's3:ListBucket',
                's3:GetBucketLocation',
            ]
        )

        self.federated_token_policy_statement = PolicyStatement(
            sid='AllowGenerateFederatedToken',
            resources=[
                '*',
            ],
            actions=[
                'iam:PassRole',
                'sts:GetFederationToken',
            ]
        )

        self.download_ascella_files_policy = ManagedPolicy(
            self,
            'DownloadAscellaFilesPolicy',
            managed_policy_name='download-ascella-files',
            statements=[
                self.download_ascella_files_policy_statement,
            ],
        )

        self.upload_ascella_files_policy = ManagedPolicy(
            self,
            'UploadAscellaFilesPolicy',
            managed_policy_name='upload-ascella-files',
            statements=[
                self.upload_ascella_files_policy_statement,
                self.federated_token_policy_statement,
            ],
        )

        self.upload_ascella_files_user = User(
            self,
            'UploadAscellaFilesUser',
            user_name='upload-ascella-files',
            managed_policies=[
                self.upload_ascella_files_policy,
            ]
        )

        self.upload_ascella_files_user_access_key = AccessKey(
            self,
            'UploadAscellaFilesUserAccessKey',
            user=self.upload_ascella_files_user,
        )

        self.upload_ascella_files_user_access_key_secret = Secret(
            self,
            'UploadAscellaFilesUserAccessKeySecret',
            secret_name='upload-ascella-files-user-access-key-secret',
            secret_object_value={
                'ACCESS_KEY': SecretValue.unsafe_plain_text(
                    self.upload_ascella_files_user_access_key.access_key_id,
                ),
                'SECRET_ACCESS_KEY': self.upload_ascella_files_user_access_key.secret_access_key,
            },
        )
