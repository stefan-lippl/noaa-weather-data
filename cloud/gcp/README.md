# GCP

## Create Bucket
With the script `create_bucket.py` you can create buckets via your CLI.

<br>

### Arguments
| arg | description | default |
| --- | ----------- | ------- |
| -h | Help | - |
| --name | Give the bucket a bucket name | - |
| --storage_class | Define your storage class e.g. STANDARD, where you don't have a minimum storage duration. You can find all storage classes on the official [GCP Storage classes](https://cloud.google.com/storage/docs/storage-classes) site | STANDARD |
| --region | Define your storages' region e.g. US-EAST1, where you don't have a minimum storage duration. You can find all storage classes on the official [GCP regions](https://cloud.google.com/storage/docs/locations) site | EUROPE-WEST3 |

<br>

### Example
> Create a bucket in the region ***US-CENTRAL1*** (Iowa) with the name ***my_gcp_bucket_deloitte*** and the storage class ***COLDLINE*** (minimum storage duration: 90 days)

```
python create_bucket.py --name my_gcp_bucket_deloitte --storage_class COLDLINE --region US-CENTRAL1
```

<br>

***

<br>

## Upload files
