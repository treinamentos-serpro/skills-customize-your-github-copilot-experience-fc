from typing import Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class Book(BaseModel):
    title: str
    author: str
    published_year: int


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    published_year: Optional[int] = None


books = [
    {
        "id": 1,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt and David Thomas",
        "published_year": 1999,
    },
    {
        "id": 2,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "published_year": 2008,
    },
]


@app.get("/books")
def list_books():
    """Return every book in the catalog."""
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Return one book by ID."""
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    """Add a new book to the catalog."""
    pass


@app.patch("/books/{book_id}")
def update_book(book_id: int, book_update: BookUpdate):
    """Update the provided fields of an existing book."""
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """Remove a book from the catalog."""
    pass
