from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .endpoint import screen_router, keyboard_router

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(screen_router, prefix='/screen', tags=['ScreenShot'])
app.include_router(keyboard_router, prefix='/keyboard', tags=['Keyboard'])
