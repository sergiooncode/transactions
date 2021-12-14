from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase

from accounts.models import Account
from transactions.models import Transaction


class TestSummaryByAccountController(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_post_returns_405(self):
        response = self.client.post("/summary/bob_doe/account/")
        self.assertEqual(405, response.status_code)

    def test_(self):
        user_1 = User.objects.create(username="bob_doe")
        account_1 = Account.objects.create(account_number="C00099", user=user_1)
        account_2 = Account.objects.create(account_number="S00012", user=user_1)
        Transaction.objects.create(
            reference="000051",
            account=account_1,
            amount=2500.50,
            type="inflow",
            category="salary",
        )
        Transaction.objects.create(
            reference="000052",
            account=account_2,
            amount=-500.50,
            type="outflow",
            category="rent",
        )
        response = self.client.get("/summary/bob_doe/account/")

        self.assertEqual(200, response.status_code)
        self.assertEqual(
            [
                {
                    "account": "1",
                    "total_inflow": "2500.50",
                    "total_outflow": "0.00",
                    "balance": "2500.50",
                },
                {
                    "account": "2",
                    "total_inflow": "0.00",
                    "total_outflow": "-500.50",
                    "balance": "-500.50",
                },
            ],
            response.json(),
        )
