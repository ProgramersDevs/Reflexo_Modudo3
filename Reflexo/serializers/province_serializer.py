from rest_framework import serializers
from ..models.province import Province
from .region_serializer import RegionListSerializer


class ProvinceSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Province que acepta todos los campos"""
    
    class Meta:
        model = Province
        fields = '__all__'  # Incluye todos los campos del modelo
        read_only_fields = ('id', 'created_at', 'updated_at')  # Campos de solo lectura


class ProvinceListSerializer(serializers.ModelSerializer):
    """Serializer para listar provincias con información básica"""
    
    class Meta:
        model = Province
        fields = ('id', 'name', 'ubigeo_code', 'region', 'created_at', 'updated_at')


class ProvinceCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear provincias"""
    
    class Meta:
        model = Province
        fields = ('name', 'ubigeo_code', 'region')


class ProvinceUpdateSerializer(serializers.ModelSerializer):
    """Serializer para actualizar provincias"""
    
    class Meta:
        model = Province
        fields = ('name', 'ubigeo_code', 'region')
        extra_kwargs = {
            'name': {'required': False},
            'ubigeo_code': {'required': False},
            'region': {'required': False}
        }


class ProvinceDetailSerializer(serializers.ModelSerializer):
    """Serializer para mostrar detalles de provincia con información de región"""
    
    region = RegionListSerializer(read_only=True)
    
    class Meta:
        model = Province
        fields = ('id', 'name', 'ubigeo_code', 'region', 'created_at', 'updated_at')


class ProvinceWithRegionSerializer(serializers.ModelSerializer):
    """Serializer para provincias con información completa de región"""
    
    region_name = serializers.CharField(source='region.name', read_only=True)
    region_ubigeo = serializers.CharField(source='region.ubigeo_code', read_only=True)
    
    class Meta:
        model = Province
        fields = ('id', 'name', 'ubigeo_code', 'region', 'region_name', 'region_ubigeo', 'created_at', 'updated_at')
