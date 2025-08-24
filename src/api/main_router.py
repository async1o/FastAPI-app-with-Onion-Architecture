from fastapi import APIRouter
from src.api.routers.users import router as users_router
from src.api.routers.tasks import router as tasks_router
from src.db.db import reset_tables

router = APIRouter()

router.include_router(users_router)
router.include_router(tasks_router)

@router.get('/db')
async def reset_all_tables():
    await reset_tables()
    return {'message': 'Tables reset'}