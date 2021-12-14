from django.db.models import Sum
from django.http import JsonResponse
from rest_framework import generics

from transactions.models import Transaction
from transactions.serializers.summary_by_category import SummaryByCategorySerializer


class SummaryByCategoryController(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        username = kwargs["username"]
        queryset = (
            Transaction.objects.filter(account__user__username=username)
            .values("type", "category")
            .annotate(Sum("amount"))
        )
        results = SummaryByCategorySerializer(queryset).data

        return JsonResponse(results)
