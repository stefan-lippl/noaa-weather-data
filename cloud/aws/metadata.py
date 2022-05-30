import boto3
s3client = boto3.client('s3')

paginator = s3client.get_paginator('list_objects_v2')
page_iterator = paginator.paginate(Bucket='noaa-gfs-bdp-pds')
for bucket in page_iterator:
    for file in bucket['Contents']:
        print(file['Key'])
        try:
            metadata = s3client.head_object(Bucket='noaa-gfs-bdp-pds', Key=file['Key'])
            print(metadata)
        except:
            print("Failed {}".format(file['Key']))