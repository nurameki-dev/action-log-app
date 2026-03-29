import json
import boto3

dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):
    try:
        response = dynamodb_client.scan(
            TableName = 'action-log-table'
            )
        
        items = response['Items']

        return {
            'statusCode': 200,
            'body': json.dumps(items, ensure_ascii=False)
        }
    except Exception as e:
        return {
            'statusCode': 200,
            'body': json.dumps(f'エラー:{str(e)}')
        }
