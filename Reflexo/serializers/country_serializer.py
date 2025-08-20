from rest_framework import serializers
from ..models.country import Country


class CountrySerializer(serializers.ModelSerializer):
    """Serializer para el modelo Country que acepta todos los campos"""
    
    class Meta:
        model = Country
        fields = '__all__'  # Incluye todos los campos del modelo
        read_only_fields = ('id', 'created_at', 'updated_at')  # Campos de solo lectura


class CountryListSerializer(serializers.ModelSerializer):
    """Serializer para listar países con información básica"""
    
    class Meta:
        model = Country
        fields = ('id', 'name', 'ubigeo_code', 'created_at', 'updated_at')


class CountryCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear países"""
    
    class Meta:
        model = Country
        fields = ('name', 'ubigeo_code')


class CountryUpdateSerializer(serializers.ModelSerializer):
    """Serializer para actualizar países"""
    
    class Meta:
        model = Country
        fields = ('name', 'ubigeo_code')
        extra_kwargs = {
            'name': {'required': False},
            'ubigeo_code': {'required': False}
        }
