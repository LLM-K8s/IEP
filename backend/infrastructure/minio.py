from minio import Minio


class MinioClient:
    def __init__(self):
        self.client = Minio(
            '172.16.3.49:9000',
            secure=False,
        )
        self.bucket = 'coursefile'
        if not self.client.bucket_exists(self.bucket):
            self.client.make_bucket(self.bucket)

    def upload_file(self, file_obj, filename, content_type):
        self.client.put_object(
            self.bucket,
            filename,
            file_obj,
            length=-1,
            part_size=10 * 1024 * 1024,
            content_type=content_type,
        )
        return f'{self.bucket}/{filename}'
