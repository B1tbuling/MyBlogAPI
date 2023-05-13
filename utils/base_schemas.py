from pydantic import BaseModel


class IDSchema(BaseModel):
    id: int


class OptionalIDSchema(BaseModel):
    id: int | None = None
