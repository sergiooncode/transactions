import json

from django.contrib.auth.models import User
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APIClient, APITestCase

from accounts.models import Account
from transactions.models import Transaction


class TestTransactionController(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        user = User.objects.create(username="bob_doe")
        self.account = Account.objects.create(account_number="C00099", user=user)

    def test_post_returns_400_when_account_doesnt_exist(self):
        response = self.client.post(
            "/transactions/",
            data=json.dumps(
                [
                    {
                        "reference": "000052",
                        "account": 100,
                        "date": "2020-01-13",
                        "amount": "-2500.13",
                        "type": "inflow",
                        "category": "salary",
                    }
                ]
            ),
            content_type="application/json",
        )

        self.assertEqual(400, response.status_code)
        self.assertEqual(
            [
                {
                    "account": [
                        ErrorDetail(
                            string='Invalid pk "100" - object does not exist.',
                            code="does_not_exist",
                        )
                    ]
                }
            ],
            response.data,
        )

    def test_post_returns_400_when_inflow_with_negative_amount(self):
        response = self.client.post(
            "/transactions/",
            data=json.dumps(
                [
                    {
                        "reference": "000052",
                        "account": self.account.id,
                        "date": "2020-01-13",
                        "amount": "-500.13",
                        "type": "inflow",
                        "category": "rent",
                    }
                ]
            ),
            content_type="application/json",
        )

        self.assertEqual(400, response.status_code)
        self.assertEqual(
            [
                {
                    "non_field_errors": [
                        ErrorDetail(
                            string="transaction with inflow type must have a negative amount",
                            code="invalid",
                        )
                    ]
                }
            ],
            response.data,
        )

    def test_post_returns_400_when_outflow_with_positive_amount(self):
        response = self.client.post(
            "/transactions/",
            data=json.dumps(
                [
                    {
                        "reference": "000052",
                        "account": self.account.id,
                        "date": "2020-01-13",
                        "amount": "2500.13",
                        "type": "outflow",
                        "category": "salary",
                    }
                ]
            ),
            content_type="application/json",
        )

        self.assertEqual(400, response.status_code)
        self.assertEqual(
            [
                {
                    "non_field_errors": [
                        ErrorDetail(
                            string="transaction with outflow type must have a positive amount",
                            code="invalid",
                        )
                    ]
                }
            ],
            response.data,
        )

    def test_post_returns_400_when_transaction_with_same_reference_exists(self):
        Transaction.objects.create(
            reference="000051",
            account=self.account,
            amount=-250.50,
            type="outflow",
            category="groceries",
        )
        response = self.client.post(
            "/transactions/",
            data=json.dumps(
                [
                    {
                        "reference": "000051",
                        "account": self.account.id,
                        "date": "2020-01-13",
                        "amount": "2500.13",
                        "type": "outflow",
                        "category": "salary",
                    }
                ]
            ),
            content_type="application/json",
        )

        self.assertEqual(400, response.status_code)
        self.assertEqual(
            [
                {
                    "non_field_errors": [
                        ErrorDetail(
                            string="transaction reference must be unique",
                            code="invalid",
                        )
                    ]
                }
            ],
            response.data,
        )
