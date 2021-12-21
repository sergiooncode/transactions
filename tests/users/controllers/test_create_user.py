import json

from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase


class TestUserCreateController(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_get_returns_405(self):
        response = self.client.get("/users/create/")
        self.assertEqual(405, response.status_code)

    def test_creates_user_successfully(self):
        response = self.client.post(
            "/users/create/",
            data=json.dumps({"name": "Bob Doe", "email": "bob@email.com", "age": "37"}),
            content_type="application/json",
        )

        self.assertEqual(201, response.status_code)
        self.assertEqual(
            {"email": "bob@email.com", "name": "Bob Doe", "age": 37},
            response.data,
        )
        users = User.objects.all()
        self.assertEqual(1, len(users))
        self.assertEqual("bob_doe", users[0].username)
        self.assertEqual("bob@email.com", users[0].email)
        self.assertEqual(37, users[0].user_profile.age)
        self.assertEqual("Bob Doe", users[0].user_profile.name)
