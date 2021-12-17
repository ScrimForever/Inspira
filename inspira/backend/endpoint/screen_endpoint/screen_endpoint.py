import os.path
from fastapi import APIRouter
from fastapi import File, UploadFile
import shutil
from pathlib import Path

screen_router = APIRouter()

@screen_router.post('/{screen_name}/{host_id}')
async def screen_upload(screen_name: str, host_id: str, file: UploadFile = File(...)):
    try:
        if not os.path.exists(f'backend/screenshot/{host_id}'):
            os.makedirs(f'backend/screenshot/{host_id}')
        path = f'backend/screenshot/{host_id}/{screen_name}.{file.filename.split(".")[-1]}'
        with open(path, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        print(e)


