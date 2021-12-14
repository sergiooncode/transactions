from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")

    class Meta:
        model = Account
        fields = ("account_number",1 "username")

    def validate(self, attrs):
        account_number = attrs["account_number"]
        if Account.objects.filter(account_number=account_number).count() != 0:
            raise serializers.ValidationError("account number must be unique")

        return attrs

    def create(self, validated_data):
        print(validated_data)
        user_data = validated_data.pop("user", None)
        user = User.objects.filter(
            username=user_data.get("username")
        ).all()[0]
        account = Account.objects.create(
            user=user,
            account_number=validated_data.get("account_number")
        )
        return account
