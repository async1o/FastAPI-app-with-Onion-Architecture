from pydantic import BaseModel, ConfigDict


class TasksSchema(BaseModel):
    task_id: int
    text: str
    owner_id: int

    model_config = ConfigDict(from_attributes=True)


class TasksAddSchema(BaseModel):
    text: str
    owner_id: int


class TaskViewSchema(BaseModel):
    text: str
