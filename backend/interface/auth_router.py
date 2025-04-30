from fastapi import APIRouter, Depends
from application.auth_service import get_current_user

router = APIRouter()

@router.get("/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user