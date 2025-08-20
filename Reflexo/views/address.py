from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from ..services.address_service import AddressService
from ..serializers.address_serializer import (
    AddressSerializer,
    AddressListSerializer,
    AddressCreateSerializer,
    AddressUpdateSerializer,
    AddressDetailSerializer,
    AddressWithUbigeoSerializer,
    AddressCompactSerializer
)


@require_http_methods(["GET"])
def addresses(request):
    """Lista todas las direcciones"""
    try:
        addresses = AddressService.get_all_addresses()
        serializer = AddressListSerializer(addresses, many=True)
        return JsonResponse({
            'success': True,
            'data': serializer.data,
            'count': len(serializer.data)
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@require_http_methods(["GET"])
def address_detail(request, address_id):
    """Obtiene el detalle de una dirección"""
    try:
        address = AddressService.get_address_by_id(address_id)
        serializer = AddressDetailSerializer(address)
        return JsonResponse({
            'success': True,
            'data': serializer.data
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=404)


@csrf_exempt
@require_http_methods(["POST"])
def address_create(request):
    """Crea una nueva dirección"""
    try:
        data = json.loads(request.body)
        serializer = AddressCreateSerializer(data=data)
        
        if serializer.is_valid():
            address = AddressService.create_address(serializer.validated_data)
            response_serializer = AddressSerializer(address)
            return JsonResponse({
                'success': True,
                'data': response_serializer.data,
                'message': 'Dirección creada exitosamente'
            }, status=201)
        else:
            return JsonResponse({
                'success': False,
                'error': 'Datos inválidos',
                'details': serializer.errors
            }, status=400)
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'JSON inválido'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["PUT"])
def address_update(request, address_id):
    """Actualiza una dirección existente"""
    try:
        data = json.loads(request.body)
        serializer = AddressUpdateSerializer(data=data, partial=True)
        
        if serializer.is_valid():
            address = AddressService.update_address(address_id, serializer.validated_data)
            response_serializer = AddressSerializer(address)
            return JsonResponse({
                'success': True,
                'data': response_serializer.data,
                'message': 'Dirección actualizada exitosamente'
            })
        else:
            return JsonResponse({
                'success': False,
                'error': 'Datos inválidos',
                'details': serializer.errors
            }, status=400)
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'JSON inválido'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def address_delete(request, address_id):
    """Elimina una dirección"""
    try:
        AddressService.delete_address(address_id)
        return JsonResponse({
            'success': True,
            'message': 'Dirección eliminada exitosamente'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@require_http_methods(["GET"])
def addresses_by_country(request, country_id):
    """Obtiene direcciones por país"""
    try:
        addresses = AddressService.get_addresses_by_country(country_id)
        serializer = AddressListSerializer(addresses, many=True)
        return JsonResponse({
            'success': True,
            'data': serializer.data,
            'count': len(serializer.data)
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@require_http_methods(["GET"])
def addresses_by_region(request, region_id):
    """Obtiene direcciones por región"""
    try:
        addresses = AddressService.get_addresses_by_region(region_id)
        serializer = AddressListSerializer(addresses, many=True)
        return JsonResponse({
            'success': True,
            'data': serializer.data,
            'count': len(serializer.data)
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@require_http_methods(["GET"])
def addresses_by_province(request, province_id):
    """Obtiene direcciones por provincia"""
    try:
        addresses = AddressService.get_addresses_by_province(province_id)
        serializer = AddressListSerializer(addresses, many=True)
        return JsonResponse({
            'success': True,
            'data': serializer.data,
            'count': len(serializer.data)
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@require_http_methods(["GET"])
def addresses_by_district(request, district_id):
    """Obtiene direcciones por distrito"""
    try:
        addresses = AddressService.get_addresses_by_district(district_id)
        serializer = AddressListSerializer(addresses, many=True)
        return JsonResponse({
            'success': True,
            'data': serializer.data,
            'count': len(serializer.data)
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@require_http_methods(["GET"])
def search_addresses(request):
    """Busca direcciones por query"""
    try:
        query = request.GET.get('q', '')
        if not query:
            return JsonResponse({
                'success': False,
                'error': 'Parámetro de búsqueda requerido'
            }, status=400)
        
        addresses = AddressService.search_addresses(query)
        serializer = AddressCompactSerializer(addresses, many=True)
        return JsonResponse({
            'success': True,
            'data': serializer.data,
            'count': len(serializer.data),
            'query': query
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@require_http_methods(["GET"])
def addresses_by_ubigeo(request):
    """Obtiene direcciones por código ubigeo"""
    try:
        ubigeo_code = request.GET.get('ubigeo', '')
        if not ubigeo_code:
            return JsonResponse({
                'success': False,
                'error': 'Código ubigeo requerido'
            }, status=400)
        
        addresses = AddressService.get_addresses_by_ubigeo(ubigeo_code)
        serializer = AddressWithUbigeoSerializer(addresses, many=True)
        return JsonResponse({
            'success': True,
            'data': serializer.data,
            'count': len(serializer.data),
            'ubigeo_code': ubigeo_code
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def address_restore(request, address_id):
    """Restaura una dirección eliminada"""
    try:
        address = AddressService.restore_address(address_id)
        serializer = AddressSerializer(address)
        return JsonResponse({
            'success': True,
            'data': serializer.data,
            'message': 'Dirección restaurada exitosamente'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)
