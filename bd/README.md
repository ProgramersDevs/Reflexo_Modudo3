# Datos Geográficos - Módulo UBIGEO

Esta carpeta contiene los archivos CSV con datos geográficos utilizados por el Módulo 7 de UBIGEO. Estos archivos sirven como fuente de datos para poblar la base de datos del sistema con información de países, regiones, provincias y distritos.

## Archivos Disponibles

### `countries.csv`

Contiene información sobre países.

**Estructura:**
- `name`: Nombre del país
- `ubigeo_code`: Código UBIGEO del país (opcional)

### `regions.csv`

Contiene información sobre regiones o departamentos de Perú.

**Estructura:**
- `name`: Nombre de la región
- `ubigeo_code`: Código UBIGEO de la región (2 dígitos)

### `provinces.csv`

Contiene información sobre provincias de Perú.

**Estructura:**
- `name`: Nombre de la provincia
- `ubigeo_code`: Código UBIGEO de la provincia (4 dígitos)
- `region_code`: Código UBIGEO de la región a la que pertenece

### `districts.csv`

Contiene información sobre distritos de Perú.

**Estructura:**
- `name`: Nombre del distrito
- `ubigeo_code`: Código UBIGEO del distrito (6 dígitos)
- `province_code`: Código UBIGEO de la provincia a la que pertenece

## Importación de Datos

Para importar estos datos a la base de datos, se utiliza el comando personalizado `import_ubigeo_data`:

```bash
# Importar países
python manage.py import_ubigeo_data --type=countries --file=bd/countries.csv

# Importar regiones
python manage.py import_ubigeo_data --type=regions --file=bd/regions.csv

# Importar provincias
python manage.py import_ubigeo_data --type=provinces --file=bd/provinces.csv

# Importar distritos
python manage.py import_ubigeo_data --type=districts --file=bd/districts.csv
```

## Actualización de Datos

Para actualizar estos archivos:

1. Mantén la estructura de columnas existente
2. Asegúrate de que los códigos UBIGEO sean consistentes entre archivos relacionados
3. Utiliza codificación UTF-8 para preservar caracteres especiales
4. Después de actualizar los archivos, ejecuta el comando de importación correspondiente

## Fuente de Datos

Los datos geográficos de Perú están basados en la información oficial del Instituto Nacional de Estadística e Informática (INEI) y el Registro Nacional de Identificación y Estado Civil (RENIEC).

## Notas Importantes

- Los códigos UBIGEO siguen el estándar oficial de Perú:
  - Regiones: 2 dígitos
  - Provincias: 4 dígitos (2 de región + 2 de provincia)
  - Distritos: 6 dígitos (4 de provincia + 2 de distrito)
- Mantén copias de seguridad de estos archivos antes de realizar modificaciones
- Si encuentras inconsistencias en los datos, repórtalas al equipo de mantenimiento