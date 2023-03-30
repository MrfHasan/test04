import json

def lambda_handler(event, context):
    message = "Hello, GIM!"
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
