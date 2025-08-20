from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from Reflexo.models import Province, Region
import json

# ============================================================================
# ENDPOINTS PARA PROVINCIAS
# ============================================================================

@require_http_methods(["GET"])
def provinces(request, region_id=None):
    """Listar provincias (opcionalmente filtradas por región)"""
    try:
        if region_id:
            provinces = Province.objects.filter(
                region_id=region_id
            ).values(
                'id', 'name', 'ubigeo_code', 'region__name', 'created_at', 'updated_at'
            )
        else:
            provinces = Province.objects.all().values(
                'id', 'name', 'ubigeo_code', 'region__name', 'created_at', 'updated_at'
            )
        
        return JsonResponse({
            'success': True,
            'data': list(provinces),
            'count': len(provinces)
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@require_http_methods(["GET"])
def province_detail(request, province_id):
    """Obtener una provincia específica"""
    try:
        province = Province.objects.filter(id=province_id).values(
            'id', 'name', 'ubigeo_code', 'region__name', 'region__id', 'created_at', 'updated_at'
        ).first()
        
        if not province:
            return JsonResponse({
                'success': False,
                'error': 'Provincia no encontrada'
            }, status=404)
        
        return JsonResponse({
            'success': True,
            'data': province
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def province_create(request):
    """Crear una nueva provincia"""
    try:
        data = json.loads(request.body)
        name = data.get('name')
        region_id = data.get('region_id')
        ubigeo_code = data.get('ubigeo_code')
        
        if not name or not region_id:
            return JsonResponse({
                'success': False,
                'error': 'El nombre y la región son obligatorios'
            }, status=400)
        
        # Verificar que la región existe
        try:
            region = Region.objects.get(id=region_id, deleted_at__isnull=True)
        except Region.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': 'La región especificada no existe'
            }, status=400)
        
        # Validar que el código de ubigeo sea único
        if ubigeo_code and Province.objects.filter(ubigeo_code=ubigeo_code).exists():
            return JsonResponse({
                'success': False,
                'error': 'El código de ubigeo ya existe'
            }, status=400)
        
        province = Province.objects.create(
            name=name,
            region=region,
            ubigeo_code=ubigeo_code
        )
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': province.id,
                'name': province.name,
                'ubigeo_code': province.ubigeo_code,
                'region__name': province.region.name,
                'created_at': province.created_at,
                'updated_at': province.updated_at
            },
            'message': 'Provincia creada exitosamente'
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
def province_update(request, province_id):
    """Actualizar una provincia"""
    try:
        data = json.loads(request.body)
        province = Province.objects.filter(id=province_id).first()
        
        if not province:
            return JsonResponse({
                'success': False,
                'error': 'Provincia no encontrada'
            }, status=404)
        
        # Actualizar campos
        if 'name' in data:
            province.name = data['name']
        if 'region_id' in data:
            try:
                region = Region.objects.get(id=data['region_id'], deleted_at__isnull=True)
                province.region = region
            except Region.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'error': 'La región especificada no existe'
                }, status=400)
        if 'ubigeo_code' in data:
            # Validar que el código sea único
            if Province.objects.filter(ubigeo_code=data['ubigeo_code']).exclude(id=province_id).exists():
                return JsonResponse({
                    'success': False,
                    'error': 'El código de ubigeo ya existe'
                }, status=400)
            province.ubigeo_code = data['ubigeo_code']
        
        province.save()
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': province.id,
                'name': province.name,
                'ubigeo_code': province.ubigeo_code,
                'region__name': province.region.name,
                'created_at': province.created_at,
                'updated_at': province.updated_at
            },
            'message': 'Provincia actualizada exitosamente'
        })
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
@require_http_methods(["DELETE"])
def province_delete(request, province_id):
    """Eliminar una provincia"""
    try:
        province = Province.objects.filter(id=province_id).first()
        
        if not province:
            return JsonResponse({
                'success': False,
                'error': 'Provincia no encontrada'
            }, status=404)
        
        # Verificar que no tenga distritos asociados
        if province.districts.exists():
            return JsonResponse({
                'success': False,
                'error': 'No se puede eliminar una provincia que tiene distritos asociados'
            }, status=400)
        
        province.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'Provincia eliminada exitosamente'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)