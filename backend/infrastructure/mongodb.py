from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from infrastructure.config import settings


async def init_mongodb(app: FastAPI):
    try:
        client = AsyncIOMotorClient(settings.MONGODB_URL)
        await client.admin.command('ping')  # 測試連線
        engine = AIOEngine(database=settings.MONGODB_DB_NAME, client=client)

        # 確保 engine 被正確設置
        if engine is None:
            raise Exception('Engine initialization failed')

        app.state.mongodb_client = client
        app.state.mongodb_engine = engine
        print('✅ MongoDB 已連線')
    except Exception as e:
        print(f'MongoDB 連接失敗: {str(e)}')
        raise


async def close_mongodb(app: FastAPI):
    app.state.mongodb_client.close()
    print('🧹 MongoDB 連線關閉')


def get_engine(app: FastAPI) -> AIOEngine:
    return app.state.mongodb_engine
