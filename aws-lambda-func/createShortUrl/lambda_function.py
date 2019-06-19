import json
import boto3
import os
from short_url_generator import short_url_generator
def lambda_handler(event, context):



 # get the instance id that triggered the event


  url = event['postData']['url']
  customDomain = event['postData']['customDomain']

  bucket=event['postData']['bucket']
  short_url,token=short_url_generator(8).generate_short_url(customDomain)

  s3 = boto3.client('s3')

  s3.put_object(ACL='public-read',Bucket=bucket, Key=token, WebsiteRedirectLocation=url,ContentType='text/html')

  return {'statusCode': 200,
          'body': json.dumps({'short_url' :short_url,'url': url, 'token': token})}

