from rest_framework import serializers
from ..models.region import Region


class RegionSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Region que acepta todos los campos"""
    
    class Meta:
        model = Region
        fields = '__all__'  # Incluye todos los campos del modelo
        read_only_fields = ('id', 'created_at', 'updated_at')  # Campos de solo lectura


class RegionListSerializer(serializers.ModelSerializer):
    """Serializer para listar regiones con información básica"""
    
    class Meta:
        model = Region
        fields = ('id', 'name', 'ubigeo_code', 'created_at', 'updated_at')


class RegionCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear regiones"""
    
    class Meta:
        model = Region
        fields = ('name', 'ubigeo_code')


class RegionUpdateSerializer(serializers.ModelSerializer):
    """Serializer para actualizar regiones"""
    
    class Meta:
        model = Region
        fields = ('name', 'ubigeo_code')
        extra_kwargs = {
            'name': {'required': False},
            'ubigeo_code': {'required': False}
        }


class RegionDetailSerializer(serializers.ModelSerializer):
    """Serializer para mostrar detalles de región con información completa"""
    
    class Meta:
        model = Region
        fields = ('id', 'name', 'ubigeo_code', 'deleted_at', 'created_at', 'updated_at')
