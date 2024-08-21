from pydantic import BaseModel, Field
from typing import Optional

class Book(BaseModel):
    title: str
    author: str
    published_year: int
    isbn: str
    pages: int
    id: Optional[str] = Field(default=None, alias="_id")
