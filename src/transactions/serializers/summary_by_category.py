from rest_framework import serializers


class SummaryByCategorySerializer(serializers.Serializer):
    def to_representation(self, instance):
        representation = {"inflow": {}, "outflow": {}}
        for o in instance.all():
            if o["type"] == "inflow":
                representation["inflow"][o["category"]] = format(
                    o["amount__sum"], ".2f"
                )
            if o["type"] == "outflow":
                representation["outflow"][o["category"]] = format(
                    o["amount__sum"], ".2f"
                )

        return representation
