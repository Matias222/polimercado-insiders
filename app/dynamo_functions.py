import boto3
import json
import os

from botocore.exceptions import ClientError
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

aws_access_key_id = os.getenv('amazon_access_key_id')
aws_secret_access_key = os.getenv('amazon_secret_access_key')

def write(valor:str,table_name="polimercado"):
   
    dynamodb = boto3.resource('dynamodb',aws_secret_access_key=aws_secret_access_key,aws_access_key_id=aws_access_key_id,region_name="us-east-1")

    table = dynamodb.Table(table_name)

    try:
        
        response = table.put_item(Item={"id":"ultima_hora","valor":valor})
        return response
    
    except ClientError as e:
    
        print(f"Error writing to {table_name}: {e.response['Error']['Message']}")
        return None
    
def read(key:str="ultima_hora",table_name="polimercado"):

    dynamodb = boto3.resource('dynamodb',aws_secret_access_key=aws_secret_access_key,aws_access_key_id=aws_access_key_id,region_name="us-east-1")

    table = dynamodb.Table(table_name)

    key={"id":key}

    try:
        
        response = table.get_item(Key=key)
        
        if 'Item' in response:
            return response['Item']
        else:
            print(f"No item found with the key {key} in table {table_name}")
            return None
        
    except ClientError as e:

        print(f"Error reading from {table_name}: {e.response['Error']['Message']}")
        return None