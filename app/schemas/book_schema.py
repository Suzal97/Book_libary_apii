from pydantic import BaseModel

class BookSchema(BaseModel):
    title: str
    author: str
    published_year: int
    isbn: str
    pages: int

    class Config:
        orm_mode = True
