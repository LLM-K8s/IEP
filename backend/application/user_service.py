from typing import List
from odmantic import AIOEngine
from domain.user import User
from bson import ObjectId

class UserService:
    def __init__(self, engine: AIOEngine):
        self.engine = engine

    async def create_user(self, user: User) -> User:
        await self.engine.save(user)
        return user

    async def list_users(self) -> List[User]:
        return await self.engine.find(User, {})

    async def get_user(self, user_id: str) -> User | None:
        try:
            object_id = ObjectId(user_id)
            return await self.engine.find_one(User, User.id == object_id)
        except:
            return None

    async def delete_user(self, user_id: str) -> bool:
        try:
            object_id = ObjectId(user_id)
            user = await self.engine.find_one(User, User.id == object_id)
            if user:
                await self.engine.delete(user)
                return True
            return False
        except:
            return False