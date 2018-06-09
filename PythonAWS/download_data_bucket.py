import boto3
s3 = boto3.resource('s3')
s3.Bucket("projectx-bucket1-2018-06-08-1528435468").download_file("test.txt", "test_download.txt")
print("Downloaded")
