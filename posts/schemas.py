from pydantic import BaseModel

from users.schemas import UserProfileInfo


class PostID(BaseModel):
    id: int = None


class PostBaseData(BaseModel):
    title: str = None
    text: str = None

    class Config:
        orm_mode = True


class PostData(PostID, PostBaseData): ...


class CommentsSchemas(BaseModel):
    id: int = None
    text: str = None
    user: UserProfileInfo

    class Config:
        orm_mode = True


class CommentCreate(BaseModel):
    post_id: int = None
    text: str = None




