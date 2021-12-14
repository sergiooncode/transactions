from django.contrib.auth.models import User
from rest_framework import generics

from users.serializers.list_user import UserListSerializer


class UserListController(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
