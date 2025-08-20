from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from Reflexo.models import Region
import json

# ============================================================================
# ENDPOINTS PARA REGIONES
# ============================================================================

@require_http_methods(["GET"])
def regions(request):
    """Listar todas las regiones"""
    try:
        regions = Region.objects.filter(deleted_at__isnull=True).values(
            'id', 'name', 'ubigeo_code', 'created_at', 'updated_at'
        )
        return JsonResponse({
            'success': True,
            'data': list(regions),
            'count': len(regions)
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@require_http_methods(["GET"])
def region_detail(request, region_id):
    """Obtener una región específica"""
    try:
        region = Region.objects.filter(id=region_id, deleted_at__isnull=True).values(
            'id', 'name', 'ubigeo_code', 'created_at', 'updated_at'
        ).first()
        
        if not region:
            return JsonResponse({
                'success': False,
                'error': 'Región no encontrada'
            }, status=404)
        
        return JsonResponse({
            'success': True,
            'data': region
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def region_create(request):
    """Crear una nueva región"""
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
        if ubigeo_code and Region.objects.filter(ubigeo_code=ubigeo_code).exists():
            return JsonResponse({
                'success': False,
                'error': 'El código de ubigeo ya existe'
            }, status=400)
        
        region = Region.objects.create(
            name=name,
            ubigeo_code=ubigeo_code
        )
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': region.id,
                'name': region.name,
                'ubigeo_code': region.ubigeo_code,
                'created_at': region.created_at,
                'updated_at': region.updated_at
            },
            'message': 'Región creada exitosamente'
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
def region_update(request, region_id):
    """Actualizar una región"""
    try:
        data = json.loads(request.body)
        region = Region.objects.filter(id=region_id, deleted_at__isnull=True).first()
        
        if not region:
            return JsonResponse({
                'success': False,
                'error': 'Región no encontrada'
            }, status=404)
        
        # Actualizar campos
        if 'name' in data:
            region.name = data['name']
        if 'ubigeo_code' in data:
            # Validar que el código sea único
            if Region.objects.filter(ubigeo_code=data['ubigeo_code']).exclude(id=region_id).exists():
                return JsonResponse({
                    'success': False,
                    'error': 'El código de ubigeo ya existe'
                }, status=400)
            region.ubigeo_code = data['ubigeo_code']
        
        region.save()
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': region.id,
                'name': region.name,
                'ubigeo_code': region.ubigeo_code,
                'created_at': region.created_at,
                'updated_at': region.updated_at
            },
            'message': 'Región actualizada exitosamente'
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
def region_delete(request, region_id):
    """Eliminar una región (soft delete)"""
    try:
        region = Region.objects.filter(id=region_id, deleted_at__isnull=True).first()
        
        if not region:
            return JsonResponse({
                'success': False,
                'error': 'Región no encontrada'
            }, status=404)
        
        # Verificar que no tenga provincias asociadas
        if region.provinces.exists():
            return JsonResponse({
                'success': False,
                'error': 'No se puede eliminar una región que tiene provincias asociadas'
            }, status=400)
        
        region.delete()  # Soft delete
        
        return JsonResponse({
            'success': True,
            'message': 'Región eliminada exitosamente'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)