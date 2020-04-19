from django.urls import reverse

from meadow.tests.base import AuthorizedTestCase
from meadow.tests.factories import BookFactory


class SearchViewTestCase(AuthorizedTestCase):
    def test_search_empty_title(self):
        books = [BookFactory() for _ in range(5)]
        response = self.client.get(reverse("search"))

        response_json = response.json()
        # check that every book in the result
        self.assertEqual(len(response_json), len(books))

    def test_search_some_unique_title(self):
        books = [BookFactory() for _ in range(5)]
        book_to_search = books[1]

        response = self.client.get(reverse("search"), {"title": book_to_search.title})

        response_json = response.json()
        self.assertEqual(len(response_json), 1)
        self.assertEqual(response_json[0]["title"], book_to_search.title)
