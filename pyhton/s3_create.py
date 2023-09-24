import boto3
import os
import time

region = os.getenv('region')
bucket_name = os.getenv('s3_name')

s3_client = boto3.client('s3', region_name=os.getenv('region'))

s3_resource=boto3.resource( 's3', region_name=os.getenv('region'))

def create_bucket(bucket_name, region):
    location = {'LocationConstraint': region}
    s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    print(f' Bucket {bucket_name} has been created')
    time.sleep(5)
create_bucket(bucket_name, region)