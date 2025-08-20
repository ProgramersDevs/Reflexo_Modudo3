from rest_framework import generics, status
from rest_framework.response import Response
from django.utils import timezone
from ..models.medical_record import MedicalRecord 
from ..serializers.medical_record import MedicalRecordSerializer, MedicalRecordListSerializer
from ..services.medical_record_service import MedicalRecordService

medical_record_service = MedicalRecordService()

class MedicalRecordListCreateAPIView(generics.ListCreateAPIView):
    queryset = MedicalRecord.objects.filter(deleted_at__isnull=True)
    serializer_class = MedicalRecordSerializer
    
    def list(self, request, *args, **kwargs):
        # Parámetros de paginación
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('page_size', 10))
        search = request.GET.get('search', '')
        
        # Filtros
        filters = {}
        if request.GET.get('patient_id'):
            filters['patient_id'] = request.GET.get('patient_id')
        if request.GET.get('diagnosis_id'):
            filters['diagnosis_id'] = request.GET.get('diagnosis_id')
        if request.GET.get('status'):
            filters['status'] = request.GET.get('status')
        if request.GET.get('date_from'):
            filters['date_from'] = request.GET.get('date_from')
        if request.GET.get('date_to'):
            filters['date_to'] = request.GET.get('date_to')
        
        # Usar el servicio
        result = medical_record_service.get_all_medical_records(page, page_size, search, filters)
        
        return Response({
            "count": result['total'],
            "num_pages": result['total_pages'],
            "current_page": result['current_page'],
            "results": result['medical_records'],
        })
    
    def create(self, request, *args, **kwargs):
        record_data, errors = medical_record_service.create_medical_record(request.data)
        
        if record_data:
            return Response(record_data, status=status.HTTP_201_CREATED)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

class MedicalRecordRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecord.objects.filter(deleted_at__isnull=True)
    serializer_class = MedicalRecordSerializer

    def retrieve(self, request, *args, **kwargs):
        record_data = medical_record_service.get_medical_record_by_id(kwargs['pk'])
        
        if record_data:
            return Response(record_data)
        else:
            return Response({'error': 'Historial médico no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, *args, **kwargs):
        record_data, errors = medical_record_service.update_medical_record(kwargs['pk'], request.data)
        
        if record_data:
            return Response(record_data)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        success = medical_record_service.delete_medical_record(kwargs['pk'])
        
        if success:
            return Response({'detail': 'Historial médico eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Historial médico no encontrado'}, status=status.HTTP_404_NOT_FOUND)

class PatientMedicalHistoryAPIView(generics.ListAPIView):
    """Obtiene el historial médico de un paciente específico."""
    
    def get(self, request, patient_id):
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('page_size', 10))
        
        result = medical_record_service.get_patient_medical_history(patient_id, page, page_size)
        
        return Response({
            "count": result['total'],
            "num_pages": result['total_pages'],
            "current_page": result['current_page'],
            "results": result['medical_records'],
        })

class DiagnosisStatisticsAPIView(generics.ListAPIView):
    """Obtiene estadísticas de diagnósticos."""
    
    def get(self, request):
        stats = medical_record_service.get_diagnosis_statistics()
        return Response(stats)
