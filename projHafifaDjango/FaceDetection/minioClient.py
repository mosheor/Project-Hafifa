import boto3
from botocore.client import Config
import os
import botocore


s3 = boto3.client('s3',
    endpoint_url='http://%s:9000' % (os.environ['OBJ_STORE_IP']),
    aws_access_key_id=os.environ['KEY_ID'],
    aws_secret_access_key=os.environ['SECRET_KEY'],
    config=Config(signature_version='s3v4'))

bucket = 'images'

try:
    s3.head_bucket(Bucket=bucket)
except botocore.exceptions.ClientError:
    s3.create_bucket(Bucket=bucket)


def upload(file, object_name):
    s3.upload_fileobj(file, bucket, object_name)