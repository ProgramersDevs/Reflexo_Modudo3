# Patients Diagnoses App

Esta aplicación maneja la gestión de pacientes, diagnósticos e historiales médicos, estableciendo relaciones con las apps `Reflexo` y `mi_app`.

## Estructura de la Aplicación

```
patients_diagnoses/
├── __init__.py
├── apps.py
├── models/
│   ├── __init__.py
│   ├── patient.py         # Modelo de paciente
│   ├── diagnosis.py       # Modelo de diagnóstico
│   └── medical_record.py  # Historial médico
├── serializers/
│   ├── __init__.py
│   ├── patient.py         # Serializers de paciente
│   ├── diagnosis.py       # Serializers de diagnóstico
│   └── medical_record.py  # Serializers de historial médico
├── views/
│   ├── __init__.py
│   ├── patient.py         # Vistas de paciente
│   ├── diagnosis.py       # Vistas de diagnóstico
│   └── medical_record.py  # Vistas de historial médico
├── services/
│   ├── __init__.py
│   ├── patient_service.py # Servicios de paciente
│   ├── diagnosis_service.py # Servicios de diagnóstico
│   └── medical_record_service.py # Servicios de historial médico
├── urls.py                # URLs del módulo
├── admin.py               # Admin de Django
└── tests/                 # Tests del módulo
    ├── __init__.py
    ├── test_models.py
    ├── test_views.py
    └── test_services.py
```

## Relaciones con Otras Apps

### App Reflexo
La app `patients_diagnoses` utiliza los modelos de ubicación geográfica de `Reflexo`:

- **Country**: País del paciente
- **Region**: Región del paciente  
- **Province**: Provincia del paciente
- **District**: Distrito del paciente

### App mi_app
La app `patients_diagnoses` utiliza el modelo de tipo de documento de `mi_app`:

- **DocumentType**: Tipo de documento de identidad del paciente

## Modelos

### Patient
Modelo principal que representa a un paciente con:
- Información personal (nombre, apellidos, fecha de nacimiento, sexo)
- Información de contacto (teléfonos, email, dirección)
- Información adicional (ocupación, condición de salud)
- Relaciones con ubicación geográfica (Reflexo)
- Relación con tipo de documento (mi_app)
- Campos de auditoría (created_at, updated_at, deleted_at)

### Diagnosis
Modelo que representa diagnósticos médicos con:
- Código único del diagnóstico
- Nombre y descripción
- Campos de auditoría
- Soft delete implementado

### MedicalRecord
Modelo que relaciona pacientes con diagnósticos:
- Relación con Patient y Diagnosis
- Fecha del diagnóstico
- Síntomas, tratamiento y notas
- Estado del diagnóstico (activo, resuelto, crónico, en monitoreo)
- Campos de auditoría

## API Endpoints

### Pacientes
- `GET /api/patients/` - Lista pacientes
- `POST /api/patients/` - Crea paciente
- `GET /api/patients/<id>/` - Obtiene paciente
- `PUT /api/patients/<id>/` - Actualiza paciente
- `DELETE /api/patients/<id>/` - Elimina paciente
- `GET /api/patients/search/` - Busca pacientes

### Diagnósticos
- `GET /api/diagnoses/` - Lista diagnósticos
- `POST /api/diagnoses/` - Crea diagnóstico
- `GET /api/diagnoses/<id>/` - Obtiene diagnóstico
- `PUT /api/diagnoses/<id>/` - Actualiza diagnóstico
- `DELETE /api/diagnoses/<id>/` - Elimina diagnóstico
- `GET /api/diagnoses/search/` - Busca diagnósticos

### Historiales Médicos
- `GET /api/medical-records/` - Lista historiales
- `POST /api/medical-records/` - Crea historial
- `GET /api/medical-records/<id>/` - Obtiene historial
- `PUT /api/medical-records/<id>/` - Actualiza historial
- `DELETE /api/medical-records/<id>/` - Elimina historial
- `GET /api/patients/<id>/medical-history/` - Historial de paciente
- `GET /api/diagnosis-statistics/` - Estadísticas

## Características

- **Soft Delete**: Todos los modelos implementan eliminación lógica
- **Paginación**: Endpoints de lista incluyen paginación
- **Búsqueda**: Funcionalidad de búsqueda en todos los modelos
- **Filtros**: Filtros por diferentes criterios
- **Validaciones**: Validaciones personalizadas en serializers
- **Relaciones**: Relaciones bien definidas entre modelos
- **Auditoría**: Campos de auditoría automáticos

## Configuración

Para que la app funcione correctamente, asegúrate de que:

1. Las apps `Reflexo` y `mi_app` estén en `INSTALLED_APPS`
2. Las migraciones se hayan ejecutado
3. Los modelos de las otras apps tengan datos de ejemplo

## Uso

La app está diseñada para ser utilizada como un módulo completo de gestión médica, permitiendo:

- Registrar y gestionar pacientes
- Mantener un catálogo de diagnósticos
- Crear historiales médicos que relacionen pacientes con diagnósticos
- Consultar estadísticas y reportes
- Realizar búsquedas avanzadas.
