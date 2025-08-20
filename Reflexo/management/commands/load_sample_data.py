import csv
import os
from django.core.management.base import BaseCommand
from Reflexo.models import Country, Region, Province, District
from django.db import transaction

class Command(BaseCommand):
    help = 'Carga datos desde archivos CSV'

    def handle(self, *args, **options):
        self.stdout.write('Cargando datos desde archivos CSV......')
        
        # Limpiar datos existentes
        self.stdout.write('Limpiando datos existentes.....')
        District.objects.all().delete()
        Province.objects.all().delete()
        Region.objects.all().delete()
        Country.objects.all().delete()
        
        # Rutas de los archivos CSV
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        csv_dir = os.path.join(base_dir, 'bd')
        
        countries_file = os.path.join(csv_dir, 'countries.csv')
        regions_file = os.path.join(csv_dir, 'regions.csv')
        provinces_file = os.path.join(csv_dir, 'provinces.csv')
        districts_file = os.path.join(csv_dir, 'districts.csv')
        
        # Cargar datos desde CSV
        with transaction.atomic():
            # Cargar países
            self.stdout.write('Cargando países...')
            with open(countries_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    iso2_code = row.get('ISO2', '')
                    # Si el código ya existe, agregar un sufijo
                    if Country.objects.filter(ubigeo_code=iso2_code).exists():
                        iso2_code = f"{iso2_code}_{row['name'][:3].upper()}"
                    
                    Country.objects.create(
                        name=row['name'],
                        ubigeo_code=iso2_code if iso2_code else None
                    )
            
            # Cargar regiones
            self.stdout.write('Cargando regiones...')
            with open(regions_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    Region.objects.create(
                        id=int(row['id']),
                        name=row['name']
                    )
            
            # Cargar provincias
            self.stdout.write('Cargando provincias...')
            with open(provinces_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    Province.objects.create(
                        id=int(row['id']),
                        name=row['name'],
                        region_id=int(row['region_id'])
                    )
            
            # Cargar distritos
            self.stdout.write('Cargando distritos...')
            with open(districts_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    District.objects.create(
                        id=int(row['id']),
                        name=row['name'],
                        province_id=int(row['province_id'])
                    )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Datos cargados exitosamente:\n'
                f'- {Country.objects.count()} países\n'
                f'- {Region.objects.count()} regiones\n'
                f'- {Province.objects.count()} provincias\n'
                f'- {District.objects.count()} distritos'
            )
        )




