import factory

from meadow.models import Book, BookAuthor


class BookAuthorFactory(factory.DjangoModelFactory):
    class Meta:
        model = BookAuthor


class BookFactory(factory.DjangoModelFactory):
    class Meta:
        model = Book

    author = factory.SubFactory(BookAuthorFactory)
