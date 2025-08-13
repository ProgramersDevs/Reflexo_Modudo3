from django.urls import path
from . import views
from .views import PatientListCreateView,PatientRetrieveUpdateDeleteView,PatientSearchView


urlpatterns = [
    path('patients/', PatientListCreateView.as_view(), name='patient-list'),
    path('patients/search/', PatientSearchView.as_view(), name='patient-search'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDeleteView.as_view(), name='patient-detail'),
]
