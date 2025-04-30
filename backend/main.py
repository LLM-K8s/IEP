from fastapi import FastAPI
from interface.user_router import router as user_router
from interface.auth_router import router as auth_router
from infrastructure.mongodb import init_mongodb, close_mongodb
from contextlib import asynccontextmanager
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_mongodb(app)
    yield
    await close_mongodb(app)

app = FastAPI(lifespan=lifespan)

# 路由綁定
app.include_router(user_router, prefix="/api")
app.include_router(auth_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)