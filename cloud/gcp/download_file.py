from google.cloud import storage
import os 
from argparse import ArgumentParser
import sys

def download_folder_from_gcp_bucket(bucket_name: str, date: str, band: str, directory: str):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/stefanlippl/dev/wef_final/spatial-risk-mapping/cloud/gcp/key/wildfire-forecasting-70bb79e32916.json'

    prefix = f'sentinel_data/{date}/{band}'
    
    # Make sure the path is correct and add trailing / if not exists
    if directory[-1] != '/':
        directory = directory + '/'

    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f'Created directory: {directory}')

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_or_name=bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)  # Get list of files
    
    sum_blobs = int(sum(1 for _ in bucket.list_blobs()) / 3)  # because of 3 bands - so 3 subfolder

    for i, blob in enumerate(blobs):
        
        #sys.stdout.flush()
        print(f'\rDownloading image {i+1}/{sum_blobs}', end='', flush=True)
        

        filename = blob.name.replace('/', '_') 
        blob.download_to_filename(directory + filename)  # Download
    print('\n')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--bname', default='sentinel2_data_bucket', help='Which date would you like to download. FORMAT: YYYYMMDD')
    parser.add_argument('--date', help='Which date would you like to download. FORMAT: YYYYMMDD')
    parser.add_argument('--band', help='Which band would you like to download. CHOICE: b8a, b11, b12 (CASE SENSITIVE)')
    parser.add_argument('--dest', default='tmp_dflt/', help='Directory where to store the downloaded files')

    args = parser.parse_args()
    bname = args.bname
    date = args.date
    band = args.band
    sdir = args.dest

    if band == 'b8a' or band == 'b11' or band == 'b12':
        download_folder_from_gcp_bucket(bucket_name=bname, date=date, band=band, directory=sdir)
    else:
        print('\nBAND NOT FOUND.. Please insert band name b8a, b11 or b12 (CASE SENSITIVE)\n')
        sys.exit()