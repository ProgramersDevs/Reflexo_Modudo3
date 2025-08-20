from django.db.models import Q
from django.core.paginator import Paginator
from ..models.diagnosis import Diagnosis
from ..serializers.diagnosis import DiagnosisSerializer, DiagnosisListSerializer

class DiagnosisService:
    """Servicio para gestionar diagnósticos."""
    
    @staticmethod
    def get_all_diagnoses(page=1, page_size=10, search=None):
        """Obtiene todos los diagnósticos con paginación y búsqueda."""
        queryset = Diagnosis.objects.filter(deleted_at__isnull=True)
        
        # Aplicar búsqueda
        if search:
            queryset = queryset.filter(
                Q(code__icontains=search) |
                Q(name__icontains=search) |
                Q(description__icontains=search)
            )
        
        # Ordenar por código
        queryset = queryset.order_by('code')
        
        # Paginación
        paginator = Paginator(queryset, page_size)
        diagnoses_page = paginator.get_page(page)
        
        # Serializar
        diagnoses_data = DiagnosisListSerializer(diagnoses_page, many=True).data
        
        return {
            'diagnoses': diagnoses_data,
            'total': paginator.count,
            'total_pages': paginator.num_pages,
            'current_page': page,
            'has_next': diagnoses_page.has_next(),
            'has_previous': diagnoses_page.has_previous()
        }
    
    @staticmethod
    def get_diagnosis_by_id(diagnosis_id):
        """Obtiene un diagnóstico por su ID."""
        try:
            diagnosis = Diagnosis.objects.get(id=diagnosis_id, deleted_at__isnull=True)
            return DiagnosisSerializer(diagnosis).data
        except Diagnosis.DoesNotExist:
            return None
    
    @staticmethod
    def create_diagnosis(diagnosis_data):
        """Crea un nuevo diagnóstico."""
        serializer = DiagnosisSerializer(data=diagnosis_data)
        if serializer.is_valid():
            diagnosis = serializer.save()
            return DiagnosisSerializer(diagnosis).data, None
        return None, serializer.errors
    
    @staticmethod
    def update_diagnosis(diagnosis_id, diagnosis_data):
        """Actualiza un diagnóstico existente."""
        try:
            diagnosis = Diagnosis.objects.get(id=diagnosis_id, deleted_at__isnull=True)
            serializer = DiagnosisSerializer(diagnosis, data=diagnosis_data, partial=True)
            if serializer.is_valid():
                diagnosis = serializer.save()
                return DiagnosisSerializer(diagnosis).data, None
            return None, serializer.errors
        except Diagnosis.DoesNotExist:
            return None, {'error': 'Diagnóstico no encontrado'}
    
    @staticmethod
    def delete_diagnosis(diagnosis_id):
        """Elimina un diagnóstico (soft delete)."""
        try:
            diagnosis = Diagnosis.objects.get(id=diagnosis_id, deleted_at__isnull=True)
            diagnosis.soft_delete()
            return True
        except Diagnosis.DoesNotExist:
            return False
    
    @staticmethod
    def restore_diagnosis(diagnosis_id):
        """Restaura un diagnóstico eliminado."""
        try:
            diagnosis = Diagnosis.objects.get(id=diagnosis_id, deleted_at__isnull=False)
            diagnosis.restore()
            return True
        except Diagnosis.DoesNotExist:
            return False
    
    @staticmethod
    def get_diagnosis_by_code(code):
        """Obtiene un diagnóstico por su código."""
        try:
            diagnosis = Diagnosis.objects.get(code=code, deleted_at__isnull=True)
            return DiagnosisSerializer(diagnosis).data
        except Diagnosis.DoesNotExist:
            return None
