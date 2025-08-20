# Serializadores - Módulo UBIGEO

Esta carpeta contiene los serializadores utilizados para convertir los modelos de datos a formatos JSON para la API REST del Módulo 7 de UBIGEO. Los serializadores son una parte fundamental de Django Rest Framework y permiten la transformación bidireccional entre objetos Python y formatos de datos como JSON.

## Estructura de Serializadores

### `country_serializer.py`

Contiene serializadores para el modelo Country (País).

**Clases principales:**
- `CountrySerializer`: Serializa todos los campos del modelo Country
- `CountryBasicSerializer`: Versión simplificada con campos esenciales

**Campos serializados:**
- `id`: Identificador único
- `name`: Nombre del país
- `ubigeo_code`: Código de ubigeo (opcional)
- `created_at`: Fecha de creación
- `updated_at`: Fecha de actualización

### `region_serializer.py`

Contiene serializadores para el modelo Region (Región/Departamento).

**Clases principales:**
- `RegionSerializer`: Serializa todos los campos del modelo Region
- `RegionWithProvincesSerializer`: Incluye provincias anidadas

**Campos serializados:**
- `id`: Identificador único
- `name`: Nombre de la región
- `ubigeo_code`: Código de ubigeo
- `created_at`: Fecha de creación
- `updated_at`: Fecha de actualización
- `provinces`: Lista de provincias (en RegionWithProvincesSerializer)

### `province_serializer.py`

Contiene serializadores para el modelo Province (Provincia).

**Clases principales:**
- `ProvinceSerializer`: Serializa todos los campos del modelo Province
- `ProvinceWithDistrictsSerializer`: Incluye distritos anidados
- `ProvinceWithRegionSerializer`: Incluye información de la región

**Campos serializados:**
- `id`: Identificador único
- `name`: Nombre de la provincia
- `ubigeo_code`: Código de ubigeo
- `region`: Información de la región (ID o datos completos)
- `created_at`: Fecha de creación
- `updated_at`: Fecha de actualización
- `districts`: Lista de distritos (en ProvinceWithDistrictsSerializer)

### `district_serializer.py`

Contiene serializadores para el modelo District (Distrito).

**Clases principales:**
- `DistrictSerializer`: Serializa todos los campos del modelo District
- `DistrictWithProvinceSerializer`: Incluye información de la provincia
- `DistrictCompleteSerializer`: Incluye información completa de provincia y región

**Campos serializados:**
- `id`: Identificador único
- `name`: Nombre del distrito
- `ubigeo_code`: Código de ubigeo
- `province`: Información de la provincia (ID o datos completos)
- `created_at`: Fecha de creación
- `updated_at`: Fecha de actualización

### `address_serializer.py`

Contiene serializadores para el modelo Address (Dirección).

**Clases principales:**
- `AddressSerializer`: Serializa todos los campos del modelo Address
- `AddressCompleteSerializer`: Incluye información completa de ubicación geográfica

**Campos serializados:**
- `id`: Identificador único
- `street`: Nombre de calle
- `number`: Número de dirección
- `district`: Distrito (ID o datos completos)
- `province`: Provincia (ID o datos completos)
- `region`: Región (ID o datos completos)
- `country`: País (ID o datos completos)
- `postal_code`: Código postal
- `reference`: Referencia adicional
- `created_at`: Fecha de creación
- `updated_at`: Fecha de actualización

## Características Comunes

Todos los serializadores implementan:

1. **Validación de Datos**: Verificación de datos antes de la deserialización
2. **Relaciones Anidadas**: Manejo de relaciones entre modelos
3. **Campos Calculados**: Algunos serializadores incluyen campos calculados
4. **Control de Profundidad**: Opciones para controlar la profundidad de las relaciones

## Uso de los Serializadores

Los serializadores se utilizan principalmente en las vistas de la API:

```python
# Ejemplo de uso en una vista basada en función
from Reflexo.serializers.region_serializer import RegionSerializer
from Reflexo.models.region import Region
from rest_framework.response import Response

def get_regions(request):
    regions = Region.objects.all()
    serializer = RegionSerializer(regions, many=True)
    return Response(serializer.data)
```

## Extensión de Serializadores

Para extender la funcionalidad de un serializador, se recomienda:

1. Crear una nueva clase que herede del serializador base
2. Agregar campos adicionales o sobrescribir métodos según sea necesario
3. Mantener la coherencia en la validación y transformación de datos
4. Documentar los nuevos serializadores siguiendo el estilo existente