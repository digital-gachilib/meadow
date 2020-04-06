from meadow.models import Book


def search_by_title(title: str):
    books = []
    for book in Book.objects.all():
        if book.title.lower().count(title) > 0:
            books.append(book)
    return books
