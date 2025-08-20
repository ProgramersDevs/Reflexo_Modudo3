from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models.country import Country
from ..models.region import Region
from ..models.province import Province
from ..models.district import District


class CountryModelTest(TestCase):
    """Tests para el modelo Country"""
    
    def setUp(self):
        self.country = Country.objects.create(
            name="Perú",
            ubigeo_code="PE"
        )
    
    def test_country_creation(self):
        """Test de creación de país"""
        self.assertEqual(self.country.name, "Perú")
        self.assertEqual(self.country.ubigeo_code, "PE")
        self.assertIsNotNone(self.country.created_at)
        self.assertIsNotNone(self.country.updated_at)
    
    def test_country_str_representation(self):
        """Test de representación en string"""
        self.assertEqual(str(self.country), "Perú")
    
    def test_country_meta(self):
        """Test de configuración Meta"""
        self.assertEqual(Country._meta.verbose_name, "País")
        self.assertEqual(Country._meta.verbose_name_plural, "Países")


class RegionModelTest(TestCase):
    """Tests para el modelo Region"""
    
    def setUp(self):
        self.region = Region.objects.create(
            name="Lima",
            ubigeo_code="15"
        )
    
    def test_region_creation(self):
        """Test de creación de región"""
        self.assertEqual(self.region.name, "Lima")
        self.assertEqual(self.region.ubigeo_code, "15")
        self.assertIsNone(self.region.deleted_at)
    
    def test_region_str_representation(self):
        """Test de representación en string"""
        self.assertEqual(str(self.region), "15 - Lima")
    
    def test_region_soft_delete(self):
        """Test de soft delete"""
        self.region.delete()
        self.assertIsNotNone(self.region.deleted_at)
    
    def test_region_restore(self):
        """Test de restauración"""
        self.region.delete()
        self.region.restore()
        self.assertIsNone(self.region.deleted_at)


class ProvinceModelTest(TestCase):
    """Tests para el modelo Province"""
    
    def setUp(self):
        self.region = Region.objects.create(
            name="Lima",
            ubigeo_code="15"
        )
        self.province = Province.objects.create(
            name="Lima",
            region=self.region,
            ubigeo_code="1501"
        )
    
    def test_province_creation(self):
        """Test de creación de provincia"""
        self.assertEqual(self.province.name, "Lima")
        self.assertEqual(self.province.region, self.region)
        self.assertEqual(self.province.ubigeo_code, "1501")
    
    def test_province_str_representation(self):
        """Test de representación en string"""
        self.assertEqual(str(self.province), "1501 - Lima")
    
    def test_province_region_relationship(self):
        """Test de relación con región"""
        self.assertEqual(self.province.region.name, "Lima")
        self.assertIn(self.province, self.region.provinces.all())


class DistrictModelTest(TestCase):
    """Tests para el modelo District"""
    
    def setUp(self):
        self.region = Region.objects.create(
            name="Lima",
            ubigeo_code="15"
        )
        self.province = Province.objects.create(
            name="Lima",
            region=self.region,
            ubigeo_code="1501"
        )
        self.district = District.objects.create(
            name="Lima",
            province=self.province,
            ubigeo_code="150101"
        )
    
    def test_district_creation(self):
        """Test de creación de distrito"""
        self.assertEqual(self.district.name, "Lima")
        self.assertEqual(self.district.province, self.province)
        self.assertEqual(self.district.ubigeo_code, "150101")
    
    def test_district_str_representation(self):
        """Test de representación en string"""
        self.assertEqual(str(self.district), "150101 - Lima")
    
    def test_district_province_relationship(self):
        """Test de relación con provincia"""
        self.assertEqual(self.district.province.name, "Lima")
        self.assertIn(self.district, self.province.districts.all())
