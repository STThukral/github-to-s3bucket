import json

def lambda_handler(event, context):
    # Example Lambda code in Python
    response = {
        "statusCode": 200,
        "body": json.dumps("Hello, World from Python Lambda!")
    }
    return response