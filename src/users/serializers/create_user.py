from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import UserProfile


class UserCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user_profile.name")
    age = serializers.IntegerField(source="user_profile.age")

    class Meta:
        model = User
        fields = ("email", "name", "age")

    def create(self, validated_data):
        user_profile_data = validated_data.pop("user_profile", None)
        user = User.objects.create(
            email=validated_data["email"],
            username=user_profile_data.get("name").replace(" ", "_").lower(),
        )
        UserProfile.objects.create(
            user=user,
            age=user_profile_data.get("age"),
            name=user_profile_data.get("name"),
        )
        return user
