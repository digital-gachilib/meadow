from meadow.models import Book
from meadow.models import BookAuthor


def create_new_book(titl:str, link: str, descr: str, author_first: str, author_last: str):
    a = BookAuthor(first_name=author_first, last_name=author_last)
    a.save()
    Book(title=titl, download_link=link, description=descr, author=a).save()
