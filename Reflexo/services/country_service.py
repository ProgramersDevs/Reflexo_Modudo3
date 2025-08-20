from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from ..models.country import Country


class CountryService:
    """Servicio para operaciones CRUD de Country"""
    
    @staticmethod
    def get_all_countries():
        """Obtiene todos los países"""
        try:
            countries = Country.objects.all()
            return countries
        except Exception as e:
            raise Exception(f"Error al obtener países: {str(e)}")
    
    @staticmethod
    def get_country_by_id(country_id):
        """Obtiene un país por ID"""
        try:
            country = Country.objects.get(id=country_id)
            return country
        except Country.DoesNotExist:
            raise Exception(f"País con ID {country_id} no encontrado")
        except Exception as e:
            raise Exception(f"Error al obtener país: {str(e)}")
    
    @staticmethod
    def create_country(data):
        """Crea un nuevo país"""
        try:
            country = Country.objects.create(
                name=data.get('name'),
                ubigeo_code=data.get('ubigeo_code')
            )
            return country
        except Exception as e:
            raise Exception(f"Error al crear país: {str(e)}")
    
    @staticmethod
    def update_country(country_id, data):
        """Actualiza un país existente"""
        try:
            country = Country.objects.get(id=country_id)
            if 'name' in data:
                country.name = data['name']
            if 'ubigeo_code' in data:
                country.ubigeo_code = data['ubigeo_code']
            country.save()
            return country
        except Country.DoesNotExist:
            raise Exception(f"País con ID {country_id} no encontrado")
        except Exception as e:
            raise Exception(f"Error al actualizar país: {str(e)}")
    
    @staticmethod
    def delete_country(country_id):
        """Elimina un país"""
        try:
            country = Country.objects.get(id=country_id)
            country.delete()
            return True
        except Country.DoesNotExist:
            raise Exception(f"País con ID {country_id} no encontrado")
        except Exception as e:
            raise Exception(f"Error al eliminar país: {str(e)}")
    
    @staticmethod
    def search_countries(query):
        """Busca países por nombre"""
        try:
            countries = Country.objects.filter(name__icontains=query)
            return countries
        except Exception as e:
            raise Exception(f"Error al buscar países: {str(e)}")
