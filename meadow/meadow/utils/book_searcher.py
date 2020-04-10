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
