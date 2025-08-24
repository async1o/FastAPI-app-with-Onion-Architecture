from pydantic import BaseModel

class TasksSchema(BaseModel):
    user_id: int
    text: str
    owner_id: int

    class Config():
        from_attributes = True

class TasksAddSchema(BaseModel):
    text: str
    owner_id: int

class TaskViewSchema(BaseModel):
    text: str