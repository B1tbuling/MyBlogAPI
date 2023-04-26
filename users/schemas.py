import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    first_name: str
    last_name: str


class UserCreate(schemas.BaseUserCreate):
    username: str
    first_name: str
    last_name: str


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str
    last_name: str