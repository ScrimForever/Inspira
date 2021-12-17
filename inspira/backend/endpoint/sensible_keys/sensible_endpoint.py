from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from inspira.backend.core.utils import get_db
from inspira.backend.models import UserPwd
from inspira.backend.schemas import UserPwdSchema
from fastapi.responses import JSONResponse
keyboard_router = APIRouter()


@keyboard_router.post('/{host_id}')
async def screen_upload(sensible: UserPwdSchema, host_id: str, db: Session = Depends(get_db)):
    try:
        sense = UserPwd(**sensible.dict())
        sense.host_id = host_id
        db.add(sense)
        db.commit()
        db.refresh(sense)
        return sense
    except Exception as e:
        print(e)
        return JSONResponse(status_code=403, content={'Message': 'Problem to register object'})



