from typing import Dict

from src.utils.repositories import AbstractRepositories
from src.schemas.tasks import TasksSchema, TasksAddSchema



class TasksServices():
    def __init__(self, tasks_repo: type(AbstractRepositories)): #type: ignore
        self.tasks_repo: type(AbstractRepositories) = tasks_repo()  #type: ignore
    
    async def get_all_tasks(self) -> TasksSchema:
        res = await self.tasks_repo.find_all()
        return res
    
    async def add_task(self, data: TasksAddSchema) -> TasksSchema:
        data_dict = data.model_dump()
        res = await self.tasks_repo.add_one(data_dict)
        return res
    
    async def update_task(self, task_id: int, data: TasksAddSchema) -> TasksSchema:
        data_dict = data.model_dump()
        res = await self.tasks_repo.update_one(task_id, data_dict)
        return res
    
    async def delete_task(self, user_id: int) -> Dict:
        await self.tasks_repo.delete_one(user_id)
        return {'message': 'User deleted'}
