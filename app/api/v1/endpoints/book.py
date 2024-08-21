# app/api/v1/endpoints/book.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.book import BookCreate, BookUpdate, BookOut
from app.services.book_service import BookService
from app.repositories.book_repository import BookRepository
from app.database import get_book_collection

router = APIRouter()

def get_book_service():
    collection = get_book_collection()
    repository = BookRepository(collection)
    return BookService(repository)

@router.post("/", response_model=str)
def create_book(book: BookCreate, service: BookService = Depends(get_book_service)):
    return service.create_book(book)

@router.get("/", response_model=List[BookOut])
def get_books(service: BookService = Depends(get_book_service)):
    return service.get_books()

@router.get("/{book_id}", response_model=BookOut)
def get_book(book_id: str, service: BookService = Depends(get_book_service)):
    book = service.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=bool)
def update_book(book_id: str, book: BookUpdate, service: BookService = Depends(get_book_service)):
    return service.update_book(book_id, book)

@router.delete("/{book_id}", response_model=bool)
def delete_book(book_id: str, service: BookService = Depends(get_book_service)):
    return service.delete_book(book_id)
