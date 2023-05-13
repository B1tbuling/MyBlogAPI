from pydantic import BaseModel

from users.schemas import UserProfileInfo
from utils.base_schemas import IDSchema


class PostDataSchema(BaseModel):
    title: str = None
    text: str = None

    class Config:
        orm_mode = True


class PostSchema(IDSchema, PostDataSchema):
    user_id: int


class CommentDataSchema(BaseModel):
    text: str = None

    class Config:
        orm_mode = True


class CommentSchema(IDSchema, CommentDataSchema):
    user: UserProfileInfo




