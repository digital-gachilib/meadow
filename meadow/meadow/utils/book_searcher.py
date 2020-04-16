from typing import List

from meadow.models import Book


def search_by_title(title: str) -> List[Book]:
    if not title:
        return list(Book.objects.all())
    title = title.lower()

    books = []
    for book in Book.objects.all():
        if book.title.lower().count(title) > 0:
            books.append(book)
    return books


def book_preview(book_id: int) -> {Book.title, BookAuthor.first_name, BookAuthor.last_name, Book.description}:
    book = Book.objects.get(id=book_id)
    return {book.title, book.author.first_name, book.author.last_name, book.description}