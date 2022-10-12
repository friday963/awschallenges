import boto3
import json

def lambda_handler(event, context):
    client = boto3.resource('dynamodb', region_name="us-east-1")
   
    table_name = 'VisitsCount'
    params = {
        'TableName': table_name,
        'KeySchema': [
            {'AttributeName': 'partition_key', 'KeyType': 'HASH'},
            {'AttributeName': 'sort_key', 'KeyType': 'RANGE'},
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'partition_key', 'AttributeType': 'N'},
            {'AttributeName': 'sort_key', 'AttributeType': 'N'},
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    }
    table = client.create_table(**params)
    print(f"Creating {table_name}...")
    table.wait_until_exists()

    return {
        'statusCode': 200,
        'body': table
    }