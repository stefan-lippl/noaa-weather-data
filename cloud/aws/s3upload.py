import boto3

s3 = boto3.client('s3')

s3.upload_file('/Users/stefanlippl/dev/wef_final/aws_weather/ffff4158943bf4d76fc0912894d013852159b711.nc', 'wef-wildfire-project', 'test_upload')
print('Upload successful')