from typing import Optional

from pydantic import BaseModel

class BookBase(BaseModel):
  title: str
  author: str
  year: int
  isbn: str

class BookCreate(BookBase):
  pass

class BookUpdate(BookBase):
  title: Optional[str] = None
  author: Optional[str] = None
  year: Optional[int] = None
  isbn: Optional[str] = None

class Book(BookBase):
  id: int
  class Config:
    orm_mode = True
