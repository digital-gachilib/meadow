import factory

from meadow.models import Book, BookAuthor


class BookAuthorFactory(factory.DjangoModelFactory):
    class Meta:
        model = BookAuthor


class BookFactory(factory.DjangoModelFactory):
    class Meta:
        model = Book

    author = factory.SubFactory(BookAuthorFactory)
    title = factory.Sequence(lambda n: f"Book title #{n}")
