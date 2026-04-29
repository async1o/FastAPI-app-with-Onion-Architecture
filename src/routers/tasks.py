from typing import List

from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError


from schemas.tasks import TasksAddSchema, TasksSchema
from services.tasks import TasksServices
from repositories.tasks import TasksRepositories
from utils.exceptions import EntityNotFoundError

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=List[TasksSchema])
async def get_all_tasks() -> List[TasksSchema]:
    res = await TasksServices(TasksRepositories).get_all_tasks()
    return res


@router.post("", response_model=int)
async def add_task(data: TasksAddSchema) -> int:
    try:
        task_id = await TasksServices(TasksRepositories).add_task(data)
        return task_id
    except IntegrityError as exc:
        raise HTTPException(status_code=400, detail="Invalid task payload") from exc


@router.put("", response_model=TasksSchema)
async def update_task(task_id: int, data: TasksAddSchema) -> TasksSchema:
    try:
        model = await TasksServices(TasksRepositories).update_task(task_id, data)
        return model
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.delete("", response_model=dict)
async def delete_task(task_id: int) -> dict:
    try:
        res = await TasksServices(TasksRepositories).delete_task(task_id)
        return res
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
