from rest_framework import serializers
from ..models.diagnosis import Diagnosis
import re

class DiagnosisSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Diagnosis."""
    
    class Meta:
        model = Diagnosis
        fields = [
            'id', 'code', 'name', 'description',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_code(self, value):
        """Validar que el código solo contenga letras y números."""
        if not re.match(r'^[A-Za-z0-9]+$', value):
            raise serializers.ValidationError("El código solo debe contener letras y números.")
        if len(value) > 10:
            raise serializers.ValidationError("El código no debe superar los 10 caracteres.")
        
        # Validar que el código sea único
        if Diagnosis.objects.filter(code=value).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError("Ya existe un diagnóstico con este código.")
        return value

    def validate_name(self, value):
        """Validar que el nombre no esté vacío."""
        if not value.strip():
            raise serializers.ValidationError("El nombre es obligatorio.")
        return value

class DiagnosisListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listar diagnósticos."""
    
    class Meta:
        model = Diagnosis
        fields = ['id', 'code', 'name', 'created_at']   