from minio import Minio

from infrastructure.config import settings


class MinioClient:
    def __init__(self):
        self.client = Minio(
            settings.MINIO_ENDPOINT,
            secure=False,
        )
        self.bucket = settings.MINIO_BUCKET
        if not self.client.bucket_exists(self.bucket):
            self.client.make_bucket(self.bucket)

    def upload_file(self, file_obj, filename, content_type) -> str:
        self.client.put_object(
            self.bucket,
            filename,
            file_obj,
            length=-1,
            part_size=10 * 1024 * 1024,
            content_type=content_type,
        )
        return f'{self.bucket}/{filename}'
