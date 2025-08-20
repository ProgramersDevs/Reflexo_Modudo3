# Estructura de Vistas - Reflexo

## Organización de Archivos

El código CRUD ha sido reorganizado en archivos específicos por entidad para mejorar la mantenibilidad y organización del código.

### Archivos de Vistas

#### `views_region.py`
Contiene todas las funciones CRUD para **Regiones**:
- `regions()` - Listar todas las regiones
- `region_detail(request, region_id)` - Obtener una región específica
- `region_create(request)` - Crear una nueva región
- `region_update(request, region_id)` - Actualizar una región
- `region_delete(request, region_id)` - Eliminar una región (soft delete)

#### `views_provincia.py`
Contiene todas las funciones CRUD para **Provincias**:
- `provinces(request, region_id=None)` - Listar provincias (opcionalmente filtradas por región)
- `province_detail(request, province_id)` - Obtener una provincia específica
- `province_create(request)` - Crear una nueva provincia
- `province_update(request, province_id)` - Actualizar una provincia
- `province_delete(request, province_id)` - Eliminar una provincia

#### `views_distrito.py`
Contiene todas las funciones CRUD para **Distritos**:
- `districts(request, province_id=None)` - Listar distritos (opcionalmente filtrados por provincia)
- `district_detail(request, district_id)` - Obtener un distrito específico
- `district_create(request)` - Crear un nuevo distrito
- `district_update(request, district_id)` - Actualizar un distrito
- `district_delete(request, district_id)` - Eliminar un distrito

#### `views_country.py`
Contiene todas las funciones CRUD para **Países**:
- `countries(request)` - Listar todos los países
- `country_detail(request, country_id)` - Obtener un país específico
- `country_create(request)` - Crear un nuevo país
- `country_update(request, country_id)` - Actualizar un país
- `country_delete(request, country_id)` - Eliminar un país

#### `views_web.py`
Contiene las vistas web para renderizar templates HTML.

#### `views_ubigeoController.py`
Archivo de referencia que indica dónde se han movido las funciones CRUD.

## Endpoints API

### Versión 3 (CRUD Completo)
- **Regiones**: `/api/v3/regions/`
- **Provincias**: `/api/v3/provinces/`
- **Distritos**: `/api/v3/districts/`
- **Países**: `/api/v3/countries/`

### Versión 2 (Compatibilidad)
- **Regiones**: `/api/v2/regions/`
- **Provincias**: `/api/v2/provinces/`
- **Distritos**: `/api/v2/districts/`
- **Países**: `/api/v2/countries/`

### Versión 1 (Simples)
- **Regiones**: `/api/regions/`
- **Provincias**: `/api/provinces/`
- **Distritos**: `/api/districts/`
- **Países**: `/api/countries/`

## Características

- **Validación de datos**: Todas las funciones incluyen validación de campos obligatorios
- **Manejo de errores**: Respuestas JSON consistentes con códigos de estado HTTP apropiados
- **Soft Delete**: Las regiones y provincias usan soft delete para mantener integridad referencial
- **Códigos Únicos**: Validación de códigos de ubigeo únicos
- **Relaciones**: Validación de relaciones entre entidades (región → provincia → distrito)

## Uso

Todas las funciones están disponibles a través de las importaciones en `__init__.py`:

```python
from Reflexo.views import (
    regions, region_create, region_update, region_delete,
    provinces, province_create, province_update, province_delete,
    districts, district_create, district_update, district_delete,
    countries, country_create, country_update, country_delete
)
```
