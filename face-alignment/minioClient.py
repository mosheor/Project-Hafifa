import boto3
from botocore.client import Config
import os

# Create an S3 client
s3 = boto3.client('s3',
    endpoint_url='http://%s:9000' % (os.environ['OBJ_STORE_IP']),
    aws_access_key_id=os.environ['KEY_ID'],
    aws_secret_access_key=os.environ['SECRET_KEY'],
    config=Config(signature_version='s3v4'))


def download_file(bucket_name, file_name, location):
    s3.download_file(bucket_name, file_name, location)


def get_file(bucket_name, file_name):
    return s3.get_object(Bucket=bucket_name, Key=file_name)['Body']