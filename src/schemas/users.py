from typing import List
from pydantic import BaseModel, ConfigDict

from schemas.tasks import TasksSchema


class UserSchema(BaseModel):
    user_id: int
    username: str
    email: str
    tasks: List[TasksSchema]

    model_config = ConfigDict(from_attributes=True)


class UserAddSchema(BaseModel):
    username: str
    email: str
    password: str
