import sys
sys.path.append('..')
import os
import warnings
warnings.filterwarnings("ignore")
from datetime import timedelta, date, datetime
from cloud.gcp.gcp_cloudstorage_upload_file import GCPFileUploader
from cloud.aws.aws_s3_download_file import AWSDownloader
from noaa_extract_features import NOAAFeatureExtractor


def download(s3_bucket_name, object_file_name, result_file_name):
    # Create a downloader object and download the data from AWS bucket
    downloader = AWSDownloader()
    try:
        flag = downloader.download(s3_bucket=s3_bucket_name, 
                            s3_object_key=object_file_name,
                            result_file_name=result_file_name)
        return flag
    except:
        print('No dataset for this date')
        return False

def extract(result_file_name):
    # Create a extractor object and extract specified features out of the .grib file
    print('Start extracting features..')
    extractor = NOAAFeatureExtractor()

    # list of features to extract from the file
    features = ['TMP_P0_L103_GLL0', 'RH_P0_L103_GLL0', 'UGRD_P0_L103_GLL0', 'VGRD_P0_L103_GLL0']
    for feature in features:
        extractor.extract_feature(file_name=result_file_name, 
                                  feature=feature)
                         
    print('Extraction Successfull')

def upload(result_file_name, object_file_name):
    # Create a uploader object and upload every download to a GCP bucket
    uploader = GCPFileUploader()

    print('Start Uploading to GCP..')
    # upload extracted features
    uploader.upload_blob(bucket_name='wef_noaa_weather_data_bucket',
                         source_file_name=f'{result_file_name}_features.csv',
                         destination_blob_name=f'{object_file_name}_features.csv')


def main():
    curr_date = '20211210'  # start date
    end_date = str(datetime.today()).replace('-', '').split(' ')[0]  # today

    period = 'f024'  # forcast window, f024 = 24h forecast data, f072 = 72h forecast data
    
    while curr_date != end_date:
        print('\nDate:',curr_date)
        curr_date = datetime.strptime(curr_date, '%Y%m%d').strftime('%Y-%m-%d')
        curr_date = date.fromisoformat(curr_date) + timedelta(days=1)
        curr_date = str(curr_date).replace('-', '').split(' ')[0]

        s3_bucket_name = 'noaa-gfs-bdp-pds'
        object_file_name = f'gfs.{curr_date}/12/atmos/gfs.t12z.pgrb2.0p25.{period}'
        result_file_name = f's3_downloads/{curr_date}_gfs.t12z.pgrb2.0p25.{period}'

        try:
            dwl = download(s3_bucket_name, object_file_name, result_file_name)
            #print(dwl)
            if dwl:
                extract(result_file_name)
                upload(result_file_name, object_file_name)
        except:
            continue
    
        # Delete files locally after uploaded to Cloud bucket
        os.system('rm -rf s3_downloads/*')
    

if __name__ == '__main__':
    main()