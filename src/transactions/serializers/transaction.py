from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_bulk import BulkSerializerMixin, BulkListSerializer

from transactions.models import Transaction


class TransactionSerializer(BulkSerializerMixin, ModelSerializer):
    class Meta:
        model = Transaction
        list_serializer_class = BulkListSerializer
        fields = ["reference", "account", "type", "category", "amount"]

    def validate(self, attrs):
        reference = attrs["reference"]
        if Transaction.objects.filter(reference=reference).count() != 0:
            raise serializers.ValidationError("transaction reference must be unique")
        if attrs["type"] == "inflow" and attrs["amount"] < 0:
            raise serializers.ValidationError(
                "transaction with inflow type must " "have a negative amount"
            )
        if attrs["type"] == "outflow" and attrs["amount"] > 0:
            raise serializers.ValidationError(
                "transaction with outflow type must " "have a positive amount"
            )

        return attrs
