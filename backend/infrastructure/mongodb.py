from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from fastapi import FastAPI

async def init_mongodb(app: FastAPI):
    client = AsyncIOMotorClient("mongodb://172.16.3.49:27017")
    await client.admin.command("ping")  # 測試連線
    engine = AIOEngine(database="yangtest", client=client)

    app.state.mongodb_client = client
    app.state.mongodb_engine = engine
    print("✅ MongoDB 已連線")

async def close_mongodb(app: FastAPI):
    app.state.mongodb_client.close()
    print("🧹 MongoDB 連線關閉")

def get_engine(app: FastAPI) -> AIOEngine:
    return app.state.mongodb_engine