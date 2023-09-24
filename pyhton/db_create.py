import boto3
import os

dynamodb = boto3.client('dynamodb', region_name="us-east-1")
db_table_name = os.getenv('db_table_name')

table = dynamodb.create_table(
    TableName=db_table_name,
    KeySchema=[
        {
            'AttributeName': 'LockID',
            'KeyType': 'HASH'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'LockID',
            'AttributeType': 'S'
        },
    ],
    BillingMode='PAY_PER_REQUEST'
)
print(db_table_name + " table has been created")