from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from Reflexo.models import District, Province
import json

# ============================================================================
# ENDPOINTS PARA DISTRITOS
# ============================================================================

@require_http_methods(["GET"])
def districts(request, province_id=None):
    """Listar distritos (opcionalmente filtrados por provincia)"""
    try:
        if province_id:
            districts = District.objects.filter(
                province_id=province_id
            ).values(
                'id', 'name', 'ubigeo_code', 'province__name', 'created_at', 'updated_at'
            )
        else:
            districts = District.objects.all().values(
                'id', 'name', 'ubigeo_code', 'province__name', 'created_at', 'updated_at'
            )
        
        return JsonResponse({
            'success': True,
            'data': list(districts),
            'count': len(districts)
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@require_http_methods(["GET"])
def district_detail(request, district_id):
    """Obtener un distrito específico"""
    try:
        district = District.objects.filter(id=district_id).values(
            'id', 'name', 'ubigeo_code', 'province__name', 'province__id', 'created_at', 'updated_at'
        ).first()
        
        if not district:
            return JsonResponse({
                'success': False,
                'error': 'Distrito no encontrado'
            }, status=404)
        
        return JsonResponse({
            'success': True,
            'data': district
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def district_create(request):
    """Crear un nuevo distrito"""
    try:
        data = json.loads(request.body)
        name = data.get('name')
        province_id = data.get('province_id')
        ubigeo_code = data.get('ubigeo_code')
        
        if not name or not province_id:
            return JsonResponse({
                'success': False,
                'error': 'El nombre y la provincia son obligatorios'
            }, status=400)
        
        # Verificar que la provincia existe
        try:
            province = Province.objects.get(id=province_id)
        except Province.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': 'La provincia especificada no existe'
            }, status=400)
        
        # Validar que el código de ubigeo sea único
        if ubigeo_code and District.objects.filter(ubigeo_code=ubigeo_code).exists():
            return JsonResponse({
                'success': False,
                'error': 'El código de ubigeo ya existe'
            }, status=400)
        
        district = District.objects.create(
            name=name,
            province=province,
            ubigeo_code=ubigeo_code
        )
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': district.id,
                'name': district.name,
                'ubigeo_code': district.ubigeo_code,
                'province__name': district.province.name,
                'created_at': district.created_at,
                'updated_at': district.updated_at
            },
            'message': 'Distrito creado exitosamente'
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
def district_update(request, district_id):
    """Actualizar un distrito"""
    try:
        data = json.loads(request.body)
        district = District.objects.filter(id=district_id).first()
        
        if not district:
            return JsonResponse({
                'success': False,
                'error': 'Distrito no encontrado'
            }, status=404)
        
        # Actualizar campos
        if 'name' in data:
            district.name = data['name']
        if 'province_id' in data:
            try:
                province = Province.objects.get(id=data['province_id'])
                district.province = province
            except Province.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'error': 'La provincia especificada no existe'
                }, status=400)
        if 'ubigeo_code' in data:
            # Validar que el código sea único
            if District.objects.filter(ubigeo_code=data['ubigeo_code']).exclude(id=district_id).exists():
                return JsonResponse({
                    'success': False,
                    'error': 'El código de ubigeo ya existe'
                }, status=400)
            district.ubigeo_code = data['ubigeo_code']
        
        district.save()
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': district.id,
                'name': district.name,
                'ubigeo_code': district.ubigeo_code,
                'province__name': district.province.name,
                'created_at': district.created_at,
                'updated_at': district.updated_at
            },
            'message': 'Distrito actualizado exitosamente'
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
def district_delete(request, district_id):
    """Eliminar un distrito"""
    try:
        district = District.objects.filter(id=district_id).first()
        
        if not district:
            return JsonResponse({
                'success': False,
                'error': 'Distrito no encontrado'
            }, status=404)
        
        district.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'Distrito eliminado exitosamente'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)
