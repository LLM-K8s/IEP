from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

client = None
engine = None

async def init_mongodb():
    global client, engine
    try:
        client = AsyncIOMotorClient("mongodb://172.16.3.49:27017")
        await client.admin.command('ping') # 測試連接
        # 確保 engine 被正確設置
        engine = AIOEngine(database="testDB", client=client)
        # 再次確認 engine 不為 None
        if engine is None:
            raise Exception("Engine initialization failed")
        print("MongoDB 連接成功")
    except Exception as e:
        print(f"MongoDB 連接失敗: {str(e)}")
        raise

def get_engine():
    if engine is None:
        raise Exception("MongoDB engine not initialized")
    return engine