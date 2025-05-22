from domain.file import FileEntity
from infrastructure.minio import MinioClient


class FileService:
    def __init__(self):
        self.minio = MinioClient()

    def upload(self, file_entity: FileEntity, file_obj):
        return self.minio.upload_file(file_obj, file_entity.filename, file_entity.content_type)
