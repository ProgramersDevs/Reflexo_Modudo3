from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from ..models.district import District
from ..models.province import Province


class DistrictService:
    """Servicio para operaciones CRUD de District"""
    
    @staticmethod
    def get_all_districts():
        """Obtiene todos los distritos"""
        try:
            districts = District.objects.all()
            return districts
        except Exception as e:
            raise Exception(f"Error al obtener distritos: {str(e)}")
    
    @staticmethod
    def get_district_by_id(district_id):
        """Obtiene un distrito por ID"""
        try:
            district = District.objects.get(id=district_id)
            return district
        except District.DoesNotExist:
            raise Exception(f"Distrito con ID {district_id} no encontrado")
        except Exception as e:
            raise Exception(f"Error al obtener distrito: {str(e)}")
    
    @staticmethod
    def get_districts_by_province(province_id):
        """Obtiene distritos por provincia"""
        try:
            districts = District.objects.filter(province_id=province_id)
            return districts
        except Exception as e:
            raise Exception(f"Error al obtener distritos por provincia: {str(e)}")
    
    @staticmethod
    def create_district(data):
        """Crea un nuevo distrito"""
        try:
            province_id = data.get('province_id')
            if not province_id:
                raise Exception("province_id es requerido")
            
            province = Province.objects.get(id=province_id)
            district = District.objects.create(
                name=data.get('name'),
                province=province,
                ubigeo_code=data.get('ubigeo_code')
            )
            return district
        except Province.DoesNotExist:
            raise Exception(f"Provincia con ID {province_id} no encontrada")
        except Exception as e:
            raise Exception(f"Error al crear distrito: {str(e)}")
    
    @staticmethod
    def update_district(district_id, data):
        """Actualiza un distrito existente"""
        try:
            district = District.objects.get(id=district_id)
            
            if 'name' in data:
                district.name = data['name']
            if 'ubigeo_code' in data:
                district.ubigeo_code = data['ubigeo_code']
            if 'province_id' in data:
                province = Province.objects.get(id=data['province_id'])
                district.province = province
            
            district.save()
            return district
        except District.DoesNotExist:
            raise Exception(f"Distrito con ID {district_id} no encontrado")
        except Province.DoesNotExist:
            raise Exception(f"Provincia con ID {data.get('province_id')} no encontrada")
        except Exception as e:
            raise Exception(f"Error al actualizar distrito: {str(e)}")
    
    @staticmethod
    def delete_district(district_id):
        """Elimina un distrito"""
        try:
            district = District.objects.get(id=district_id)
            district.delete()
            return True
        except District.DoesNotExist:
            raise Exception(f"Distrito con ID {district_id} no encontrado")
        except Exception as e:
            raise Exception(f"Error al eliminar distrito: {str(e)}")
    
    @staticmethod
    def search_districts(query):
        """Busca distritos por nombre"""
        try:
            districts = District.objects.filter(name__icontains=query)
            return districts
        except Exception as e:
            raise Exception(f"Error al buscar distritos: {str(e)}")
    
    @staticmethod
    def get_districts_by_ubigeo_code(ubigeo_code):
        """Obtiene distritos por código ubigeo"""
        try:
            districts = District.objects.filter(ubigeo_code__icontains=ubigeo_code)
            return districts
        except Exception as e:
            raise Exception(f"Error al buscar distritos por ubigeo: {str(e)}")
    
    @staticmethod
    def get_districts_by_region(region_id):
        """Obtiene distritos por región (a través de provincias)"""
        try:
            districts = District.objects.filter(province__region_id=region_id)
            return districts
        except Exception as e:
            raise Exception(f"Error al obtener distritos por región: {str(e)}")
