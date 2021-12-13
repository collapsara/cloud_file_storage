import boto3


class minio_manager:

    @classmethod
    def upload_file(cls):
        s3 = boto3.resource('s3')
        data = open('test.jpg', 'rb')
        s3.Bucket('files').put_object(Key='test.jpg', Body=data)