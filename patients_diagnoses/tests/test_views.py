from django.test import TestCase
# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models.diagnosis import Diagnosis
# Create your test here
from ..models.patient import Patient, Region, Province, District, Country, DocumentType
from datetime import date
class DiagnosisTests(APITestCase):
    def setUp(self):
        self.diagnosis = Diagnosis.objects.create(code='D001', name='Dolor de cabeza')

    def test_list_diagnoses(self):
        url = reverse('diagnosis-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_diagnosis(self):
        url = reverse('diagnosis-list-create')
        data = {'code': 'D002', 'name': 'Fiebre'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'D002')

    def test_get_diagnosis_detail(self):
        url = reverse('diagnosis-detail', args=[self.diagnosis.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], self.diagnosis.code)

    def test_update_diagnosis(self):
        url = reverse('diagnosis-detail', args=[self.diagnosis.pk])
        data = {'code': 'D001', 'name': 'Cefalea aguda'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Cefalea aguda')

    def test_soft_delete_diagnosis(self):
        url = reverse('diagnosis-detail', args=[self.diagnosis.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.diagnosis.refresh_from_db()
        self.assertIsNotNone(self.diagnosis.deleted_at)

    def test_search_diagnosis(self):
        url = reverse('diagnosis-search')
        response = self.client.get(url, {'q': 'D001'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

class PatientTests(APITestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Perú")
        self.region = Region.objects.create(name="Lima", country=self.country)
        self.province = Province.objects.create(name="Lima", region=self.region)
        self.district = District.objects.create(name="Miraflores", province=self.province)
        self.document_type = DocumentType.objects.create(name="DNI")

        self.patient_data = {
            "document_number": "12345678",
            "paternal_lastname": "Gonzales",
            "maternal_lastname": "Perez",
            "name": "Luis",
            "birth_date": "2000-01-01",
            "sex": "Masculino",
            "primary_phone": "987654321",
            "email": "luis@example.com",
            "address": "Calle Falsa 123",
            "region_id": self.region.id,
            "province_id": self.province.id,
            "district_id": self.district.id,
            "country_id": self.country.id,
            "document_type_id": self.document_type.id
        }

        self.patient = Patient.objects.create(
            document_number="87654321",
            paternal_lastname="Ramirez",
            maternal_lastname="Lopez",
            name="Ana",
            birth_date=date(1990, 5, 10),
            sex="Femenino",
            primary_phone="912345678",
            email="ana@example.com",
            address="Av. Siempreviva 742",
            region=self.region,
            province=self.province,
            district=self.district,
            country=self.country,
            document_type=self.document_type
        )
    def test_list_patients(self):
        url = reverse('patient-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_patient(self):
        url = reverse('patient-list')
        response = self.client.post(url, self.patient_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "Luis")

    def test_get_patient_detail(self):
        url = reverse('patient-detail', args=[self.patient.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.patient.name)

    def test_update_patient(self):
        url = reverse('patient-detail', args=[self.patient.id])
        self.patient_data["name"] = "Ana Maria"
        response = self.client.put(url, self.patient_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Ana Maria")

    def test_delete_patient(self):
        url = reverse('patient-detail', args=[self.patient.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_search_patient(self):
        url = reverse('patient-search')
        response = self.client.get(url, {'q': 'Ana'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)