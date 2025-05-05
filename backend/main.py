from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from interface.user_router import router as user_router
from interface.auth_router import router as auth_router
from interface.course_router import router as course_router
from infrastructure.mongodb import init_mongodb, close_mongodb
from contextlib import asynccontextmanager
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_mongodb(app)
    yield
    await close_mongodb(app)

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 或使用 ["*"] 開放所有來源（開發用）
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 路由綁定
app.include_router(user_router, prefix="/api")
app.include_router(auth_router, prefix="/api")
app.include_router(course_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)