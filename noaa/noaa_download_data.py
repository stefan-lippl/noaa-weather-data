import sys
sys.path.append('..')
from argparse import ArgumentParser
from cloud.gcp.gcp_cloudstorage_upload_file import GCPFileUploader
from cloud.aws.aws_s3_download_file import AWSDownloader


if __name__ == '__main__':
    # Get Arguments for download
    parser = ArgumentParser(description='Download grib2 files from AWS bucket "noaa-gfs-bdp-pds"')
    parser.add_argument('--date', help='(str) Date which data should be downloaded (YYYYMMDD)', type=str, required=True)
    parser.add_argument('--period', help='(str) Forecast period: e.g. f024, f048, f072, ... (default: f024)', default='f024', type=str, required=False)
    parser.add_argument('-u', help='(str) Should the file get uploaded to the GCP bucket? If -u set: yes else no', required=False, action='store_true')
    args = parser.parse_args()
    date = args.date
    period = args.period
    upload = args.u

    # Download AWS data
    s3_bucket_name = 'noaa-gfs-bdp-pds'
    object_file_name = f'gfs.{date}/12/atmos/gfs.t12z.pgrb2.0p25.{period}'
    result_file_name = f's3_downloads/{date}_gfs.t12z.pgrb2.0p25.{period}'

    downloader = AWSDownloader()
    downloader.download(s3_bucket=s3_bucket_name, 
                        s3_object_key=object_file_name,
                        result_file_name=result_file_name)

    # Upload to GCP bucket
    if upload:
        print('Uploading to GCP bucket..')
        uploader = GCPFileUploader()
        uploader.upload_blob(bucket_name='wef_noaa_weather_data_bucket',
                             source_file_name=result_file_name,
                             destination_blob_name=object_file_name)