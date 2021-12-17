from fastapi import APIRouter

keyboard_router = APIRouter()

@keyboard_router.post('/{sensible_str}/{host_id}')
async def screen_upload(sensible_str: str, host_id: str):
    try:
        print(sensible_str, host_id)
    except Exception as e:
        print(e)


