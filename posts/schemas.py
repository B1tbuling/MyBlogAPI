from pydantic import BaseModel


class PostID(BaseModel):
    id: int = None


class PostBaseData(BaseModel):
    title: str = None
    text: str = None

    class Config:
        orm_mode = True


class PostData(PostID, PostBaseData): ...