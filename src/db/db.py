from config_db import settings
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import inspect

engine = create_async_engine(
    url=settings.get_db_ulr
)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_async_session():
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    pass

async def reset_tables():
    async with engine.begin() as eng:
        await eng.run_sync(Base.metadata.drop_all)    
        await eng.run_sync(Base.metadata.create_all)    
