from pydantic import BaseModel


class Book(BaseModel):
    title: str
    rating: int

    class Config:
        orm_mode = True
