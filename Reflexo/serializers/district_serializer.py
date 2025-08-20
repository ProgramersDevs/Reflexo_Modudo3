from rest_framework import serializers
from ..models.district import District
from .province_serializer import ProvinceListSerializer
from .region_serializer import RegionListSerializer


class DistrictSerializer(serializers.ModelSerializer):
    """Serializer para el modelo District que acepta todos los campos"""
    
    class Meta:
        model = District
        fields = '__all__'  # Incluye todos los campos del modelo
        read_only_fields = ('id', 'created_at', 'updated_at')  # Campos de solo lectura


class DistrictListSerializer(serializers.ModelSerializer):
    """Serializer para listar distritos con información básica"""
    
    class Meta:
        model = District
        fields = ('id', 'name', 'ubigeo_code', 'province', 'created_at', 'updated_at')


class DistrictCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear distritos"""
    
    class Meta:
        model = District
        fields = ('name', 'ubigeo_code', 'province')


class DistrictUpdateSerializer(serializers.ModelSerializer):
    """Serializer para actualizar distritos"""
    
    class Meta:
        model = District
        fields = ('name', 'ubigeo_code', 'province')
        extra_kwargs = {
            'name': {'required': False},
            'ubigeo_code': {'required': False},
            'province': {'required': False}
        }


class DistrictDetailSerializer(serializers.ModelSerializer):
    """Serializer para mostrar detalles de distrito con información de provincia"""
    
    province = ProvinceListSerializer(read_only=True)
    
    class Meta:
        model = District
        fields = ('id', 'name', 'ubigeo_code', 'province', 'created_at', 'updated_at')


class DistrictWithProvinceSerializer(serializers.ModelSerializer):
    """Serializer para distritos con información completa de provincia"""
    
    province_name = serializers.CharField(source='province.name', read_only=True)
    province_ubigeo = serializers.CharField(source='province.ubigeo_code', read_only=True)
    
    class Meta:
        model = District
        fields = ('id', 'name', 'ubigeo_code', 'province', 'province_name', 'province_ubigeo', 'created_at', 'updated_at')


class DistrictWithRegionSerializer(serializers.ModelSerializer):
    """Serializer para distritos con información completa de provincia y región"""
    
    province_name = serializers.CharField(source='province.name', read_only=True)
    province_ubigeo = serializers.CharField(source='province.ubigeo_code', read_only=True)
    region_name = serializers.CharField(source='province.region.name', read_only=True)
    region_ubigeo = serializers.CharField(source='province.region.ubigeo_code', read_only=True)
    
    class Meta:
        model = District
        fields = (
            'id', 'name', 'ubigeo_code', 'province', 
            'province_name', 'province_ubigeo',
            'region_name', 'region_ubigeo',
            'created_at', 'updated_at'
        )
