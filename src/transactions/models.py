from django.db import models


class Transaction(models.Model):
    reference = models.CharField(max_length=6)
    account = models.ForeignKey("accounts.Account", on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=7)
    category = models.CharField(max_length=20)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
