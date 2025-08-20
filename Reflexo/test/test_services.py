from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from ..services.country_service import CountryService
from ..services.region_service import RegionService
from ..services.province_service import ProvinceService
from ..services.district_service import DistrictService
from ..models.country import Country
from ..models.region import Region
from ..models.province import Province
from ..models.district import District


class CountryServiceTest(TestCase):
    """Tests para CountryService"""
    
    def setUp(self):
        self.country_data = {
            'name': 'Perú',
            'ubigeo_code': 'PE'
        }
        self.country = Country.objects.create(**self.country_data)
    
    def test_get_all_countries(self):
        """Test de obtener todos los países"""
        countries = CountryService.get_all_countries()
        self.assertEqual(len(countries), 1)
        self.assertEqual(countries[0].name, 'Perú')
    
    def test_get_country_by_id(self):
        """Test de obtener país por ID"""
        country = CountryService.get_country_by_id(self.country.id)
        self.assertEqual(country.name, 'Perú')
    
    def test_get_country_by_id_not_found(self):
        """Test de obtener país por ID inexistente"""
        with self.assertRaises(Exception):
            CountryService.get_country_by_id(999)
    
    def test_create_country(self):
        """Test de crear país"""
        data = {'name': 'Chile', 'ubigeo_code': 'CL'}
        country = CountryService.create_country(data)
        self.assertEqual(country.name, 'Chile')
        self.assertEqual(country.ubigeo_code, 'CL')
    
    def test_update_country(self):
        """Test de actualizar país"""
        data = {'name': 'Perú Actualizado'}
        country = CountryService.update_country(self.country.id, data)
        self.assertEqual(country.name, 'Perú Actualizado')
    
    def test_delete_country(self):
        """Test de eliminar país"""
        result = CountryService.delete_country(self.country.id)
        self.assertTrue(result)
        with self.assertRaises(ObjectDoesNotExist):
            Country.objects.get(id=self.country.id)
    
    def test_search_countries(self):
        """Test de búsqueda de países"""
        countries = CountryService.search_countries('Perú')
        self.assertEqual(len(countries), 1)
        self.assertEqual(countries[0].name, 'Perú')


class RegionServiceTest(TestCase):
    """Tests para RegionService"""
    
    def setUp(self):
        self.region_data = {
            'name': 'Lima',
            'ubigeo_code': '15'
        }
        self.region = Region.objects.create(**self.region_data)
    
    def test_get_all_regions(self):
        """Test de obtener todas las regiones"""
        regions = RegionService.get_all_regions()
        self.assertEqual(len(regions), 1)
        self.assertEqual(regions[0].name, 'Lima')
    
    def test_get_region_by_id(self):
        """Test de obtener región por ID"""
        region = RegionService.get_region_by_id(self.region.id)
        self.assertEqual(region.name, 'Lima')
    
    def test_create_region(self):
        """Test de crear región"""
        data = {'name': 'Arequipa', 'ubigeo_code': '04'}
        region = RegionService.create_region(data)
        self.assertEqual(region.name, 'Arequipa')
    
    def test_delete_region_soft_delete(self):
        """Test de soft delete de región"""
        result = RegionService.delete_region(self.region.id)
        self.assertTrue(result)
        # La región debe seguir existiendo pero con deleted_at
        region = Region.objects.get(id=self.region.id)
        self.assertIsNotNone(region.deleted_at)
    
    def test_restore_region(self):
        """Test de restaurar región"""
        self.region.delete()
        region = RegionService.restore_region(self.region.id)
        self.assertIsNone(region.deleted_at)


class ProvinceServiceTest(TestCase):
    """Tests para ProvinceService"""
    
    def setUp(self):
        self.region = Region.objects.create(
            name='Lima',
            ubigeo_code='15'
        )
        self.province_data = {
            'name': 'Lima',
            'region': self.region,
            'ubigeo_code': '1501'
        }
        self.province = Province.objects.create(**self.province_data)
    
    def test_get_all_provinces(self):
        """Test de obtener todas las provincias"""
        provinces = ProvinceService.get_all_provinces()
        self.assertEqual(len(provinces), 1)
        self.assertEqual(provinces[0].name, 'Lima')
    
    def test_get_provinces_by_region(self):
        """Test de obtener provincias por región"""
        provinces = ProvinceService.get_provinces_by_region(self.region.id)
        self.assertEqual(len(provinces), 1)
        self.assertEqual(provinces[0].name, 'Lima')
    
    def test_create_province(self):
        """Test de crear provincia"""
        data = {
            'name': 'Callao',
            'region_id': self.region.id,
            'ubigeo_code': '1502'
        }
        province = ProvinceService.create_province(data)
        self.assertEqual(province.name, 'Callao')
        self.assertEqual(province.region, self.region)
    
    def test_create_province_without_region(self):
        """Test de crear provincia sin región"""
        data = {'name': 'Callao', 'ubigeo_code': '1502'}
        with self.assertRaises(Exception):
            ProvinceService.create_province(data)


class DistrictServiceTest(TestCase):
    """Tests para DistrictService"""
    
    def setUp(self):
        self.region = Region.objects.create(
            name='Lima',
            ubigeo_code='15'
        )
        self.province = Province.objects.create(
            name='Lima',
            region=self.region,
            ubigeo_code='1501'
        )
        self.district_data = {
            'name': 'Lima',
            'province': self.province,
            'ubigeo_code': '150101'
        }
        self.district = District.objects.create(**self.district_data)
    
    def test_get_all_districts(self):
        """Test de obtener todos los distritos"""
        districts = DistrictService.get_all_districts()
        self.assertEqual(len(districts), 1)
        self.assertEqual(districts[0].name, 'Lima')
    
    def test_get_districts_by_province(self):
        """Test de obtener distritos por provincia"""
        districts = DistrictService.get_districts_by_province(self.province.id)
        self.assertEqual(len(districts), 1)
        self.assertEqual(districts[0].name, 'Lima')
    
    def test_create_district(self):
        """Test de crear distrito"""
        data = {
            'name': 'Miraflores',
            'province_id': self.province.id,
            'ubigeo_code': '150102'
        }
        district = DistrictService.create_district(data)
        self.assertEqual(district.name, 'Miraflores')
        self.assertEqual(district.province, self.province)
