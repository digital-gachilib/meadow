from django.test import TestCase

from meadow.models import Book
from meadow.tests.factories.book import BookFactory
from meadow.utils.book_searcher import book_preview, search_by_title


class BookPreviewTestCase(TestCase):
    def test_book_preview_book_exists(self):
        some_book = BookFactory()

        result = book_preview(some_book.id)
        self.assertEqual(result["title"], some_book.title)
        self.assertEqual(result["description"], some_book.description)
        self.assertEqual(result["author"]["first_name"], some_book.author.first_name)
        self.assertEqual(result["author"]["last_name"], some_book.author.last_name)

    def test_book_preview_book_doesnot_exist(self):
        some_book = BookFactory()

        # there is definitely no book with invalid_id in the DB
        invalid_id = some_book.id + 1

        # the function should raise an exception if the id is invalid
        with self.assertRaises(Book.DoesNotExist):
            book_preview(invalid_id)


class BookSearchTestCase(TestCase):
    def test_search_empty_title(self):
        books = [BookFactory() for _ in range(5)]
        title = ""
        result = search_by_title(title)
        self.assertEqual(len(books), len(result))

    def test_search_some_unique_title(self):
        books = [BookFactory() for _ in range(5)]
        book_to_search = books[1]
        title = book_to_search.title
        result = search_by_title(title)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, title)

    def test_search_title_doesnot_exist(self):
        [BookFactory() for _ in range(5)]
        title = "Some cook title which doesn't exist in DB"
        result = search_by_title(title)
        self.assertEqual(result, [])
