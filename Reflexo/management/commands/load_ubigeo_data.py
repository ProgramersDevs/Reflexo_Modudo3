import csv
import os
from django.core.management.base import BaseCommand
from django.db import transaction
from Reflexo.models import Region, Province, District

class Command(BaseCommand):
    help = 'Carga datos de ubigeo desde archivos CSV y asigna códigos de ubigeo'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Forzar la recarga de datos existentes',
        )

    def handle(self, *args, **options):
        self.stdout.write('Cargando datos de ubigeo...')
        
        # Obtener la ruta de los archivos CSV
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        csv_dir = os.path.join(base_dir, 'bd')
        
        with transaction.atomic():
            if options['force']:
                self.stdout.write('Eliminando datos existentes...')
                District.objects.all().delete()
                Province.objects.all().delete()
                Region.objects.all().delete()
            
            # Cargar regiones
            self.load_regions(csv_dir)
            
            # Cargar provincias
            self.load_provinces(csv_dir)
            
            # Cargar distritos
            self.load_districts(csv_dir)
            
            self.stdout.write(self.style.SUCCESS('Datos de ubigeo cargados exitosamente'))

    def load_regions(self, csv_dir):
        """Carga regiones desde el archivo CSV"""
        regions_file = os.path.join(csv_dir, 'regions.csv')
        
        if not os.path.exists(regions_file):
            self.stdout.write(self.style.WARNING(f'Archivo no encontrado: {regions_file}'))
            return
        
        with open(regions_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for row in reader:
                region_id = int(row['id'])
                name = row['name']
                
                # Crear o actualizar región
                region, created = Region.objects.get_or_create(
                    id=region_id,
                    defaults={
                        'name': name,
                        'ubigeo_code': f"{region_id:02d}"
                    }
                )
                
                if created:
                    self.stdout.write(f"Creada región: {region_id} - {name}")
                else:
                    # Actualizar código de ubigeo si no existe
                    if not region.ubigeo_code:
                        region.ubigeo_code = f"{region_id:02d}"
                        region.save()
                        self.stdout.write(f"Actualizado código de ubigeo para región: {region_id}")

    def load_provinces(self, csv_dir):
        """Carga provincias desde el archivo CSV"""
        provinces_file = os.path.join(csv_dir, 'provinces.csv')
        
        if not os.path.exists(provinces_file):
            self.stdout.write(self.style.WARNING(f'Archivo no encontrado: {provinces_file}'))
            return
        
        with open(provinces_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for row in reader:
                province_id = int(row['id'])
                name = row['name']
                region_id = int(row['region_id'])
                
                try:
                    region = Region.objects.get(id=region_id)
                    
                    # Crear o actualizar provincia
                    province, created = Province.objects.get_or_create(
                        id=province_id,
                        defaults={
                            'name': name,
                            'region': region,
                            'ubigeo_code': f"{province_id:04d}"
                        }
                    )
                    
                    if created:
                        self.stdout.write(f"Creada provincia: {province_id} - {name}")
                    else:
                        # Actualizar código de ubigeo si no existe
                        if not province.ubigeo_code:
                            province.ubigeo_code = f"{province_id:04d}"
                            province.save()
                            self.stdout.write(f"Actualizado código de ubigeo para provincia: {province_id}")
                
                except Region.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Región {region_id} no encontrada para provincia {province_id}'))

    def load_districts(self, csv_dir):
        """Carga distritos desde el archivo CSV"""
        districts_file = os.path.join(csv_dir, 'districts.csv')
        
        if not os.path.exists(districts_file):
            self.stdout.write(self.style.WARNING(f'Archivo no encontrado: {districts_file}'))
            return
        
        with open(districts_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for row in reader:
                district_id = int(row['id'])
                name = row['name']
                province_id = int(row['province_id'])
                
                try:
                    province = Province.objects.get(id=province_id)
                    
                    # Crear o actualizar distrito
                    district, created = District.objects.get_or_create(
                        id=district_id,
                        defaults={
                            'name': name,
                            'province': province,
                            'ubigeo_code': f"{district_id:06d}"
                        }
                    )
                    
                    if created:
                        self.stdout.write(f"Creado distrito: {district_id} - {name}")
                    else:
                        # Actualizar código de ubigeo si no existe
                        if not district.ubigeo_code:
                            district.ubigeo_code = f"{district_id:06d}"
                            district.save()
                            self.stdout.write(f"Actualizado código de ubigeo para distrito: {district_id}")
                
                except Province.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Provincia {province_id} no encontrada para distrito {district_id}'))
