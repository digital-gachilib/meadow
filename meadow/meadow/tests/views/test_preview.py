from django.urls import reverse

from meadow.models import Book
from meadow.tests.base import AuthorizedTestCase
from meadow.tests.factories import BookFactory


class PreviewViewTestCase(AuthorizedTestCase):
    def test_book_preview_book_exists(self):
        some_book = BookFactory()
        response = self.client.get(reverse("preview"), {"id": some_book.id})

        result = response.json()
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
            self.client.get(reverse("preview"), {"id": invalid_id})

    def test_book_preview_no_id(self):
        with self.assertRaises(ValueError, msg="No id provided!"):
            self.client.get(reverse("preview"), {})
