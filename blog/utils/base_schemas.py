from pydantic import BaseModel


class IDSchema(BaseModel):
    id: int

    class Config:
        orm_mode = True

class OptionalIDSchema(BaseModel):
    id: int | None = None
