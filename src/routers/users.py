from typing import List

from fastapi import APIRouter, HTTPException


from schemas.users import UserAddSchema, UserSchema
from services.users import UserServices
from repositories.users import UserRepositories
from utils.exceptions import EntityNotFoundError

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=List[UserSchema])
async def get_all_users() -> List[UserSchema]:
    res = await UserServices(UserRepositories).get_all_users()
    return res


@router.post("", response_model=int)
async def add_user(data: UserAddSchema) -> int:
    user_id = await UserServices(UserRepositories).add_user(data)
    return user_id


@router.put("", response_model=UserSchema)
async def update_user(user_id: int, data: UserAddSchema) -> UserSchema:
    try:
        model = await UserServices(UserRepositories).update_user(user_id, data)
        return model
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.delete("", response_model=dict)
async def delete_user(user_id: int) -> dict:
    try:
        res = await UserServices(UserRepositories).delete_user(user_id)
        return res
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
