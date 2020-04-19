from django.test import TestCase
from django.urls import reverse

from meadow.tests.factories.user import UserFactory


class AuthTestCase(TestCase):
    def test_get_method_not_allowed(self):
        # GET method is not allowed
        response = self.client.get(reverse("api_token_auth"))
        self.assertEqual(response.status_code, 405)

    def test_obtain_token_success(self):
        # firstly create a user for which we query an auth token
        user = UserFactory()

        response = self.client.post(
            reverse("api_token_auth"), data={"username": user.username, "password": user.real_password}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json())

    def test_obtain_token_wrong_credentials(self):
        response = self.client.post(
            reverse("api_token_auth"), data={"username": "Dummy fake boy", "password": "I don't like it"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("Unable to log in", str(response.content))
