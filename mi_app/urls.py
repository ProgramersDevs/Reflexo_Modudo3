from django.urls import path
from .views import document_type, history, payment_type, predetermined_price
from .views.history import histories_list, history_create, history_delete

urlpatterns = [
    path('document-types/', document_type.document_types_list, name='document_types_list'),
    path('document-types/new/', document_type.document_type_create, name='document_type_create'),
    path('document-types/<int:pk>/delete/', document_type.document_type_delete, name='document_type_delete'),

    path('histories/', histories_list, name='histories_list'),         
    path('histories/new/', history_create, name='history_create'),      
    path('histories/<int:pk>/delete/', history_delete, name='history_delete'),


    path('payment-types/', payment_type.payment_types_list, name='payment_types_list'),
    path('payment-types/new/', payment_type.payment_type_create, name='payment_type_create'),
    path('payment-types/<int:pk>/delete/', payment_type.payment_type_delete, name='payment_type_delete'),

    path('predetermined-prices/', predetermined_price.predetermined_prices_list, name='predetermined_prices_list'),
    path('predetermined-prices/new/', predetermined_price.predetermined_price_create, name='predetermined_price_create'),
]
