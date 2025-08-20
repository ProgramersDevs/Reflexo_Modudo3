# Servicios - Módulo UBIGEO

Esta carpeta contiene los servicios que implementan la lógica de negocio para las entidades geográficas del Módulo 7 de UBIGEO. Los servicios actúan como una capa intermedia entre los modelos y las vistas, proporcionando métodos reutilizables para operaciones comunes.

## Estructura de Servicios

### `country_service.py`

Implementa operaciones CRUD y lógica de negocio para el modelo Country (País).

**Métodos principales:**
- `get_all_countries()`: Obtiene todos los países
- `get_country_by_id(country_id)`: Obtiene un país por su ID
- `create_country(data)`: Crea un nuevo país
- `update_country(country_id, data)`: Actualiza un país existente
- `delete_country(country_id)`: Elimina un país

### `region_service.py`

Implementa operaciones CRUD y lógica de negocio para el modelo Region (Región/Departamento).

**Métodos principales:**
- `get_all_regions()`: Obtiene todas las regiones
- `get_region_by_id(region_id)`: Obtiene una región por su ID
- `create_region(data)`: Crea una nueva región
- `update_region(region_id, data)`: Actualiza una región existente
- `delete_region(region_id)`: Elimina una región (soft delete)
- `restore_region(region_id)`: Restaura una región eliminada

### `province_service.py`

Implementa operaciones CRUD y lógica de negocio para el modelo Province (Provincia).

**Métodos principales:**
- `get_all_provinces()`: Obtiene todas las provincias
- `get_province_by_id(province_id)`: Obtiene una provincia por su ID
- `get_provinces_by_region(region_id)`: Obtiene provincias filtradas por región
- `create_province(data)`: Crea una nueva provincia
- `update_province(province_id, data)`: Actualiza una provincia existente
- `delete_province(province_id)`: Elimina una provincia

### `district_service.py`

Implementa operaciones CRUD y lógica de negocio para el modelo District (Distrito).

**Métodos principales:**
- `get_all_districts()`: Obtiene todos los distritos
- `get_district_by_id(district_id)`: Obtiene un distrito por su ID
- `get_districts_by_province(province_id)`: Obtiene distritos filtrados por provincia
- `create_district(data)`: Crea un nuevo distrito
- `update_district(district_id, data)`: Actualiza un distrito existente
- `delete_district(district_id)`: Elimina un distrito

### `address_service.py`

Implementa operaciones CRUD y lógica de negocio para el modelo Address (Dirección).

**Métodos principales:**
- `get_all_addresses()`: Obtiene todas las direcciones
- `get_address_by_id(address_id)`: Obtiene una dirección por su ID
- `get_addresses_by_country(country_id)`: Obtiene direcciones filtradas por país
- `get_addresses_by_region(region_id)`: Obtiene direcciones filtradas por región
- `get_addresses_by_province(province_id)`: Obtiene direcciones filtradas por provincia
- `get_addresses_by_district(district_id)`: Obtiene direcciones filtradas por distrito
- `create_address(data)`: Crea una nueva dirección
- `update_address(address_id, data)`: Actualiza una dirección existente
- `delete_address(address_id)`: Elimina una dirección

## Características Comunes

Todos los servicios implementan:

1. **Manejo de Excepciones**: Captura y gestión de errores específicos
2. **Validación de Datos**: Verificación de datos antes de operaciones de base de datos
3. **Transacciones**: Garantía de integridad en operaciones complejas
4. **Logging**: Registro de operaciones importantes y errores

## Uso de los Servicios

Los servicios están diseñados para ser utilizados desde las vistas o desde otros servicios:

```python
# Ejemplo de uso en una vista
from Reflexo.services.region_service import RegionService

def my_view(request):
    # Obtener todas las regiones
    regions = RegionService.get_all_regions()
    
    # Crear una nueva región
    new_region = RegionService.create_region({
        'name': 'Nueva Región',
        'ubigeo_code': '99'
    })
    
    # Resto del código...
```

## Extensión de Servicios

Para extender la funcionalidad de un servicio, se recomienda:

1. Agregar nuevos métodos a la clase de servicio existente
2. Mantener la coherencia en el manejo de excepciones y validaciones
3. Documentar los nuevos métodos siguiendo el estilo existente
4. Agregar pruebas unitarias para los nuevos métodos en la carpeta test/