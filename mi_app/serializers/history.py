from rest_framework import serializers
from ..models import History

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ["id", "document_type", "document_number", "testimony", "private_observation", "observation", "height", "weight", "last_weight", "created_at", "updated_at"]
