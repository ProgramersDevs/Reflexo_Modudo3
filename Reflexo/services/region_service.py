from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from ..models.region import Region


class RegionService:
    """Servicio para operaciones CRUD de Region"""
    
    @staticmethod
    def get_all_regions():
        """Obtiene todas las regiones"""
        try:
            regions = Region.objects.filter(deleted_at__isnull=True)
            return regions
        except Exception as e:
            raise Exception(f"Error al obtener regiones: {str(e)}")
    
    @staticmethod
    def get_region_by_id(region_id):
        """Obtiene una región por ID"""
        try:
            region = Region.objects.get(id=region_id, deleted_at__isnull=True)
            return region
        except Region.DoesNotExist:
            raise Exception(f"Región con ID {region_id} no encontrada")
        except Exception as e:
            raise Exception(f"Error al obtener región: {str(e)}")
    
    @staticmethod
    def create_region(data):
        """Crea una nueva región"""
        try:
            region = Region.objects.create(
                name=data.get('name'),
                ubigeo_code=data.get('ubigeo_code')
            )
            return region
        except Exception as e:
            raise Exception(f"Error al crear región: {str(e)}")
    
    @staticmethod
    def update_region(region_id, data):
        """Actualiza una región existente"""
        try:
            region = Region.objects.get(id=region_id, deleted_at__isnull=True)
            if 'name' in data:
                region.name = data['name']
            if 'ubigeo_code' in data:
                region.ubigeo_code = data['ubigeo_code']
            region.save()
            return region
        except Region.DoesNotExist:
            raise Exception(f"Región con ID {region_id} no encontrada")
        except Exception as e:
            raise Exception(f"Error al actualizar región: {str(e)}")
    
    @staticmethod
    def delete_region(region_id):
        """Elimina una región (soft delete)"""
        try:
            region = Region.objects.get(id=region_id, deleted_at__isnull=True)
            region.delete()  # Esto ejecuta el soft delete
            return True
        except Region.DoesNotExist:
            raise Exception(f"Región con ID {region_id} no encontrada")
        except Exception as e:
            raise Exception(f"Error al eliminar región: {str(e)}")
    
    @staticmethod
    def restore_region(region_id):
        """Restaura una región eliminada"""
        try:
            region = Region.objects.get(id=region_id, deleted_at__isnull=False)
            region.restore()
            return region
        except Region.DoesNotExist:
            raise Exception(f"Región con ID {region_id} no encontrada")
        except Exception as e:
            raise Exception(f"Error al restaurar región: {str(e)}")
    
    @staticmethod
    def search_regions(query):
        """Busca regiones por nombre"""
        try:
            regions = Region.objects.filter(
                name__icontains=query,
                deleted_at__isnull=True
            )
            return regions
        except Exception as e:
            raise Exception(f"Error al buscar regiones: {str(e)}")
    
    @staticmethod
    def get_regions_by_ubigeo_code(ubigeo_code):
        """Obtiene regiones por código ubigeo"""
        try:
            regions = Region.objects.filter(
                ubigeo_code__icontains=ubigeo_code,
                deleted_at__isnull=True
            )
            return regions
        except Exception as e:
            raise Exception(f"Error al buscar regiones por ubigeo: {str(e)}")
