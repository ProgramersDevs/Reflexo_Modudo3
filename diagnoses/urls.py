from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  DiagnosisListCreateAPIView, DiagnosisRetrieveUpdateDestroyAPIView,DiagnosisSearchAPIView


urlpatterns = [
     path('', DiagnosisListCreateAPIView.as_view(), name='diagnosis-list-create'),
     path('<int:pk>/', DiagnosisRetrieveUpdateDestroyAPIView.as_view(), name='diagnosis-detail'),
     path('search/', DiagnosisSearchAPIView.as_view(), name='diagnosis-search'),
]