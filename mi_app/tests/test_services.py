from django.test import TestCase
from mi_app.models import DocumentType, History, PaymentType
from mi_app.services import document_type_service, history_service, payment_type_service

class ServicesTest(TestCase):
    def test_document_type_service(self):
        document_type_service.create(name="DNI")
        self.assertEqual(document_type_service.list_active().count(), 1)

    def test_history_service(self):
        dt = DocumentType.objects.create(name="DNI")
        h = history_service.create(document_type=dt, document_number="123")
        self.assertEqual(history_service.list_active().count(), 1)
        history_service.soft_delete(h)
        self.assertEqual(history_service.list_active().count(), 0)

    def test_payment_type_service(self):
        payment_type_service.create(code="EF", name="Efectivo")
        self.assertEqual(payment_type_service.list_active().count(), 1)
