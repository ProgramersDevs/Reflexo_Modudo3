from django.db.models import Q
from django.core.paginator import Paginator
from ..models.medical_record import MedicalRecord
from ..serializers.medical_record import MedicalRecordSerializer, MedicalRecordListSerializer

class MedicalRecordService:
    """Servicio para gestionar historiales médicos."""
    
    @staticmethod
    def get_all_medical_records(page=1, page_size=10, search=None, filters=None):
        """Obtiene todos los historiales médicos con paginación y filtros."""
        queryset = MedicalRecord.objects.filter(deleted_at__isnull=True)
        
        # Aplicar búsqueda
        if search:
            queryset = queryset.filter(
                Q(patient__name__icontains=search) |
                Q(patient__paternal_lastname__icontains=search) |
                Q(patient__document_number__icontains=search) |
                Q(diagnosis__name__icontains=search) |
                Q(diagnosis__code__icontains=search) |
                Q(symptoms__icontains=search) |
                Q(treatment__icontains=search)
            )
        
        # Aplicar filtros
        if filters:
            if filters.get('patient_id'):
                queryset = queryset.filter(patient_id=filters['patient_id'])
            if filters.get('diagnosis_id'):
                queryset = queryset.filter(diagnosis_id=filters['diagnosis_id'])
            if filters.get('status'):
                queryset = queryset.filter(status=filters['status'])
            if filters.get('date_from'):
                queryset = queryset.filter(diagnosis_date__gte=filters['date_from'])
            if filters.get('date_to'):
                queryset = queryset.filter(diagnosis_date__lte=filters['date_to'])
        
        # Ordenar por fecha de diagnóstico
        queryset = queryset.order_by('-diagnosis_date', '-created_at')
        
        # Paginación
        paginator = Paginator(queryset, page_size)
        records_page = paginator.get_page(page)
        
        # Serializar
        records_data = MedicalRecordListSerializer(records_page, many=True).data
        
        return {
            'medical_records': records_data,
            'total': paginator.count,
            'total_pages': paginator.num_pages,
            'current_page': page,
            'has_next': records_page.has_next(),
            'has_previous': records_page.has_previous()
        }
    
    @staticmethod
    def get_medical_record_by_id(record_id):
        """Obtiene un historial médico por su ID."""
        try:
            record = MedicalRecord.objects.get(id=record_id, deleted_at__isnull=True)
            return MedicalRecordSerializer(record).data
        except MedicalRecord.DoesNotExist:
            return None
    
    @staticmethod
    def create_medical_record(record_data):
        """Crea un nuevo historial médico."""
        serializer = MedicalRecordSerializer(data=record_data)
        if serializer.is_valid():
            record = serializer.save()
            return MedicalRecordSerializer(record).data
        return None, serializer.errors
    
    @staticmethod
    def update_medical_record(record_id, record_data):
        """Actualiza un historial médico existente."""
        try:
            record = MedicalRecord.objects.get(id=record_id, deleted_at__isnull=True)
            serializer = MedicalRecordSerializer(record, data=record_data, partial=True)
            if serializer.is_valid():
                record = serializer.save()
                return MedicalRecordSerializer(record).data
            return None, serializer.errors
        except MedicalRecord.DoesNotExist:
            return None, {'error': 'Historial médico no encontrado'}
    
    @staticmethod
    def delete_medical_record(record_id):
        """Elimina un historial médico (soft delete)."""
        try:
            record = MedicalRecord.objects.get(id=record_id, deleted_at__isnull=True)
            record.soft_delete()
            return True
        except MedicalRecord.DoesNotExist:
            return False
    
    @staticmethod
    def restore_medical_record(record_id):
        """Restaura un historial médico eliminado."""
        try:
            record = MedicalRecord.objects.get(id=record_id, deleted_at__isnull=False)
            record.restore()
            return True
        except MedicalRecord.DoesNotExist:
            return False
    
    @staticmethod
    def get_patient_medical_history(patient_id, page=1, page_size=10):
        """Obtiene el historial médico de un paciente específico."""
        queryset = MedicalRecord.objects.filter(
            patient_id=patient_id,
            deleted_at__isnull=True
        ).order_by('-diagnosis_date', '-created_at')
        
        # Paginación
        paginator = Paginator(queryset, page_size)
        records_page = paginator.get_page(page)
        
        # Serializar
        records_data = MedicalRecordListSerializer(records_page, many=True).data
        
        return {
            'medical_records': records_data,
            'total': paginator.count,
            'total_pages': paginator.num_pages,
            'current_page': page,
            'has_next': records_page.has_next(),
            'has_previous': records_page.has_previous()
        }
    
    @staticmethod
    def get_diagnosis_statistics():
        """Obtiene estadísticas de diagnósticos."""
        from django.db.models import Count
        
        stats = MedicalRecord.objects.filter(
            deleted_at__isnull=True
        ).values('diagnosis__name').annotate(
            count=Count('id')
        ).order_by('-count')[:10]
        
        return stats
