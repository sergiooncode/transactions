from django.contrib.auth.models import User
from rest_framework import generics

from users.serializers.create_user import UserCreateSerializer


class UserCreateController(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
