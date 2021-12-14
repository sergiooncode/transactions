from django.contrib.auth.models import User
from rest_framework import generics

from users.serializers.list_user import UserListSerializer
from users.serializers.retrieve_user import UserRetrieveSerializer


class UserRetrieveController(generics.RetrieveAPIView):
    queryset = User.objects.all()
    lookup_field = "username"
    serializer_class = UserRetrieveSerializer
