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


def book_preview(book_id: int) -> dict:
    book = Book.objects.get(id=book_id)
    return {'title': book.title, 'author': {'name': book.author.first_name, 'surname': book.author.last_name},
            'description': book.description}
