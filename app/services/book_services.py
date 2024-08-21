# app/services/book_service.py
from typing import List, Optional
from app.models.book import Book
from app.repositories.book_repository import BookRepository

class BookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def create_book(self, book: Book) -> str:
        return self.book_repository.create(book)

    def get_books(self) -> List[Book]:
        return self.book_repository.get_all()

    def get_book(self, book_id: str) -> Optional[Book]:
        return self.book_repository.get_by_id(book_id)

    def update_book(self, book_id: str, book: Book) -> bool:
        return self.book_repository.update(book_id, book)

    def delete_book(self, book_id: str) -> bool:
        return self.book_repository.delete(book_id)
