import os
import sys
import logging

from fastapi import FastAPI
import uvicorn

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from src.api.main_router import router

app = FastAPI()
app.include_router(router)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)