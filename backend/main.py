from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from infrastructure.config import settings
from infrastructure.mongodb import close_mongodb, init_mongodb
from interface.auth_router import router as auth_router
from interface.course_router import router as course_router
from interface.file_router import router as file_router
from interface.user_router import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_mongodb(app)
    yield
    await close_mongodb(app)


app = FastAPI(lifespan=lifespan)

origins = [
    *settings.CORS_ORIGINS,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# 路由綁定
app.include_router(user_router, prefix='/api')
app.include_router(auth_router, prefix='/api')
app.include_router(course_router, prefix='/api')
app.include_router(file_router, prefix='/api')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
