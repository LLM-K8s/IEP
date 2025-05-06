from fastapi import APIRouter, HTTPException, Depends, Request
from typing import List
from domain.user import User
from application.user_service import UserService
from infrastructure.mongodb import get_engine
from application.auth_service import get_current_user

router = APIRouter()

def get_user_service(request: Request) -> UserService:
    return UserService(get_engine(request.app))

@router.post("/users", response_model=User)
async def create_user(
    user: User,
    service: UserService = Depends(get_user_service),
    current_user: dict = Depends(get_current_user)
):
    return await service.create_user(user)

@router.get("/users", response_model=List[User])
async def list_users(
    service: UserService = Depends(get_user_service),
    current_user: dict = Depends(get_current_user)
):
    print(current_user)
    return await service.list_users()

@router.get("/users/{user_sub}", response_model=User)
async def get_user(
    user_sub: str,
    service: UserService = Depends(get_user_service),
    current_user: dict = Depends(get_current_user)
):
    user = await service.get_user(user_sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/current_user", response_model=User)
async def get_current_user(
    service: UserService = Depends(get_user_service),
    current_user: dict = Depends(get_current_user)
):
    user = await service.get_user(current_user["sub"])
    if not user:
        raise HTTPException(status_code=404, detail="Current user not found")
    return user

@router.delete("/users/{user_sub}")
async def delete_user(
    user_sub: str,
    service: UserService = Depends(get_user_service),
    current_user: dict = Depends(get_current_user)
):
    success = await service.delete_user(user_sub)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}