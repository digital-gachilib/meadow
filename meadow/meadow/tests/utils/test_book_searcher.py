from django.test import TestCase

from meadow.models import Book
from meadow.tests.factories.book import BookFactory
from meadow.utils.book_searcher import book_preview


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
