from django.contrib import admin
from .models.patient import Patient
from .models.diagnosis import Diagnosis
from .models.medical_record import MedicalRecord

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_number', 'name', 'paternal_lastname', 'maternal_lastname', 'primary_phone', 'email')
    search_fields = ('id', 'document_number', 'name', 'paternal_lastname', 'maternal_lastname', 'personal_reference')
    list_filter = ('sex', 'region', 'province', 'district', 'country', 'document_type')



@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description')
    search_fields = ('code', 'name', 'description')
    ordering = ('code',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'diagnosis', 'diagnosis_date', 'status', 'created_at')
    list_filter = ('status', 'diagnosis_date', 'created_at')
    search_fields = ('patient__name', 'patient__document_number', 'diagnosis__name', 'diagnosis__code')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-diagnosis_date', '-created_at')
    
    fieldsets = (
        ('Información del Paciente', {
            'fields': ('patient',)
        }),
        ('Información del Diagnóstico', {
            'fields': ('diagnosis', 'diagnosis_date', 'status')
        }),
        ('Detalles Médicos', {
            'fields': ('symptoms', 'treatment', 'notes')
        }),
        ('Auditoría', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('patient', 'diagnosis')