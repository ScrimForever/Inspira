from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .endpoint import screen_router, keyboard_router
from starlette.responses import Response
from starlette.requests import Request
from inspira.backend.core.utils import get_db
from inspira.backend.core.database import SessionLocal


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.middleware('http')
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(screen_router, prefix='/screen', tags=['ScreenShot'])
app.include_router(keyboard_router, prefix='/keyboard', tags=['Keyboard'])
