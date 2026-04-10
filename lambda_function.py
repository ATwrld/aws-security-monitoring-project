import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = "andre-security-logs-teamt"
    key = f"finding-{datetime.utcnow().isoformat()}.json"

    s3.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=json.dumps(event),
        ContentType="application/json"
    )

    return {
        "statusCode": 200,
        "body": "Finding saved to S3"
    }
