from fastapi import APIRouter
from fastapi import File, UploadFile
import shutil

screen_router = APIRouter()

@screen_router.post('/{screen_name}/')
async def screen_upload(screen_name: str, file: UploadFile = File(...)):
    try:
        path = f'backend/screenshot/{screen_name}.{file.filename.split(".")[-1]}'
        with open(path, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        print(e)


