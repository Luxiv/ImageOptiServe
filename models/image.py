from pydantic import BaseModel


class Image(BaseModel):
    id: int
    path: str
    quality: int

    class Config:
        orm_mode = True
