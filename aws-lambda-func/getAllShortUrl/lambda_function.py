import json
import boto3

def lambda_handler(event, context):
    # TODO implement


    responese_data=[]
    s3 = boto3.client("s3")

    #custom_domain=event['custom_domain']
    #bucket=event['bucket']

    custom_domain='https://panjingping.s3-ap-southeast-1.amazonaws.com'
    bucket='panjingping'

    all_objects = s3.list_objects(Bucket = bucket)





    id=1
    for obj in all_objects['Contents']:
      if obj['Key']!='admin/index.html':
        k = s3.head_object(Bucket = 'panjingping', Key =obj['Key'])
        #print(obj['Key'])
        #print(k['ContentType'])
        #print(k['WebsiteRedirectLocation'])
        responese={}
        responese['id']=id
        responese['url']=k['WebsiteRedirectLocation']
        responese['short_url']=custom_domain+'/'+obj['Key']
        responese['token']=obj['Key']
        #print(responese)
        responese_data.append(responese)

        id=id+1
        #print(responese_data)


    return {'statusCode': 200,
             'body': json.dumps(responese_data)}
