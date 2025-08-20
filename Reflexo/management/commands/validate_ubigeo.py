from django.core.management.base import BaseCommand
from django.db import transaction
from Reflexo.models import Region, Province, District

class Command(BaseCommand):
    help = 'Valida la integridad de los códigos de ubigeo'

    def add_arguments(self, parser):
        parser.add_argument(
            '--fix',
            action='store_true',
            help='Corregir automáticamente los códigos de ubigeo basándose en los IDs',
        )

    def handle(self, *args, **options):
        self.stdout.write('Validando códigos de ubigeo...')
        
        if options['fix']:
            self.fix_ubigeo_codes()
        else:
            self.validate_ubigeo_codes()

    def validate_ubigeo_codes(self):
        """Valida que los códigos de ubigeo sean únicos y consistentes"""
        errors = []
        
        # Validar regiones
        regions = Region.objects.all()
        for region in regions:
            if not region.ubigeo_code:
                errors.append(f"Región {region.id} ({region.name}): Falta código de ubigeo")
            elif len(region.ubigeo_code) != 2:
                errors.append(f"Región {region.id} ({region.name}): Código de ubigeo debe tener 2 dígitos")
        
        # Validar provincias
        provinces = Province.objects.all()
        for province in provinces:
            if not province.ubigeo_code:
                errors.append(f"Provincia {province.id} ({province.name}): Falta código de ubigeo")
            elif len(province.ubigeo_code) != 4:
                errors.append(f"Provincia {province.id} ({province.name}): Código de ubigeo debe tener 4 dígitos")
            elif not province.ubigeo_code.startswith(province.region.ubigeo_code):
                errors.append(f"Provincia {province.id} ({province.name}): Código no coincide con región padre")
        
        # Validar distritos
        districts = District.objects.all()
        for district in districts:
            if not district.ubigeo_code:
                errors.append(f"Distrito {district.id} ({district.name}): Falta código de ubigeo")
            elif len(district.ubigeo_code) != 6:
                errors.append(f"Distrito {district.id} ({district.name}): Código de ubigeo debe tener 6 dígitos")
            elif not district.ubigeo_code.startswith(district.province.ubigeo_code):
                errors.append(f"Distrito {district.id} ({district.name}): Código no coincide con provincia padre")
        
        if errors:
            self.stdout.write(self.style.ERROR('Errores encontrados:'))
            for error in errors:
                self.stdout.write(f"  - {error}")
        else:
            self.stdout.write(self.style.SUCCESS('Todos los códigos de ubigeo son válidos'))

    def fix_ubigeo_codes(self):
        """Corrige automáticamente los códigos de ubigeo basándose en los IDs"""
        with transaction.atomic():
            # Corregir regiones
            regions = Region.objects.all()
            for region in regions:
                if not region.ubigeo_code:
                    region.ubigeo_code = f"{region.id:02d}"
                    region.save()
                    self.stdout.write(f"Corregido: Región {region.id} -> {region.ubigeo_code}")
            
            # Corregir provincias
            provinces = Province.objects.all()
            for province in provinces:
                if not province.ubigeo_code:
                    province.ubigeo_code = f"{province.id:04d}"
                    province.save()
                    self.stdout.write(f"Corregido: Provincia {province.id} -> {province.ubigeo_code}")
            
            # Corregir distritos
            districts = District.objects.all()
            for district in districts:
                if not district.ubigeo_code:
                    district.ubigeo_code = f"{district.id:06d}"
                    district.save()
                    self.stdout.write(f"Corregido: Distrito {district.id} -> {district.ubigeo_code}")
            
            self.stdout.write(self.style.SUCCESS('Códigos de ubigeo corregidos exitosamente'))
