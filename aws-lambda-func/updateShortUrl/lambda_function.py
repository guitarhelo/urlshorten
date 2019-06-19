import json
import boto3

def lambda_handler(event, context):
    # TODO implement

    token  = event['token']
    bucket = event['bucket']
    url    = event['url']

    s3 = boto3.client('s3')
    try:

      s3.put_object(ACL='public-read',Bucket=bucket, Key=token, WebsiteRedirectLocation=url,ContentType='text/html')

      return {'statusCode': 200,'body': json.dumps({'url': url, 'token': token})}
    except Exception as e:
      print(e)
      raise e