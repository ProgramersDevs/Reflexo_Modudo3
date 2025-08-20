# Pruebas - Módulo UBIGEO

Esta carpeta contiene las pruebas unitarias y de integración para el Módulo 7 de UBIGEO. Las pruebas están organizadas por tipo y componente para facilitar su mantenimiento y ejecución.

## Estructura de Pruebas

### `test_models.py`

Contiene pruebas unitarias para los modelos de datos:

- **TestCountryModel**: Pruebas para el modelo Country
  - Creación de países
  - Validación de campos
  - Relaciones con otros modelos

- **TestRegionModel**: Pruebas para el modelo Region
  - Creación de regiones
  - Validación de campos
  - Soft delete y restauración
  - Relaciones con provincias

- **TestProvinceModel**: Pruebas para el modelo Province
  - Creación de provincias
  - Validación de campos
  - Relaciones con regiones y distritos

- **TestDistrictModel**: Pruebas para el modelo District
  - Creación de distritos
  - Validación de campos
  - Relaciones con provincias

- **TestAddressModel**: Pruebas para el modelo Address
  - Creación de direcciones
  - Validación de campos
  - Relaciones con la jerarquía geográfica

### `test_services.py`

Contiene pruebas unitarias para los servicios:

- **TestCountryService**: Pruebas para CountryService
  - Obtención de países
  - Creación, actualización y eliminación
  - Manejo de errores

- **TestRegionService**: Pruebas para RegionService
  - Obtención de regiones
  - Creación, actualización y eliminación
  - Restauración de regiones eliminadas
  - Manejo de errores

- **TestProvinceService**: Pruebas para ProvinceService
  - Obtención de provincias
  - Filtrado por región
  - Creación, actualización y eliminación
  - Manejo de errores

- **TestDistrictService**: Pruebas para DistrictService
  - Obtención de distritos
  - Filtrado por provincia
  - Creación, actualización y eliminación
  - Manejo de errores

- **TestAddressService**: Pruebas para AddressService
  - Obtención de direcciones
  - Filtrado por país, región, provincia y distrito
  - Creación, actualización y eliminación
  - Manejo de errores

### `test_views.py`

Contiene pruebas de integración para las vistas y endpoints de la API:

- **TestCountryViews**: Pruebas para endpoints de países
  - Listado, detalle, creación, actualización y eliminación
  - Validación de respuestas HTTP
  - Formato de datos JSON

- **TestRegionViews**: Pruebas para endpoints de regiones
  - Listado, detalle, creación, actualización y eliminación
  - Validación de respuestas HTTP
  - Formato de datos JSON

- **TestProvinceViews**: Pruebas para endpoints de provincias
  - Listado, detalle, creación, actualización y eliminación
  - Filtrado por región
  - Validación de respuestas HTTP
  - Formato de datos JSON

- **TestDistrictViews**: Pruebas para endpoints de distritos
  - Listado, detalle, creación, actualización y eliminación
  - Filtrado por provincia
  - Validación de respuestas HTTP
  - Formato de datos JSON

- **TestWebViews**: Pruebas para vistas web
  - Renderizado de plantillas
  - Contexto de datos
  - Respuestas HTTP

## Ejecución de Pruebas

Las pruebas pueden ejecutarse utilizando pytest:

```bash
# Ejecutar todas las pruebas
python manage.py test

# Ejecutar pruebas específicas
python manage.py test Reflexo.test.test_models
python manage.py test Reflexo.test.test_services
python manage.py test Reflexo.test.test_views

# Ejecutar con pytest
pytest
```

## Configuración de Pruebas

La configuración de pytest se encuentra en el archivo `pytest.ini` en la raíz del proyecto. Esta configuración incluye:

- Opciones de verbosidad
- Patrones de descubrimiento de pruebas
- Configuración de cobertura
- Plugins activados

## Buenas Prácticas

Al agregar nuevas pruebas, se recomienda:

1. Seguir la estructura existente de organización por tipo de componente
2. Utilizar fixtures para configurar datos de prueba reutilizables
3. Aislar las pruebas para evitar dependencias entre ellas
4. Cubrir casos positivos y negativos (manejo de errores)
5. Mantener las pruebas rápidas y enfocadas
6. Documentar el propósito de cada caso de prueba