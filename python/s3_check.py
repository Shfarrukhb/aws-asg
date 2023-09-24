import boto3 
import time 
import os 
 
region = os.getenv('region')
bucket_name = os.getenv('s3_name')
s3_list = [] 
 
s3_client = boto3.client('s3', region_name=os.getenv('region') )
s3_resource = boto3.resource('s3', region_name=os.getenv('region') ) 
 
#get the list of all buckets 
for bucket in s3_client.list_buckets()['Buckets']: 
       s3_list.append(bucket["Name"]) 
 
#function to check bucket 
def check_bucket(bucket_name, region): 
    if bucket_name in s3_list: 
        print(bucket_name + " already exists")
        print(f'::set-output name=s3_chr::{"Yes"}')
    else: 
        print("Bucket " + bucket_name + " doesn't exist")
        print(f'::set-output name=s3_chr::{None}')
check_bucket(bucket_name, region)