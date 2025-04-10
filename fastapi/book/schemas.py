from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: Optional[str] = None
    owner: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    
    class Config:
        from_attributes = True