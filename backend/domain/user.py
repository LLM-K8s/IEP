from odmantic import Model, Field
from typing import Optional
from bson import ObjectId

class User(Model):
    user_id: Optional[ObjectId] = Field(default_factory=ObjectId, primary_field=True)
    user_sub: str
    user_email: str
    user_name: str
    user_is_teacher: bool

