from django.contrib import admin
from .models.country import Country
from .models.region import Region
from .models.province import Province
from .models.district import District


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'ubigeo_code', 'deleted_at', 'created_at', 'updated_at')
    list_filter = ('deleted_at', 'created_at', 'updated_at')
    search_fields = ('name', 'ubigeo_code')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    
    def get_queryset(self, request):
        """Mostrar solo países no eliminados por defecto"""
        return super().get_queryset(request).filter(deleted_at__isnull=True)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'ubigeo_code', 'deleted_at', 'created_at', 'updated_at')
    list_filter = ('deleted_at', 'created_at', 'updated_at')
    search_fields = ('name', 'ubigeo_code')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    
    def get_queryset(self, request):
        """Mostrar solo regiones no eliminadas por defecto"""
        return super().get_queryset(request).filter(deleted_at__isnull=True)


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'ubigeo_code', 'deleted_at', 'created_at', 'updated_at')
    list_filter = ('region', 'deleted_at', 'created_at', 'updated_at')
    search_fields = ('name', 'ubigeo_code', 'region__name')
    ordering = ('region__name', 'name')
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ('region',)
    
    def get_queryset(self, request):
        """Mostrar solo provincias no eliminadas por defecto"""
        return super().get_queryset(request).filter(deleted_at__isnull=True)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'ubigeo_code', 'deleted_at', 'created_at', 'updated_at')
    list_filter = ('province__region', 'province', 'deleted_at', 'created_at', 'updated_at')
    search_fields = ('name', 'ubigeo_code', 'province__name', 'province__region__name')
    ordering = ('province__region__name', 'province__name', 'name')
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ('province',)
    
    def get_queryset(self, request):
        """Mostrar solo distritos no eliminados por defecto"""
        return super().get_queryset(request).filter(deleted_at__isnull=True)#
