import logging

from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import NullPool

from config_db import settings


logger = logging.getLogger(__name__)


engine = create_async_engine(
    url=settings.get_db_ulr,
    poolclass=NullPool if settings.MODE == "TEST" else None,
)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session():
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    pass


async def reset_tables():
    _import_all_models()
    async with engine.begin() as eng:
        await eng.run_sync(Base.metadata.drop_all)
        await eng.run_sync(Base.metadata.create_all)


def _import_all_models():
    from models.users import UsersModel  # noqa: F401
    from models.tasks import TasksModel  # noqa: F401


async def _table_exists(table_name: str) -> bool:
    """Проверить, существует ли конкретная таблица в БД."""
    async with engine.connect() as conn:

        def _check(sync_conn):
            insp = inspect(sync_conn)
            return table_name in insp.get_table_names()

        return await conn.run_sync(_check)


async def create_tables():
    _import_all_models()

    async with engine.begin() as eng:
        await eng.run_sync(Base.metadata.create_all)
    logger.info("Tables created")


async def create_tables_if_not_exists():
    """Создать таблицы, если они ещё не существуют."""
    _import_all_models()

    if not await _table_exists("users"):
        await create_tables()
        logger.info("Tables created on startup (auto)")
    else:
        logger.info("Tables already exist, skipping creation")
