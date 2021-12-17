from pydantic import BaseModel


class UserPwdSchema(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
