#!/usr/bin/env python3
import boto3
import argparse
# Please note that by default boto will check credentials in AWS env variables.
# AWS_ACCESS_KEY_ID - The access key for your AWS account.
# AWS_SECRET_ACCESS_KEY - The secret key for your AWS account.
# AWS_SESSION_TOKEN - The session key for your AWS account.
# if you want to specify them directly use the following snippet
# session = boto3.Session(
#         aws_access_key_id='<your_access_key_id>',
#         aws_secret_access_key='<your_secret_access_key>')

parser = argparse.ArgumentParser()
parser.add_argument('--bucket-name', type=str, required=True)
parser.add_argument('--string', type=str, required=True)
args = parser.parse_args()
search_string = args.string
session = boto3.Session()

s3 = session.resource('s3')

my_bucket = s3.Bucket(args.bucket_name)

for obj in my_bucket.objects.all():
    if obj.key.endswith('txt'):
        body = obj.get()['Body'].read()
        body = body.decode('utf8')
        if search_string in body:
            count = body.count(search_string)
            print("String:", search_string, 'Found in File:', obj.key, "occurs in file ", count, "times")
