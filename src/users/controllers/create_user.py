from rest_framework import generics

from users.serializers.create_user import UserCreateSerializer


class UserCreateController(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
