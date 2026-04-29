import logging
import asyncio

import uvicorn
from fastapi import FastAPI

from routers import router
from db.db import create_tables_if_not_exists


app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    asyncio.run(create_tables_if_not_exists())

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
