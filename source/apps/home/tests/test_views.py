from django.contrib.auth.models import User
from django.test import Client, TestCase
from source.apps.home.tests.factories import UserFactory


class UserLoginTestCase(TestCase):
    dummy_user = None
    url = "/login/"
    model = User

    @classmethod
    def setUpTestData(cls) -> None:
        cls.dummy_user = UserFactory()
        cls.dummy_client = Client()

    def test_user_login_get(self) -> None:
        _response = self.dummy_client.get(path=self.url)

        self.assertEqual(first=_response.status_code, second=200)

    def test_unregister_user_login_post(self) -> None:
        _response = self.dummy_client.post(path=self.url, data={"username": "example", "password": "example"})

        self.assertEqual(first=_response.status_code, second=401)
