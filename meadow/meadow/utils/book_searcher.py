from operator import attrgetter
from typing import List

from meadow.models import Book


def search_by_title(title: str) -> List[Book]:
    if not title:
        return list(filter(attrgetter("is_approved"), Book.objects.all()))

    title = title.lower()

    books = []
    for book in Book.objects.all():
        if book.title.lower().count(title) > 0 and book.is_approved:
            books.append(book)
    return books


def book_preview(book_id: int) -> dict:
    book = Book.objects.get(id=book_id)
    if not book.is_approved:
        raise ValueError("Book is not approved!")
    return {
        "title": book.title,
        "author": {"first_name": book.author.first_name, "last_name": book.author.last_name},
        "description": book.description,
        "isbn_10": book.isbn_10,
        "isbn_13": book.isbn_13,
        "download_link": book.download_link,
    }
