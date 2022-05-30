import boto3

sess = boto3.Session(region_name='eu-central-1')

s3_client = sess.client('s3')

bucket_name = 'wef-wildfire-project'

bucket_list = s3_client.list_buckets()
print(bucket_list)

for bucket in bucket_list['Buckets']:
    print(bucket['Name'])