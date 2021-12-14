from django.contrib.auth.models import User
from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user_profile.name")
    age = serializers.IntegerField(source="user_profile.age")

    class Meta:
        model = User
        fields = ("email", "name", "age", "username")
