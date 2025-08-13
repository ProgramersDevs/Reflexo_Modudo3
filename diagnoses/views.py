from rest_framework import generics, status
from rest_framework.response import Response
from django.utils import timezone
from .models import Diagnosis
from .serializers import DiagnosisSerializer
from django.db.models import Q
from rest_framework.views import APIView


class DiagnosisListCreateAPIView(generics.ListCreateAPIView):
    queryset = Diagnosis.objects.filter(deleted_at__isnull=True)
    serializer_class = DiagnosisSerializer

class DiagnosisRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diagnosis.objects.filter(deleted_at__isnull=True)
    serializer_class = DiagnosisSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_at = timezone.now()
        instance.save()
        return Response({'detail': 'Diagnóstico eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
    
    
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