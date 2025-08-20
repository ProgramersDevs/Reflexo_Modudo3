from django.urls import path
#from .views import addresses
from .views import (
    # Vistas web
    home_view,
    countries_view,
    regions_view,
    provinces_view,
    districts_view,
    debug_view,
    
    # API endpoints v1
    api_countries,
    api_regions,
    api_provinces,
    api_districts,
    
    # CRUD endpoints - Regiones
    regions,
    region_detail,
    region_create,
    region_update,
    region_delete,
    
    # CRUD endpoints - Provincias
    provinces,
    province_detail,
    province_create,
    province_update,
    province_delete,
    
    # CRUD endpoints - Distritos
    districts,
    district_detail,
    district_create,
    district_update,
    district_delete,
    
    # CRUD endpoints - Países
    countries,
    country_create,
    country_update,
    country_delete,
    
    # CRUD endpoints - Direcciones (comentado temporalmente)
    # addresses,
    # address_detail,
    # address_create,
    # address_update,
    # address_delete,
    # addresses_by_country,
    # addresses_by_region,
    # addresses_by_province,
    # addresses_by_district,
    # search_addresses,
    # addresses_by_ubigeo,
    # address_restore,
)

app_name = 'reflexo'

urlpatterns = [
    # Vistas web
    path('', home_view, name='home'),
    path('debug/', debug_view, name='debug_view'),
    path('countries/', countries_view, name='countries_view'),
    path('regions/', regions_view, name='regions_view'),
    path('provinces/', provinces_view, name='provinces_view'),
    path('districts/', districts_view, name='districts_view'),

    # API endpoints - versiones simples y principales
    path('api/countries/', countries, name='list_countries'),
    path('api/regions/', regions, name='list_regions'),
    path('api/provinces/', provinces, name='list_provinces'),
    path('api/districts/', districts, name='list_districts'),

    # API endpoints v2 (si las necesitas, sino elimina)
    path('api/v2/countries/', api_countries, name='api_countries'),
    path('api/v2/regions/', api_regions, name='api_regions'),
    path('api/v2/provinces/', api_provinces, name='api_provinces'),
    path('api/v2/districts/', api_districts, name='api_districts'),

    # API endpoints v3 - CRUD completo Ubigeo
    # Regiones
    path('api/v3/regions/', regions, name='ubigeo_regions'),
    path('api/v3/regions/create/', region_create, name='ubigeo_region_create'),
    path('api/v3/regions/<int:region_id>/', region_detail, name='ubigeo_region_detail'),
    path('api/v3/regions/<int:region_id>/update/', region_update, name='ubigeo_region_update'),
    path('api/v3/regions/<int:region_id>/delete/', region_delete, name='ubigeo_region_delete'),

    # Provincias
    path('api/v3/provinces/', provinces, name='ubigeo_provinces'),
    path('api/v3/provinces/create/', province_create, name='ubigeo_province_create'),
    path('api/v3/provinces/<int:province_id>/', province_detail, name='ubigeo_province_detail'),
    path('api/v3/provinces/<int:province_id>/update/', province_update, name='ubigeo_province_update'),
    path('api/v3/provinces/<int:province_id>/delete/', province_delete, name='ubigeo_province_delete'),
    path('api/v3/regions/<int:region_id>/provinces/', provinces, name='ubigeo_provinces_by_region'),

    # Distritos
    path('api/v3/districts/', districts, name='ubigeo_districts'),
    path('api/v3/districts/create/', district_create, name='ubigeo_district_create'),
    path('api/v3/districts/<int:district_id>/', district_detail, name='ubigeo_district_detail'),
    path('api/v3/districts/<int:district_id>/update/', district_update, name='ubigeo_district_update'),
    path('api/v3/districts/<int:district_id>/delete/', district_delete, name='ubigeo_district_delete'),
    path('api/v3/provinces/<int:province_id>/districts/', districts, name='ubigeo_districts_by_province'),

    # Países
    path('api/v3/countries/', countries, name='ubigeo_countries'),
    path('api/v3/countries/create/', country_create, name='ubigeo_country_create'),
    path('api/v3/countries/<int:country_id>/update/', country_update, name='ubigeo_country_update'),
    path('api/v3/countries/<int:country_id>/delete/', country_delete, name='ubigeo_country_delete'),

    # Direcciones (comentado temporalmente)
    # path('api/v3/addresses/', addresses, name='ubigeo_addresses'),
    # path('api/v3/addresses/create/', address_create, name='ubigeo_address_create'),
    # path('api/v3/addresses/<int:address_id>/', address_detail, name='ubigeo_address_detail'),
    # path('api/v3/addresses/<int:address_id>/update/', address_update, name='ubigeo_address_update'),
    # path('api/v3/addresses/<int:address_id>/delete/', address_delete, name='ubigeo_address_delete'),
    # path('api/v3/addresses/<int:address_id>/restore/', address_restore, name='ubigeo_address_restore'),
    # path('api/v3/countries/<int:country_id>/addresses/', addresses_by_country, name='ubigeo_addresses_by_country'),
    # path('api/v3/regions/<int:region_id>/addresses/', addresses_by_region, name='ubigeo_addresses_by_region'),
    # path('api/v3/provinces/<int:province_id>/addresses/', addresses_by_province, name='ubigeo_addresses_by_province'),
    # path('api/v3/districts/<int:district_id>/addresses/', addresses_by_district, name='ubigeo_addresses_by_district'),
    # path('api/v3/addresses/search/', search_addresses, name='ubigeo_addresses_search'),
    # path('api/v3/addresses/ubigeo/', addresses_by_ubigeo, name='ubigeo_addresses_by_ubigeo'),
]
