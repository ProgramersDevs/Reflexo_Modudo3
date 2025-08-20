from rest_framework import generics, status
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.decorators import api_view
from ..models.diagnosis import Diagnosis 
from ..serializers.diagnosis import DiagnosisSerializer, DiagnosisListSerializer
from django.db.models import Q
from rest_framework.views import APIView
from ..services.diagnosis_service import DiagnosisService


diagnosis_service = DiagnosisService()

class DiagnosisListCreateAPIView(generics.ListCreateAPIView):
    queryset = Diagnosis.objects.filter(deleted_at__isnull=True)
    serializer_class = DiagnosisSerializer
    
    def list(self, request, *args, **kwargs):
        # Parámetros de paginación
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('page_size', 10))
        search = request.GET.get('search', '')
        
        # Usar el servicio
        result = diagnosis_service.get_all_diagnoses(page, page_size, search)
        
        return Response({
            "count": result['total'],
            "num_pages": result['total_pages'],
            "current_page": result['current_page'],
            "results": result['diagnoses'],
        })
    
    def create(self, request, *args, **kwargs):
        diagnosis_data, errors = diagnosis_service.create_diagnosis(request.data)
        
        if diagnosis_data:
            return Response(diagnosis_data, status=status.HTTP_201_CREATED)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

class DiagnosisRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diagnosis.objects.filter(deleted_at__isnull=True)
    serializer_class = DiagnosisSerializer

    def retrieve(self, request, *args, **kwargs):
        diagnosis_data = diagnosis_service.get_diagnosis_by_id(kwargs['pk'])
        
        if diagnosis_data:
            return Response(diagnosis_data)
        else:
            return Response({'error': 'Diagnóstico no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, *args, **kwargs):
        diagnosis_data, errors = diagnosis_service.update_diagnosis(kwargs['pk'], request.data)
        
        if diagnosis_data:
            return Response(diagnosis_data)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        success = diagnosis_service.delete_diagnosis(kwargs['pk'])
        
        if success:
            return Response({'detail': 'Diagnóstico eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Diagnóstico no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    
class DiagnosisSearchAPIView(APIView):
    def get(self, request):
        query = request.GET.get('q', '').strip()
        if not query:
            return Response({"detail": "Se requiere un parámetro de búsqueda."}, status=status.HTTP_400_BAD_REQUEST)

        diagnoses = Diagnosis.objects.filter(
            Q(name__icontains=query) | Q(code__icontains=query),
            deleted_at__isnull=True
        )

        serializer = DiagnosisSerializer(diagnoses, many=True)
        return Response(serializer.data)


