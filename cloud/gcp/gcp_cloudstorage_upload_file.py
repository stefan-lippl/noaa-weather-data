import sys
sys.path.append('..')
from google.cloud import storage
import os

class GCPFileUploader():
    """Uploads a file to the bucket."""
    def upload_blob(self, bucket_name:str, source_file_name:str, destination_blob_name:str):
        """ 
        source_file_name 
            (required, str) Filename / path which should be uploaded to bucket'
        destination_blob_name 
            (required, str) Filename of final file in bucket
        """
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/stefanlippl/dev/wef_final/spatial-risk-mapping/cloud/gcp/key/wildfire-forecasting-70bb79e32916.json'
        storage_client = storage.Client()

        bucket = storage_client.bucket(bucket_name)
        bucket = storage_client.get_bucket(bucket_name, timeout=300.0)
        blob = bucket.blob(destination_blob_name)
        blob._chunk_size = 8388608  # 1024 * 1024 B * 16 = 8 MB
     
        blob.upload_from_filename(source_file_name)

        print(
            "File {} successfully uploaded to GCP.".format(
                source_file_name
            )
        )