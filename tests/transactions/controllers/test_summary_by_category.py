from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase

from accounts.models import Account
from transactions.models import Transaction


class TestSummaryByAccountController(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_post_returns_405(self):
        response = self.client.post("/summary/bob_doe/category/")
        self.assertEqual(405, response.status_code)

    def test_(self):
        user_1 = User.objects.create(username="bob_doe")
        account_1 = Account.objects.create(account_number="C00099", user=user_1)
        account_2 = Account.objects.create(account_number="S00012", user=user_1)
        Transaction.objects.create(
            reference="000051",
            account=account_1,
            amount=-250.50,
            type="outflow",
            category="groceries",
        )
        Transaction.objects.create(
            reference="000052",
            account=account_1,
            amount=2500.50,
            type="inflow",
            category="salary",
        )
        Transaction.objects.create(
            reference="000053",
            account=account_2,
            amount=-500.50,
            type="outflow",
            category="groceries",
        )
        response = self.client.get("/summary/bob_doe/category/")

        self.assertEqual(200, response.status_code)
        self.assertEqual(
            {
                "inflow": {"salary": "2500.50"},
                "outflow": {"groceries": "-751.00"},
            },
            response.json(),
        )
