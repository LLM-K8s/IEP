from typing import Optional

from bson import ObjectId
from odmantic import Field, Model


class User(Model):
    user_id: Optional[ObjectId] = Field(default_factory=ObjectId, primary_field=True)
    user_sub: str
    user_email: str
    user_name: str
    user_is_teacher: bool

