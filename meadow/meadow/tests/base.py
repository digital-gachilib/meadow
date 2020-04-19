from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from meadow.tests.factories import UserFactory


class AuthorizedTestCase(TestCase):
    # an authentication of the client is done without any user actions

    def setUp(self):
        super().setUp()
        self.user = UserFactory()
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
