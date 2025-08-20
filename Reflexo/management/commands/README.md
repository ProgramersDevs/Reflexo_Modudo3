# Comandos Personalizados - Módulo UBIGEO

Esta carpeta contiene comandos personalizados de Django para el Módulo 7 de UBIGEO. Estos comandos permiten realizar operaciones administrativas y de mantenimiento desde la línea de comandos.

## Comandos Disponibles

### `import_ubigeo_data.py`

Importa datos geográficos desde archivos CSV a la base de datos.

**Uso:**
```bash
python manage.py import_ubigeo_data --type=regions --file=bd/regions.csv
```

**Opciones:**
- `--type`: Tipo de datos a importar (regions, provinces, districts, countries)
- `--file`: Ruta al archivo CSV con los datos
- `--clear`: Opcional. Si se especifica, elimina los datos existentes antes de importar

### `update_ubigeo_codes.py`

Actualiza los códigos UBIGEO para entidades geográficas existentes.

**Uso:**
```bash
python manage.py update_ubigeo_codes --type=regions
```

**Opciones:**
- `--type`: Tipo de entidades a actualizar (regions, provinces, districts)
- `--dry-run`: Opcional. Si se especifica, muestra los cambios sin aplicarlos

### `generate_test_data.py`

Genera datos de prueba para el desarrollo y testing.

**Uso:**
```bash
python manage.py generate_test_data --count=10
```

**Opciones:**
- `--count`: Número de registros a generar para cada entidad
- `--seed`: Opcional. Semilla para el generador de números aleatorios

## Creación de Nuevos Comandos

Para crear un nuevo comando personalizado:

1. Crea un nuevo archivo Python en la carpeta `commands/`
2. Define una clase que herede de `BaseCommand`
3. Implementa el método `handle()` con la lógica del comando

Ejemplo:

```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Descripción del comando'

    def add_arguments(self, parser):
        parser.add_argument('--option', type=str, help='Descripción de la opción')

    def handle(self, *args, **options):
        # Lógica del comando
        self.stdout.write(self.style.SUCCESS('Comando ejecutado con éxito'))
```

## Buenas Prácticas

Al desarrollar comandos personalizados:

1. Proporciona mensajes claros sobre el progreso y resultado
2. Incluye manejo de errores adecuado
3. Documenta las opciones y ejemplos de uso
4. Implementa una opción `--dry-run` cuando sea apropiado
5. Considera la eficiencia para operaciones con grandes volúmenes de datos
6. Agrega logs detallados para facilitar la depuración