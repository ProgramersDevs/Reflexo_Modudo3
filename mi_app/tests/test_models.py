from django.test import TestCase
from mi_app.models import DocumentType, PaymentType, PredeterminedPrice, History

class ModelsTest(TestCase):
    def test_document_type_create(self):
        dt = DocumentType.objects.create(name="DNI", description="Documento Nacional")
        self.assertIsNotNone(dt.pk)

    def test_payment_type_create(self):
        pt = PaymentType.objects.create(code="EF", name="Efectivo")
        self.assertIsNotNone(pt.pk)

    def test_predetermined_price_create(self):
        pp = PredeterminedPrice.objects.create(name="Consulta", price=50.00)
        self.assertIsNotNone(pp.pk)

    def test_history_unique_active_by_document(self):
        dt = DocumentType.objects.create(name="DNI")
        History.objects.create(document_type=dt, document_number="12345678")
        # segundo activo idéntico debe violar la unicidad al guardar; probamos vía try/except
        with self.assertRaises(Exception):
            History.objects.create(document_type=dt, document_number="12345678")
