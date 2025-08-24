from typing import List
from pydantic import BaseModel

from src.schemas.tasks import TasksSchema

class UserSchema(BaseModel):
    user_id: int
    username: str
    email: str
    password: str
    tasks: List[TasksSchema]

    class Config():
        from_attributes = True

class UserAddSchema(BaseModel):
    username: str
    email: str
    password: str