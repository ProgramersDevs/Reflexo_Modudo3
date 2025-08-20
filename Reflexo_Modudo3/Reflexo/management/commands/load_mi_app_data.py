from django.core.management.base import BaseCommand
from django.db import transaction
from mi_app.models import DocumentType, PaymentType, PredeterminedPrice


class Command(BaseCommand):
    help = 'Carga datos de ejemplo para mi_app (DocumentType, PaymentType, PredeterminedPrice)'

    def handle(self, *args, **options):
        with transaction.atomic():
            # Crear tipos de documento
            document_types = [
                {'name': 'DNI', 'description': 'Documento Nacional de Identidad'},
                {'name': 'CE', 'description': 'Carné de Extranjería'},
                {'name': 'PASAPORTE', 'description': 'Pasaporte'},
                {'name': 'RUC', 'description': 'Registro Único de Contribuyentes'},
                {'name': 'CARNET DE SALUD', 'description': 'Carné de Salud'},
            ]
            
            for dt_data in document_types:
                dt, created = DocumentType.objects.get_or_create(
                    name=dt_data['name'],
                    defaults={'description': dt_data['description']}
                )
                if created:
                    self.stdout.write(f'Creado DocumentType: {dt.name}')
            
            # Crear tipos de pago
            payment_types = [
                {'code': 'EFECTIVO', 'name': 'Efectivo'},
                {'code': 'TARJETA', 'name': 'Tarjeta de Crédito/Débito'},
                {'code': 'TRANSFERENCIA', 'name': 'Transferencia Bancaria'},
                {'code': 'YAPE', 'name': 'Yape'},
                {'code': 'PLIN', 'name': 'Plin'},
                {'code': 'TUNKI', 'name': 'Tunki'},
                {'code': 'CHEQUE', 'name': 'Cheque'},
            ]
            
            for pt_data in payment_types:
                pt, created = PaymentType.objects.get_or_create(
                    code=pt_data['code'],
                    defaults={'name': pt_data['name']}
                )
                if created:
                    self.stdout.write(f'Creado PaymentType: {pt.name}')
            
            # Crear precios predeterminados
            predetermined_prices = [
                {'name': 'Consulta General', 'price': 50.00},
                {'name': 'Consulta Especializada', 'price': 80.00},
                {'name': 'Terapia Física', 'price': 60.00},
                {'name': 'Evaluación Médica', 'price': 100.00},
                {'name': 'Seguimiento', 'price': 30.00},
                {'name': 'Consulta de Emergencia', 'price': 120.00},
                {'name': 'Terapia Psicológica', 'price': 70.00},
                {'name': 'Examen de Laboratorio', 'price': 45.00},
            ]
            
            for pp_data in predetermined_prices:
                pp, created = PredeterminedPrice.objects.get_or_create(
                    name=pp_data['name'],
                    defaults={'price': pp_data['price']}
                )
                if created:
                    self.stdout.write(f'Creado PredeterminedPrice: {pp.name} - S/. {pp.price}')
        
        self.stdout.write(
            self.style.SUCCESS('Datos de mi_app cargados exitosamente')
        )

