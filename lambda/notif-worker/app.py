import json

def handler(event, context):
    print("Notification Worker triggered:", json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps('Notification processed successfully')
    }
