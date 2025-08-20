from django.test import TestCase, Client
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
import json
from ..models.country import Country
from ..models.region import Region
from ..models.province import Province
from ..models.district import District


class CountryViewsTest(TestCase):
    """Tests para las vistas de Country"""
    
    def setUp(self):
        self.client = Client()
        self.country = Country.objects.create(
            name='Perú',
            ubigeo_code='PE'
        )
    
    def test_countries_list_view(self):
        """Test de vista de listado de países"""
        response = self.client.get('/api/countries/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['data']), 1)
    
    def test_country_detail_view(self):
        """Test de vista de detalle de país"""
        response = self.client.get(f'/api/v3/countries/{self.country.id}/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['data']['name'], 'Perú')
    
    def test_country_create_view(self):
        """Test de vista de creación de país"""
        data = {
            'name': 'Chile',
            'ubigeo_code': 'CL'
        }
        response = self.client.post(
            '/api/v3/countries/create/',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])
        self.assertEqual(response_data['data']['name'], 'Chile')
    
    def test_country_update_view(self):
        """Test de vista de actualización de país"""
        data = {'name': 'Perú Actualizado'}
        response = self.client.put(
            f'/api/v3/countries/{self.country.id}/update/',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])
        self.assertEqual(response_data['data']['name'], 'Perú Actualizado')
    
    def test_country_delete_view(self):
        """Test de vista de eliminación de país"""
        response = self.client.delete(f'/api/v3/countries/{self.country.id}/delete/')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])
        with self.assertRaises(ObjectDoesNotExist):
            Country.objects.get(id=self.country.id)


class RegionViewsTest(TestCase):
    """Tests para las vistas de Region"""
    
    def setUp(self):
        self.client = Client()
        self.region = Region.objects.create(
            name='Lima',
            ubigeo_code='15'
        )
    
    def test_regions_list_view(self):
        """Test de vista de listado de regiones"""
        response = self.client.get('/api/regions/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['data']), 1)
    
    def test_region_detail_view(self):
        """Test de vista de detalle de región"""
        response = self.client.get(f'/api/v3/regions/{self.region.id}/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['data']['name'], 'Lima')
    
    def test_region_create_view(self):
        """Test de vista de creación de región"""
        data = {
            'name': 'Arequipa',
            'ubigeo_code': '04'
        }
        response = self.client.post(
            '/api/v3/regions/create/',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])
        self.assertEqual(response_data['data']['name'], 'Arequipa')
    
    def test_region_delete_view(self):
        """Test de vista de eliminación de región (soft delete)"""
        response = self.client.delete(f'/api/v3/regions/{self.region.id}/delete/')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])
        # La región debe seguir existiendo pero con deleted_at
        region = Region.objects.get(id=self.region.id)
        self.assertIsNotNone(region.deleted_at)


class ProvinceViewsTest(TestCase):
    """Tests para las vistas de Province"""
    
    def setUp(self):
        self.client = Client()
        self.region = Region.objects.create(
            name='Lima',
            ubigeo_code='15'
        )
        self.province = Province.objects.create(
            name='Lima',
            region=self.region,
            ubigeo_code='1501'
        )
    
    def test_provinces_list_view(self):
        """Test de vista de listado de provincias"""
        response = self.client.get('/api/provinces/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['data']), 1)
    
    def test_province_detail_view(self):
        """Test de vista de detalle de provincia"""
        response = self.client.get(f'/api/v3/provinces/{self.province.id}/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['data']['name'], 'Lima')
    
    def test_province_create_view(self):
        """Test de vista de creación de provincia"""
        data = {
            'name': 'Callao',
            'region': self.region.id,
            'ubigeo_code': '1502'
        }
        response = self.client.post(
            '/api/v3/provinces/create/',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])
        self.assertEqual(response_data['data']['name'], 'Callao')
    
    def test_provinces_by_region_view(self):
        """Test de vista de provincias por región"""
        response = self.client.get(f'/api/v3/regions/{self.region.id}/provinces/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['data']), 1)


class DistrictViewsTest(TestCase):
    """Tests para las vistas de District"""
    
    def setUp(self):
        self.client = Client()
        self.region = Region.objects.create(
            name='Lima',
            ubigeo_code='15'
        )
        self.province = Province.objects.create(
            name='Lima',
            region=self.region,
            ubigeo_code='1501'
        )
        self.district = District.objects.create(
            name='Lima',
            province=self.province,
            ubigeo_code='150101'
        )
    
    def test_districts_list_view(self):
        """Test de vista de listado de distritos"""
        response = self.client.get('/api/districts/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['data']), 1)
    
    def test_district_detail_view(self):
        """Test de vista de detalle de distrito"""
        response = self.client.get(f'/api/v3/districts/{self.district.id}/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['data']['name'], 'Lima')
    
    def test_district_create_view(self):
        """Test de vista de creación de distrito"""
        data = {
            'name': 'Miraflores',
            'province': self.province.id,
            'ubigeo_code': '150102'
        }
        response = self.client.post(
            '/api/v3/districts/create/',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])
        self.assertEqual(response_data['data']['name'], 'Miraflores')
    
    def test_districts_by_province_view(self):
        """Test de vista de distritos por provincia"""
        response = self.client.get(f'/api/v3/provinces/{self.province.id}/districts/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['data']), 1)





class WebViewsTest(TestCase):
    """Tests para las vistas web"""
    
    def setUp(self):
        self.client = Client()
    
    def test_home_view(self):
        """Test de vista de inicio"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_debug_view(self):
        """Test de vista de debug"""
        response = self.client.get('/debug/')
        self.assertEqual(response.status_code, 200)
    
    def test_countries_view(self):
        """Test de vista de países"""
        response = self.client.get('/countries/')
        self.assertEqual(response.status_code, 200)
    
    def test_regions_view(self):
        """Test de vista de regiones"""
        response = self.client.get('/regions/')
        self.assertEqual(response.status_code, 200)
    
    def test_provinces_view(self):
        """Test de vista de provincias"""
        response = self.client.get('/provinces/')
        self.assertEqual(response.status_code, 200)
    
    def test_districts_view(self):
        """Test de vista de distritos"""
        response = self.client.get('/districts/')
        self.assertEqual(response.status_code, 200)
