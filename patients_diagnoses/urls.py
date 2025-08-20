from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.diagnosis import ( DiagnosisListCreateAPIView, DiagnosisRetrieveUpdateDestroyAPIView, DiagnosisSearchAPIView )
from .views.patient import ( PatientListCreateView, PatientRetrieveUpdateDeleteView, PatientSearchView )
from .views.medical_record import ( MedicalRecordListCreateAPIView, MedicalRecordRetrieveUpdateDestroyAPIView, PatientMedicalHistoryAPIView, DiagnosisStatisticsAPIView )
router = DefaultRouter()
router.register(r'patients',PatientListCreateView, basename='patient')
urlpatterns = [
     # URLs de diagnósticos
     path('diagnoses/', DiagnosisListCreateAPIView.as_view(), name='diagnosis-list-create'), 
     path('diagnoses/<int:pk>/', DiagnosisRetrieveUpdateDestroyAPIView.as_view(), name='diagnosis-detail'), 
     path('diagnoses/search/', DiagnosisSearchAPIView.as_view(), name='diagnosis-search'),
     
     # URLs de pacientes
     path('patients/', PatientListCreateView.as_view(), name='patient-list'),
     path('patients/search/', PatientSearchView.as_view(), name='patient-search'),
     path('patients/<int:pk>/', PatientRetrieveUpdateDeleteView.as_view(), name='patient-detail'),
     
     # URLs de historiales médicos
     path('medical-records/', MedicalRecordListCreateAPIView.as_view(), name='medical-record-list-create'),
     path('medical-records/<int:pk>/', MedicalRecordRetrieveUpdateDestroyAPIView.as_view(), name='medical-record-detail'),
     path('patients/<int:patient_id>/medical-history/', PatientMedicalHistoryAPIView.as_view(), name='patient-medical-history'),
     path('diagnosis-statistics/', DiagnosisStatisticsAPIView.as_view(), name='diagnosis-statistics'),
]


