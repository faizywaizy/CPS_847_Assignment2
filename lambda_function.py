import boto3 # amazon python sdk
import json

def lambda_handler(event, context):
    s3 = boto3.resource('s3') # s3 service object to work with
    bucket = 'cbueno-cps847'
    key = 'a2.json'
    
    file = s3.Object(bucket, key)
    file_content = file.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    
    fullName = json_content['first_name'] + " " + json_content['last_name']
    
    return {
        'statusCode' : 200,
        'output' : fullName
    }