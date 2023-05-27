from fastapi_users import schemas
from pydantic import BaseModel


class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    username: str


class UserUpdate(schemas.BaseUserUpdate):
    pass


class UserProfileInfo(BaseModel):
    first_name: str
    last_name: str
    username: str

    class Config:
        orm_mode = True
