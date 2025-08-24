
from fastapi import APIRouter


from src.schemas.tasks import TasksAddSchema
from services.tasks import TasksServices
from repositories.tasks import TasksRepositories

router = APIRouter(
    prefix='/tasks',
    tags=['tasks']
)

@router.get('')
async def get_all_tasks():
    res = await TasksServices(TasksRepositories).get_all_tasks()
    return res

@router.post('')
async def add_task(data: TasksAddSchema):
    try:
        task_id = await TasksServices(TasksRepositories).add_task(data)
        return task_id
    except:
        return {'message': 'Что-то пошло не так'}

@router.put('')
async def update_task(task_id: int, data: TasksAddSchema):
    model = await TasksServices(TasksRepositories).update_task(task_id, data)
    return model

@router.delete('')
async def delete_task(task_id: int):
    res = await TasksServices(TasksRepositories).delete_task(task_id)
    return res