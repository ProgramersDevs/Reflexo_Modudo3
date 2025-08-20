import csv
import os
from django.core.management.base import BaseCommand
from django.db import transaction
from Reflexo.models import Country, Region, Province, District


class Command(BaseCommand):
    help = 'Importa datos geográficos desde archivos CSV de la carpeta bd'

    def add_arguments(self, parser):
        parser.add_argument(
            '--type',
            type=str,
            choices=['countries', 'regions', 'provinces', 'districts', 'all'],
            default='all',
            help='Tipo de datos a importar'
        )
        parser.add_argument(
            '--file',
            type=str,
            help='Ruta específica del archivo CSV a importar'
        )

    def handle(self, *args, **options):
        data_type = options['type']
        file_path = options['file']
        
        # Ruta base de la carpeta bd
        bd_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'bd')
        
        if data_type == 'all' or data_type == 'countries':
            self.import_countries(bd_path)
        
        if data_type == 'all' or data_type == 'regions':
            self.import_regions(bd_path)
        
        if data_type == 'all' or data_type == 'provinces':
            self.import_provinces(bd_path)
        
        if data_type == 'all' or data_type == 'districts':
            self.import_districts(bd_path)

    def import_countries(self, bd_path):
        """Importa países desde countries.csv"""
        file_path = os.path.join(bd_path, 'countries.csv')
        if not os.path.exists(file_path):
            self.stdout.write(self.style.WARNING(f'Archivo no encontrado: {file_path}'))
            return
        
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            countries_created = 0
            
            with transaction.atomic():
                for row in reader:
                    country, created = Country.objects.get_or_create(
                        name=row['name']
                    )
                    if created:
                        countries_created += 1
            
            self.stdout.write(
                self.style.SUCCESS(f'Países importados: {countries_created} nuevos')
            )

    def import_regions(self, bd_path):
        """Importa regiones desde regions.csv"""
        file_path = os.path.join(bd_path, 'regions.csv')
        if not os.path.exists(file_path):
            self.stdout.write(self.style.WARNING(f'Archivo no encontrado: {file_path}'))
            return
        
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            regions_created = 0
            
            with transaction.atomic():
                for row in reader:
                    region, created = Region.objects.get_or_create(
                        id=row['id'],
                        defaults={'name': row['name']}
                    )
                    if created:
                        regions_created += 1
            
            self.stdout.write(
                self.style.SUCCESS(f'Regiones importadas: {regions_created} nuevas')
            )

    def import_provinces(self, bd_path):
        """Importa provincias desde provinces.csv"""
        file_path = os.path.join(bd_path, 'provinces.csv')
        if not os.path.exists(file_path):
            self.stdout.write(self.style.WARNING(f'Archivo no encontrado: {file_path}'))
            return
        
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            provinces_created = 0
            
            with transaction.atomic():
                for row in reader:
                    try:
                        region = Region.objects.get(id=row['region_id'])
                        province, created = Province.objects.get_or_create(
                            id=row['id'],
                            defaults={'name': row['name'], 'region': region}
                        )
                        if created:
                            provinces_created += 1
                    except Region.DoesNotExist:
                        self.stdout.write(
                            self.style.WARNING(f'Región no encontrada con ID: {row["region_id"]}')
                        )
            
            self.stdout.write(
                self.style.SUCCESS(f'Provincias importadas: {provinces_created} nuevas')
            )

    def import_districts(self, bd_path):
        """Importa distritos desde districts.csv"""
        file_path = os.path.join(bd_path, 'districts.csv')
        if not os.path.exists(file_path):
            self.stdout.write(self.style.WARNING(f'Archivo no encontrado: {file_path}'))
            return
        
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            districts_created = 0
            
            with transaction.atomic():
                for row in reader:
                    try:
                        province = Province.objects.get(id=row['province_id'])
                        district, created = District.objects.get_or_create(
                            id=row['id'],
                            defaults={'name': row['name'], 'province': province}
                        )
                        if created:
                            districts_created += 1
                    except Province.DoesNotExist:
                        self.stdout.write(
                            self.style.WARNING(f'Provincia no encontrada con ID: {row["province_id"]}')
                        )
            
            self.stdout.write(
                self.style.SUCCESS(f'Distritos importados: {districts_created} nuevos')
            )
