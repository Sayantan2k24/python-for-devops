import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket = 'sayantan-demo-boto3-s3',
)
