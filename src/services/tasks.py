from typing import Dict, List

from utils.repositories import AbstractRepositories
from schemas.tasks import TasksSchema, TasksAddSchema


class TasksServices:
    def __init__(self, tasks_repo: type(AbstractRepositories)):  # type: ignore
        self.tasks_repo: type(AbstractRepositories) = tasks_repo()  # type: ignore

    async def get_all_tasks(self) -> List[TasksSchema]:
        res = await self.tasks_repo.find_all()
        return res
    
    async def get_current_task(self, task_id) -> TasksSchema:
        res = await self.tasks_repo.find_currency(task_id)
        return res

    async def add_task(self, data: TasksAddSchema) -> TasksSchema:
        data_dict = data.model_dump()
        res = await self.tasks_repo.add_one(data_dict)
        return res

    async def update_task(self, task_id: int, data: TasksAddSchema) -> TasksSchema:
        data_dict = data.model_dump()
        res = await self.tasks_repo.update_one(task_id, data_dict)
        return res

    async def delete_task(self, task_id: int) -> Dict:
        await self.tasks_repo.delete_one(task_id)
        return {"message": "Task deleted"}
