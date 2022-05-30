import boto3
from botocore.handlers import disable_signing
import pandas as pd
print('Libs imported.')

def list_files():
    resource = boto3.resource('s3')
    resource.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)

    bucket = resource.Bucket('noaa-gfs-bdp-pds')
    #bucket = resource.Bucket('aws-earth-mo-atmospheric-global-prd')

    objects = bucket.objects.all()

    df = pd.DataFrame()
    
    for o in objects:
        print(o.key, ' ', o.last_modified, ' ', o.size)
        
        result = {
            'key': o.key,
            'last_modified': o.last_modified,
            'size': o.size
        }
        df = df.append(result, ignore_index=True)

    return df


if __name__ == '__main__':
    print('Start downloading')
    df = list_files()
    df.to_csv('query_results_bucket_files2.csv')
    # print(df)