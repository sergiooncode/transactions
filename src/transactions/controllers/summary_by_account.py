from django.db.models import Q, Sum
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from rest_framework import generics

from transactions.models import Transaction
from transactions.serializers.summary_by_account import SummaryByAccountSerializer


class SummaryByAccountController(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        username = kwargs["username"]
        queryset = (
            Transaction.objects.filter(account__user__username=username)
            .values("account")
            .annotate(
                total_inflow=Coalesce(Sum("amount", filter=Q(type="inflow")), 0.00)
            )
            .annotate(
                total_outflow=Coalesce(Sum("amount", filter=Q(type="outflow")), 0.00)
            )
            .annotate(balance=Sum("amount"))
        )
        results = SummaryByAccountSerializer(queryset, many=True).data

        return JsonResponse(results, safe=False)
