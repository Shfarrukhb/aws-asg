import boto3 
import os
 
dynamodb = boto3.client('dynamodb', region_name="us-east-1") 
table_name = os.getenv('db_table_name')


# Check the DynamoDB table. 
def check_db(table_name): 
    if table_name in dynamodb.list_tables()["TableNames"]: 
        print(table_name + " already exists") 
        print(f'::set-output name=db_chr::{"Yes"}')
    else:  
        print(table_name + " doesn't exist")    
        print(f'::set-output name=db_chr::{None}')
check_db(table_name)