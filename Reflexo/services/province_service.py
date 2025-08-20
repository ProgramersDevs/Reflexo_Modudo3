from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from ..models.province import Province
from ..models.region import Region


class ProvinceService:
    """Servicio para operaciones CRUD de Province"""
    
    @staticmethod
    def get_all_provinces():
        """Obtiene todas las provincias"""
        try:
            provinces = Province.objects.all()
            return provinces
        except Exception as e:
            raise Exception(f"Error al obtener provincias: {str(e)}")
    
    @staticmethod
    def get_province_by_id(province_id):
        """Obtiene una provincia por ID"""
        try:
            province = Province.objects.get(id=province_id)
            return province
        except Province.DoesNotExist:
            raise Exception(f"Provincia con ID {province_id} no encontrada")
        except Exception as e:
            raise Exception(f"Error al obtener provincia: {str(e)}")
    
    @staticmethod
    def get_provinces_by_region(region_id):
        """Obtiene provincias por región"""
        try:
            provinces = Province.objects.filter(region_id=region_id)
            return provinces
        except Exception as e:
            raise Exception(f"Error al obtener provincias por región: {str(e)}")
    
    @staticmethod
    def create_province(data):
        """Crea una nueva provincia"""
        try:
            region_id = data.get('region_id')
            if not region_id:
                raise Exception("region_id es requerido")
            
            region = Region.objects.get(id=region_id)
            province = Province.objects.create(
                name=data.get('name'),
                region=region,
                ubigeo_code=data.get('ubigeo_code')
            )
            return province
        except Region.DoesNotExist:
            raise Exception(f"Región con ID {region_id} no encontrada")
        except Exception as e:
            raise Exception(f"Error al crear provincia: {str(e)}")
    
    @staticmethod
    def update_province(province_id, data):
        """Actualiza una provincia existente"""
        try:
            province = Province.objects.get(id=province_id)
            
            if 'name' in data:
                province.name = data['name']
            if 'ubigeo_code' in data:
                province.ubigeo_code = data['ubigeo_code']
            if 'region_id' in data:
                region = Region.objects.get(id=data['region_id'])
                province.region = region
            
            province.save()
            return province
        except Province.DoesNotExist:
            raise Exception(f"Provincia con ID {province_id} no encontrada")
        except Region.DoesNotExist:
            raise Exception(f"Región con ID {data.get('region_id')} no encontrada")
        except Exception as e:
            raise Exception(f"Error al actualizar provincia: {str(e)}")
    
    @staticmethod
    def delete_province(province_id):
        """Elimina una provincia"""
        try:
            province = Province.objects.get(id=province_id)
            province.delete()
            return True
        except Province.DoesNotExist:
            raise Exception(f"Provincia con ID {province_id} no encontrada")
        except Exception as e:
            raise Exception(f"Error al eliminar provincia: {str(e)}")
    
    @staticmethod
    def search_provinces(query):
        """Busca provincias por nombre"""
        try:
            provinces = Province.objects.filter(name__icontains=query)
            return provinces
        except Exception as e:
            raise Exception(f"Error al buscar provincias: {str(e)}")
    
    @staticmethod
    def get_provinces_by_ubigeo_code(ubigeo_code):
        """Obtiene provincias por código ubigeo"""
        try:
            provinces = Province.objects.filter(ubigeo_code__icontains=ubigeo_code)
            return provinces
        except Exception as e:
            raise Exception(f"Error al buscar provincias por ubigeo: {str(e)}")
