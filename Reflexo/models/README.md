# Estructura de Modelos - Reflexo

## Organización de Archivos

Los modelos de datos están organizados en archivos específicos por entidad para mantener una estructura clara y modular del sistema de ubicaciones.

### Archivos de Modelos

#### `country.py`
Contiene el modelo principal **Country** y sus modelos relacionados:
- `Country` - Modelo principal de países
- `CountryUser` - Relación muchos a muchos con usuarios
- `CountryPatient` - Relación muchos a muchos con pacientes
- `CountryTherapist` - Relación muchos a muchos con terapeutas

**Campos principales:**
- `name` - Nombre del país (CharField, max_length=100)
- `ubigeo_code` - Código de ubigeo único (CharField, max_length=10, opcional)
- `created_at` - Fecha de creación automática
- `updated_at` - Fecha de actualización automática

#### `region.py`
Contiene el modelo principal **Region** y sus modelos relacionados:
- `Region` - Modelo principal de regiones
- `RegionUser` - Relación muchos a muchos con usuarios
- `RegionPatient` - Relación muchos a muchos con pacientes
- `RegionTherapist` - Relación muchos a muchos con terapeutas

**Características especiales:**
- **Soft Delete**: Implementa eliminación lógica con `deleted_at`
- `restore()` - Método para restaurar registros eliminados
- `ubigeo_code` - Código de ubigeo de 2 dígitos
- Campos de auditoría: `created_at`, `updated_at`

#### `province.py`
Contiene el modelo principal **Province** y sus modelos relacionados:
- `Province` - Modelo principal de provincias
- `ProvinceUser` - Relación muchos a muchos con usuarios
- `ProvincePatient` - Relación muchos a muchos con pacientes
- `ProvinceTherapist` - Relación muchos a muchos con terapeutas
- `ProvinceDistrict` - Relación con distritos

**Relaciones:**
- `region` - ForeignKey a Region (relacion_name='provinces')
- `ubigeo_code` - Código de ubigeo de 4 dígitos

#### `district.py`
Contiene el modelo principal **District** y sus modelos relacionados:
- `District` - Modelo principal de distritos
- `DistrictUser` - Relación muchos a muchos con usuarios
- `DistrictPatient` - Relación muchos a muchos con pacientes
- `DistrictTherapist` - Relación muchos a muchos con terapeutas

**Relaciones:**
- `province` - ForeignKey a Province (related_name='districts')
- `ubigeo_code` - Código de ubigeo de 6 dígitos

## Jerarquía de Ubicaciones

```
Country (País)
└── Region (Región)
    └── Province (Provincia)
        └── District (Distrito)
```

### Relaciones Clave

1. **Country** → **Region**: Un país puede tener múltiples regiones
2. **Region** → **Province**: Una región puede tener múltiples provincias
3. **Province** → **District**: Una provincia puede tener múltiples distritos

### Códigos de Ubigeo

- **Country**: 2-10 dígitos (opcional)
- **Region**: 2 dígitos
- **Province**: 4 dígitos
- **District**: 6 dígitos

## Características de los Modelos

### Campos Comunes
- `name` - Nombre de la entidad
- `ubigeo_code` - Código de ubigeo único
- `created_at` - Fecha de creación automática
- `updated_at` - Fecha de actualización automática

### Soft Delete (Solo Region)
- `deleted_at` - Campo para eliminación lógica
- Método `delete()` personalizado
- Método `restore()` para recuperar registros

### Modelos de Relación
Cada entidad principal tiene modelos relacionados para:
- **Users**: Usuarios asociados a la ubicación
- **Patients**: Pacientes asociados a la ubicación
- **Therapists**: Terapeutas asociados a la ubicación

## Uso de los Modelos

### Importación
```python
from Reflexo.models import (
    Country, Region, Province, District,
    CountryUser, RegionUser, ProvinceUser, DistrictUser,
    CountryPatient, RegionPatient, ProvincePatient, DistrictPatient,
    CountryTherapist, RegionTherapist, ProvinceTherapist, DistrictTherapist
)
```

### Ejemplos de Consultas

```python
# Obtener todas las regiones activas
regions = Region.objects.filter(deleted_at__isnull=True)

# Obtener provincias de una región específica
provinces = Province.objects.filter(region_id=1)

# Obtener distritos de una provincia específica
districts = District.objects.filter(province_id=1)

# Crear una nueva región
region = Region.objects.create(
    name="Costa",
    ubigeo_code="CO"
)

# Soft delete de una región
region.delete()  # Marca deleted_at pero no elimina físicamente

# Restaurar una región eliminada
region.restore()
```

### Validaciones

- **Códigos únicos**: Los códigos de ubigeo deben ser únicos por entidad
- **Relaciones**: Las provincias deben pertenecer a una región válida
- **Integridad**: Los distritos deben pertenecer a una provincia válida

## Meta Información

### Verbose Names
- Country: "País" / "Países"
- Region: "Región" / "Regiones"
- Province: "Provincia" / "Provincias"
- District: "Distrito" / "Distritos"

### Tabla Personalizada
- Region usa la tabla "region" en lugar del nombre por defecto

## Migraciones

Los modelos incluyen migraciones para:
- Creación de tablas
- Adición de campos de ubigeo
- Modificación de relaciones
- Actualización de metadatos

Para aplicar migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```
