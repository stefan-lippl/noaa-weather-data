"""
https://cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-code_samples
"""

from google.cloud import storage
from argparse import ArgumentParser
import os


def create_bucket_class_location(bucket_name: str, storage_class: str, region: str):
    """
    Create a new bucket in the US region with the STANDARD storage
    class
    """
    #bucket_name = "wef_bucket_test_1"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/stefanlippl/dev/wef_final/spatial-risk-mapping/cloud/gcp/key/wildfire-forecasting-70bb79e32916.json'
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = storage_class
    new_bucket = storage_client.create_bucket(bucket, location=region)

    print(
        "\nCreated bucket {} in {} with storage class {}\n".format(
            new_bucket.name, new_bucket.location, new_bucket.storage_class
        )
    )
    return new_bucket

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--name', help='Unique name of the bucket which should be created')
    parser.add_argument('--storage_class', default='STANDARD', help='https://cloud.google.com/storage/docs/storage-classes')
    parser.add_argument('--region', default='EUROPE-WEST3', help='https://cloud.google.com/storage/docs/locations')

    args = parser.parse_args()
    bname = args.name
    sclass = args.storage_class
    regio = args.region

    create_bucket_class_location(bucket_name=bname, storage_class=sclass, region=regio)