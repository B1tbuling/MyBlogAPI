from pydantic import BaseModel

from users.schemas import UserProfileInfo
from utils.base_schemas import IDSchema


class PostDataSchema(BaseModel):
    title: str = None
    text: str = None


class PostSchema(IDSchema, PostDataSchema):
    user_id: int

    class Config:
        orm_mode = True


class CommentDataSchema(BaseModel):
    text: str = None


class CommentSchema(IDSchema, CommentDataSchema):
    user: UserProfileInfo

    class Config:
        orm_mode = True



