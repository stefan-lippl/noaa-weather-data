import sys
sys.path.append('..')
import boto3
from argparse import ArgumentParser

class AWSCreateS3Bucket():
    """Creates a AWS S3 bucket"""
    def create_bucket(self, bucket_name:str, bucket_region:str = 'eu-central-1'):
        """
        bucket_name
            (required, str) Name of the bucket which should be created. Attention: must be unique in the whole AWS environment, not only in the own project
        bucket_region
            (optional, str) Region where the bucket should be created e.g. us-west-1, eu-west-2. Default: eu-central-1 For more information see https://docs.aws.amazon.com/general/latest/gr/s3.html
        """
        sess = boto3.Session(region_name='eu-central-1')

        s3_client = sess.client('s3')

        bucket_name = 'wef-wildfire-project'
        s3_region = {
            'LocationConstraint': bucket_region
        }

        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_region)


if __name__ == '__main__':
    parser = ArgumentParser(description='Download grib2 files from AWS bucket "noaa-gfs-bdp-pds"')
    parser.add_argument('--name', help='(str)', type=str, required=True)
    parser.add_argument('--region', help='(str)', default='eu-central-1', type=str, required=False)
    args = parser.parse_args()
    bucket_name = args.name
    bucket_region = args.region

    test = AWSCreateS3Bucket()
    test.create_bucket(bucket_name=bucket_name)