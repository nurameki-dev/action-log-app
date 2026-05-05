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
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(items, ensure_ascii=False)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'  # こちらにも追加推奨
            },
            'body': json.dumps(f'エラー:{str(e)}')
        }
