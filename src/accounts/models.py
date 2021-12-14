from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    account_number = models.CharField(max_length=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
