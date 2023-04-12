from pydantic import BaseModel


class PostData(BaseModel):
    id: int = None
    title: str = None
    text: str = None

    class Config:
        orm_mode = True


class PostBaseData(BaseModel):
    title: str = None
    text: str = None

    class Config:
        orm_mode = True

