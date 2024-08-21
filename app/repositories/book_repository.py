# app/repositories/book_repository.py
from typing import List, Optional
from app.models.book import Book
from pymongo.collection import Collection

class BookRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    def create(self, book: Book) -> str:
        result = self.collection.insert_one(book.dict(by_alias=True))
        return str(result.inserted_id)

    def get_all(self) -> List[Book]:
        books = self.collection.find()
        return [Book(**book) for book in books]

    def get_by_id(self, book_id: str) -> Optional[Book]:
        book = self.collection.find_one({"_id": book_id})
        return Book(**book) if book else None

    def update(self, book_id: str, book: Book) -> bool:
        result = self.collection.replace_one({"_id": book_id}, book.dict(by_alias=True))
        return result.modified_count > 0

    def delete(self, book_id: str) -> bool:
        result = self.collection.delete_one({"_id": book_id})
        return result.deleted_count > 0
