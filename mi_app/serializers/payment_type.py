from rest_framework import serializers
from ..models import PaymentType

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ["id", "code", "name", "created_at", "updated_at"]
