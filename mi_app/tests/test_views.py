from django.test import TestCase
from django.urls import reverse
from mi_app.models import DocumentType

class ViewsTest(TestCase):
    def test_document_types_list(self):
        DocumentType.objects.create(name="DNI")
        response = self.client.get(reverse('document_types_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('document_types', response.json())
