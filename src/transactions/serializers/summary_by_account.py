from rest_framework import serializers


class SummaryByAccountSerializer(serializers.Serializer):
    account = serializers.CharField()
    total_inflow = serializers.DecimalField(max_digits=None, decimal_places=2)
    total_outflow = serializers.DecimalField(max_digits=None, decimal_places=2)
    balance = serializers.DecimalField(max_digits=None, decimal_places=2)
