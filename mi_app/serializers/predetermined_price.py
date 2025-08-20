from rest_framework import serializers
from ..models import PredeterminedPrice

class PredeterminedPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredeterminedPrice
        fields = ["id", "name", "price", "created_at", "updated_at"]
