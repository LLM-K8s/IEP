import uvicorn
from fastapi.routing import APIRouter

from application.app_factory import AppFactory
from infrastructure.config import settings
from interface.auth_router import router as auth_router
from interface.course_router import router as course_router
from interface.file_router import router as file_router
from interface.user_router import router as user_router

FRONTEND_DIST_DIR = settings.FRONTEND_DIST_DIR

# 收集所有路由
routers: list[APIRouter] = [
    user_router,
    auth_router,
    course_router,
    file_router,
]

# 創建應用程序
app_factory = AppFactory(FRONTEND_DIST_DIR)
app = app_factory.create_app(routers)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
