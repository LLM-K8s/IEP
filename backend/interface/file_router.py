from fastapi import APIRouter, Depends, File, UploadFile

from application.auth_service import get_current_user
from application.file_service import FileService
from domain.file import FileEntity

router = APIRouter()
service = FileService()


@router.post('/upload')
async def upload_file(file: UploadFile = File(...), current_user: dict = Depends(get_current_user)):
    entity = FileEntity(filename=file.filename, content_type=file.content_type)
    url = service.upload(entity, file.file)
    return {'filename': file.filename, 'url': f'{"http://172.16.3.49:9000/" + url}'}
