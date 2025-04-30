from odmantic import Model, Field
from typing import Optional
from bson import ObjectId

class User(Model):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, primary_field=True)
    sub: str
    user_email: str
    name: str
    is_teacher: bool

