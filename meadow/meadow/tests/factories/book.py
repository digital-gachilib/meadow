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
    isbn_10 = factory.Sequence(lambda n: f"isbn_10 #{n}")
    isbn_13 = factory.Sequence(lambda n: f"isbn_13 #{n}")
