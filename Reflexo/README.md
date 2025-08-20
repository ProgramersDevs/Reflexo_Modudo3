# Aplicación Reflexo - Módulo UBIGEO

Esta es la aplicación principal del Módulo 7 de UBIGEO, que proporciona funcionalidades para gestionar datos geográficos de Perú y otros países, incluyendo regiones, provincias y distritos.

## Estructura de la Aplicación

La aplicación está organizada en los siguientes directorios:

- **models/**: Definición de modelos de datos
- **views/**: Vistas y controladores para la API y páginas web
- **serializers/**: Serializadores para la API REST
- **services/**: Lógica de negocio y servicios
- **management/**: Comandos personalizados de Django
- **test/**: Pruebas unitarias y de integración

## Modelos

La aplicación maneja los siguientes modelos principales:

- **Country**: Países con código UBIGEO
- **Region**: Regiones o departamentos de Perú
- **Province**: Provincias dentro de las regiones
- **District**: Distritos dentro de las provincias
- **Address**: Direcciones completas vinculadas a la jerarquía geográfica

Cada modelo incluye campos para seguimiento de creación y actualización, así como relaciones jerárquicas entre entidades geográficas.

## Servicios

Los servicios implementan la lógica de negocio para cada entidad:

- **CountryService**: Operaciones CRUD para países
- **RegionService**: Operaciones CRUD para regiones
- **ProvinceService**: Operaciones CRUD para provincias
- **DistrictService**: Operaciones CRUD para distritos
- **AddressService**: Operaciones CRUD para direcciones

Cada servicio proporciona métodos para listar, crear, actualizar y eliminar registros, así como consultas específicas por relaciones jerárquicas.

## Vistas

La aplicación proporciona dos tipos de vistas:

1. **Vistas API**: Endpoints REST para consumo por aplicaciones cliente
   - Múltiples versiones de API (v1, v2, v3)
   - Operaciones CRUD completas
   - Filtrado por jerarquía geográfica

2. **Vistas Web**: Páginas HTML para visualización en navegador
   - Página de inicio con resumen
   - Vistas para explorar países, regiones, provincias y distritos
   - Vista de depuración

## Serializers

Los serializadores convierten los modelos a formatos JSON para la API:

- **CountrySerializer**: Serialización de países
- **RegionSerializer**: Serialización de regiones
- **ProvinceSerializer**: Serialización de provincias
- **DistrictSerializer**: Serialización de distritos
- **AddressSerializer**: Serialización de direcciones

## Pruebas

La carpeta `test/` contiene pruebas unitarias y de integración para:

- Modelos (test_models.py)
- Servicios (test_services.py)
- Vistas (test_views.py)

## Comandos Personalizados

La aplicación incluye comandos personalizados en la carpeta `management/commands/` para tareas como:

- Importación de datos geográficos desde archivos CSV
- Actualización masiva de códigos UBIGEO
- Generación de datos de prueba

## Uso de la Aplicación

Para utilizar esta aplicación como parte de otro proyecto:

1. Asegúrate de que las dependencias en requirements.txt estén instaladas
2. Incluye 'Reflexo' en INSTALLED_APPS de tu settings.py
3. Importa los modelos, servicios o vistas necesarios
4. Utiliza la API REST para integrar con aplicaciones frontend

Consulta la documentación de la API en la carpeta Config para ver todos los endpoints disponibles.