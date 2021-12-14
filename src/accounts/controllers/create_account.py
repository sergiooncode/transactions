from django.contrib.auth.models import User
from rest_framework import generics

from accounts.serializers.account import AccountSerializer


class AccountCreateController(generics.CreateAPIView):
    serializer_class = AccountSerializer
