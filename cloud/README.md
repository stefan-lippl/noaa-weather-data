# Cloud components

## AWS
### Import
#### Download Objects
```python
from cloud.aws.download_s3_file import AWSDownloader

downloader = AWSDownloader()
downloader.download(
    local_filename: str
    s3_bucket: str
    s3_object_key: str
)
```

<br>

***

<br>

## GCP
### Import
#### Upload Objects
```python
from cloud.gcp.upload_object import GCPFileUploader

uploader = GCPFileUploader()
downloader.download(
    bucket_name: str
    source_file_name: str
    destination_blob_name: str
)
```