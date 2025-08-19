from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.diagnosis import ( DiagnosisListCreateAPIView, DiagnosisRetrieveUpdateDestroyAPIView, DiagnosisSearchAPIView )
from . import views
from .views.patient import ( PatientListCreateView, PatientRetrieveUpdateDeleteView, PatientSearchView )

urlpatterns = [
     path('diagnoses/', DiagnosisListCreateAPIView.as_view(), name='diagnosis-list-create'), 
     path('diagnoses/int:pk/', DiagnosisRetrieveUpdateDestroyAPIView.as_view(), name='diagnosis-detail'), 
     path('diagnoses/search/', DiagnosisSearchAPIView.as_view(), name='diagnosis-search'),
     
     path('patients/', PatientListCreateView.as_view(), name='patient-list'),
     path('patients/search/', PatientSearchView.as_view(), name='patient-search'),
     path('patients/<int:pk>/', PatientRetrieveUpdateDeleteView.as_view(), name='patient-detail'),
]


