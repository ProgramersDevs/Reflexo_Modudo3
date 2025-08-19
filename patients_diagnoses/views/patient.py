from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.generics import ListAPIView
import unicodedata

# ✅ Paso 1 y 2: función para eliminar tildes
def remove_accents(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )

class PatientListCreateView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PatientSearchView(APIView):
    def get(self, request):
        query = request.GET.get('q', '').lower()
        query_normalized = remove_accents(query)

        patients = Patient.objects.all()
        filtered = []

        for patient in patients:
            combined_fields = (
                 f"{patient.name} {patient.paternal_lastname} {patient.maternal_lastname} "
                 f"{patient.document_number} {patient.personal_reference or ''}"
            ).lower()

            combined_fields_normalized = remove_accents(combined_fields)

            if query_normalized in combined_fields_normalized:
                filtered.append(patient)

        serializer = PatientSerializer(filtered, many=True)
        return Response(serializer.data)


# Create your views here.