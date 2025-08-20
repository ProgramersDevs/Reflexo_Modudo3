from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from Reflexo.models import Country
import json

# ============================================================================
# ENDPOINTS PARA PAÍSES
# ============================================================================

@require_http_methods(["GET"])
def countries(request):
    """Listar todos los países"""
    try:
        countries = Country.objects.all().values('id', 'name', 'ubigeo_code', 'created_at', 'updated_at')
        return JsonResponse({
            'success': True,
            'data': list(countries),
            'count': len(countries)
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@require_http_methods(["GET"])
def country_detail(request, country_id):
    """Obtener un país específico"""
    try:
        country = Country.objects.filter(id=country_id).values(
            'id', 'name', 'ubigeo_code', 'created_at', 'updated_at'
        ).first()
        
        if not country:
            return JsonResponse({
                'success': False,
                'error': 'País no encontrado'
            }, status=404)
        
        return JsonResponse({
            'success': True,
            'data': country
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def country_create(request):
    """Crear un nuevo país"""
    try:
        data = json.loads(request.body)
        name = data.get('name')
        ubigeo_code = data.get('ubigeo_code')
        
        if not name:
            return JsonResponse({
                'success': False,
                'error': 'El nombre es obligatorio'
            }, status=400)
        
        # Validar que el código de ubigeo sea único
        if ubigeo_code and Country.objects.filter(ubigeo_code=ubigeo_code).exists():
            return JsonResponse({
                'success': False,
                'error': 'El código de ubigeo ya existe'
            }, status=400)
        
        country = Country.objects.create(
            name=name,
            ubigeo_code=ubigeo_code
        )
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': country.id,
                'name': country.name,
                'ubigeo_code': country.ubigeo_code,
                'created_at': country.created_at,
                'updated_at': country.updated_at
            },
            'message': 'País creado exitosamente'
        }, status=201)
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'JSON inválido'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["PUT"])
def country_update(request, country_id):
    """Actualizar un país"""
    try:
        data = json.loads(request.body)
        country = Country.objects.get(id=country_id)
        
        # Actualizar campos
        if 'name' in data:
            country.name = data['name']
        if 'ubigeo_code' in data:
            # Validar que el código sea único si se proporciona
            if data['ubigeo_code'] and Country.objects.filter(ubigeo_code=data['ubigeo_code']).exclude(id=country_id).exists():
                return JsonResponse({
                    'success': False,
                    'error': 'El código de ubigeo ya existe'
                }, status=400)
            country.ubigeo_code = data['ubigeo_code']
        
        country.save()
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': country.id,
                'name': country.name,
                'ubigeo_code': country.ubigeo_code,
                'created_at': country.created_at,
                'updated_at': country.updated_at
            },
            'message': 'País actualizado exitosamente'
        })
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'JSON inválido'
        }, status=400)
    except Country.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'País no encontrado'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["DELETE"])
def country_delete(request, country_id):
    """Eliminar un país"""
    try:
        country = Country.objects.get(id=country_id)
        country.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'País eliminado exitosamente'
        })
    except Country.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'País no encontrado'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)
