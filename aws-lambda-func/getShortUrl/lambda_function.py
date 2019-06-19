import json
import boto3
def lambda_handler(event, context):


    token = event['token']
    bucket = event['bucket']

    s3 = boto3.client('s3')

    print(token)
    print(bucket)

    try:

      data=s3.get_object(Bucket=bucket, Key=token)

      WebsiteRedirectLocation=data['WebsiteRedirectLocation']

      return {'statusCode': 200,'body': {'WebsiteRedirectLocation':WebsiteRedirectLocation}}

    except Exception as e:
      print(e)
      raise e