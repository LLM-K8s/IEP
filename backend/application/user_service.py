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

    async def get_user(self, user_sub: str) -> User | None:
        try:
            sub = user_sub
            return await self.engine.find_one(User, User.user_sub == sub)
        except:
            return None

    async def delete_user(self, user_sub: str) -> bool:
        try:
            sub = user_sub
            user = await self.engine.find_one(User, User.user_sub == sub)
            if user:
                await self.engine.delete(user)
                return True
            return False
        except:
            return False