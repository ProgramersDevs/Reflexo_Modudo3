from rest_framework import serializers
from ..models.diagnosis import Diagnosis
import re

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ['id', 'code', 'name']

    def validate_code(self, value):
        if not re.match(r'^[A-Za-z0-9]+$', value):
            raise serializers.ValidationError("El código solo debe contener letras y números.")
        if len(value) > 20:
            raise serializers.ValidationError("El código no debe superar los 20 caracteres.")
        return value

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("El nombre es obligatorio.")
        return value   