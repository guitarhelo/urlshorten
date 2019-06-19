import boto3
import os
def lambda_handler(event, context):
    token = event['token']
    bucket= event['bucket']

    s3 = boto3.client('s3')

    try:
      s3.delete_object(Bucket=bucket, Key=token)

      return {'statusCode': 200,'body': '{delete_object sucess}'}
    except Exception as e:
      print(e)
      raise e