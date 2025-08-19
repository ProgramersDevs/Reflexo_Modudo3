from django.contrib import admin
from .models.patient import Patient, Region, Province, District, Country, DocumentType
from .models.diagnosis import Diagnosis

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_number', 'name', 'paternal_lastname', 'maternal_lastname', 'primary_phone', 'email')
    search_fields = ('id', 'document_number', 'name', 'paternal_lastname', 'maternal_lastname', 'personal_reference')
    list_filter = ('sex', 'region', 'province', 'district', 'country', 'document_type')

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region')
    search_fields = ('name',)

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'province')
    search_fields = ('name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'deleted_at')
    search_fields = ('code', 'name')
    list_filter = ('deleted_at',)