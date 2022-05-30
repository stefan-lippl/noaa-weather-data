import sys
sys.path.append('..')
import boto3
import botocore


class AWSDownloader():
    """Download all kinds of files from a given AWS S3 bucket"""
    def download(self, s3_bucket:str, s3_object_key:str, result_file_name:str):
        """
        ARGS:
        s3_bucket
            (required, str) The bucket name in which the file(s) is located

        s3_object_key
            (required, str) The specific name/path of the file to download

        result_file_name
            (required, str) Name of the downloaded file locally

        RETURN:
        True if download successfull, else False
        """
        try:
            # Connect to the Bucket/S3 Client
            s3_client = boto3.client('s3')
            meta_data = s3_client.head_object(Bucket=s3_bucket, Key=s3_object_key)
            total_length = int(meta_data.get('ContentLength', 0))
            downloaded = 0

            # Create progress bar for CLI output
            def progress(chunk):
                nonlocal downloaded
                downloaded += chunk
                done = int(50 * downloaded / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
                sys.stdout.flush()

            # Download the file
            print(f'Downloading {s3_object_key}')
            with open(result_file_name, 'wb') as f:
                s3_client.download_fileobj(s3_bucket, s3_object_key, f, Callback=progress)
            print('\nDownload Successfull')
            return True

        except botocore.exceptions.ClientError as e: 
            #print(e)
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
                return False
            else:
                print('Download Unsuccessfull')
                return False