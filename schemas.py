from pydantic import BaseModel
from datetime import date
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    publishedDate: Optional[date] = None
    numberOfPages: Optional[int] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publishedDate: Optional[date] = None
    numberOfPages: Optional[int] = None

class BookOut(BookBase):
    id: int

    class Config:
        from_attributes = True