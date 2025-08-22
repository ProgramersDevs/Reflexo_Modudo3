# Patients Diagnoses App

Esta aplicación maneja la gestión de pacientes, diagnósticos e historiales médicos, estableciendo relaciones con las apps Reflexo y mi_app.

## Estructura de la Aplicación

patients_diagnoses/
├── __init__.py
├── apps.py
├── models/
│   ├── __init__.py
│   ├── patient.py             # Modelo de paciente
│   ├── diagnosis.py           # Modelo de diagnóstico
│   └── medical_record.py      # Historial médico
├── serializers/
│   ├── __init__.py
│   ├── patient.py             # Serializers de paciente
│   ├── diagnosis.py           # Serializers de diagnóstico
│   └── medical_record.py      # Serializers de historial médico
├── views/
│   ├── __init__.py
│   ├── patient.py             # Vistas de paciente
│   ├── diagnosis.py           # Vistas de diagnóstico
│   └── medical_record.py      # Vistas de historial médico
├── services/
│   ├── __init__.py
│   ├── patient_service.py     # Servicios de paciente
│   ├── diagnosis_service.py   # Servicios de diagnóstico
│   └── medical_record_service.py # Servicios de historial médico
├── urls.py                    # URLs del módulo
├── admin.py                   # Admin de Django
└── tests/                     # Tests del módulo
    ├── __init__.py
    ├── test_models.py
    ├── test_views.py
    └── test_services.py

## Relaciones con Otras Apps

### App Reflexo
La app patients_diagnoses utiliza los modelos de ubicación geográfica de Reflexo:

- *Country*: País del paciente
- *Region*: Región del paciente  
- *Province*: Provincia del paciente
- *District*: Distrito del paciente

### App mi_app
La app patients_diagnoses utiliza el modelo de tipo de documento de mi_app:

- *DocumentType*: Tipo de documento de identidad del paciente

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
## 📑 Documentación de Endpoints
# Documentación de Endpoints - Aplicación de Pacientes y Diagnósticos
A continuación se presenta la documentación completa de todos los endpoints disponibles en la aplicación de pacientes y diagnósticos.

## Endpoints de Pacientes
### Listar Pacientes
- URL : /patients/
- Método : GET
- Descripción : Obtiene una lista paginada de todos los pacientes activos.
- Parámetros de consulta :
  - page : Número de página (por defecto: 1)
  - per_page : Cantidad de registros por página (por defecto: 10)
- Respuesta exitosa :
  
  {
    "count": 100,
    "num_pages": 10,
    "current_page": 1,
    "results": [...]
  }
  
### Buscar Pacientes
- URL : /patients/search/
- Método : GET
- Descripción : Busca pacientes según criterios específicos.
- Parámetros de consulta : Varios criterios de búsqueda como nombre, documento, etc.
- Respuesta exitosa : Similar a listar pacientes, pero filtrado según criterios.
### Ver Detalle de Paciente
- URL : /patients/{id}/
- Método : GET
- Descripción : Obtiene información detallada de un paciente específico.
- Respuesta exitosa : Datos completos del paciente.
### Crear Paciente
- URL : /patients/
- Método : POST
- Descripción : Crea un nuevo registro de paciente.
- Cuerpo de la solicitud : Datos del paciente a crear.
- Respuesta exitosa : Datos del paciente creado con código 201.
### Actualizar Paciente
- URL : /patients/{id}/
- Método : PUT
- Descripción : Actualiza los datos de un paciente existente.
- Cuerpo de la solicitud : Datos actualizados del paciente.
- Respuesta exitosa : Datos actualizados del paciente.
### Eliminar Paciente
- URL : /patients/{id}/
- Método : DELETE
- Descripción : Elimina (soft delete) un paciente existente.
- Respuesta exitosa : Código 204 sin contenido.
## Endpoints de Diagnósticos
### Listar Diagnósticos
- URL : /diagnoses/
- Método : GET
- Descripción : Obtiene una lista paginada de todos los diagnósticos.
- Parámetros de consulta :
  - page : Número de página (por defecto: 1)
  - page_size : Cantidad de registros por página (por defecto: 10)
  - search : Término de búsqueda general
- Respuesta exitosa :
  
  {
    "count": 100,
    "num_pages": 10,
    "current_page": 1,
    "results": [...]
  }
  
### Buscar Diagnósticos
- URL : /diagnoses/search/
- Método : GET
- Descripción : Busca diagnósticos por nombre o código.
- Parámetros de consulta :
  - q : Término de búsqueda
- Respuesta exitosa : Lista de diagnósticos que coinciden con el criterio.
### Ver Detalle de Diagnóstico
- URL : /diagnoses/{id}/
- Método : GET
- Descripción : Obtiene información detallada de un diagnóstico específico.
- Respuesta exitosa : Datos completos del diagnóstico.
### Crear Diagnóstico
- URL : /diagnoses/
- Método : POST
- Descripción : Crea un nuevo registro de diagnóstico.
- Cuerpo de la solicitud : Datos del diagnóstico a crear.
- Respuesta exitosa : Datos del diagnóstico creado con código 201.
### Actualizar Diagnóstico
- URL : /diagnoses/{id}/
- Método : PUT
- Descripción : Actualiza los datos de un diagnóstico existente.
- Cuerpo de la solicitud : Datos actualizados del diagnóstico.
- Respuesta exitosa : Datos actualizados del diagnóstico.
### Eliminar Diagnóstico
- URL : /diagnoses/{id}/
- Método : DELETE
- Descripción : Elimina (soft delete) un diagnóstico existente.
- Respuesta exitosa : Código 204 sin contenido.
## Endpoints de Historiales Médicos
### Listar Historiales Médicos
- URL : /medical-records/
- Método : GET
- Descripción : Obtiene una lista paginada de todos los historiales médicos.
- Parámetros de consulta :
  - page : Número de página (por defecto: 1)
  - page_size : Cantidad de registros por página (por defecto: 10)
  - search : Término de búsqueda general
  - patient_id : Filtrar por ID de paciente
  - diagnosis_id : Filtrar por ID de diagnóstico
  - status : Filtrar por estado
  - date_from : Filtrar desde fecha
  - date_to : Filtrar hasta fecha
- Respuesta exitosa :
  
  {
    "count": 100,
    "num_pages": 10,
    "current_page": 1,
    "results": [...]
  }
  
### Ver Detalle de Historial Médico
- URL : /medical-records/{id}/
- Método : GET
- Descripción : Obtiene información detallada de un historial médico específico.
- Respuesta exitosa : Datos completos del historial médico.
### Crear Historial Médico
- URL : /medical-records/
- Método : POST
- Descripción : Crea un nuevo registro de historial médico.
- Cuerpo de la solicitud : Datos del historial médico a crear.
- Respuesta exitosa : Datos del historial médico creado con código 201.
### Actualizar Historial Médico
- URL : /medical-records/{id}/
- Método : PUT
- Descripción : Actualiza los datos de un historial médico existente.
- Cuerpo de la solicitud : Datos actualizados del historial médico.
- Respuesta exitosa : Datos actualizados del historial médico.
### Eliminar Historial Médico
- URL : /medical-records/{id}/
- Método : DELETE
- Descripción : Elimina (soft delete) un historial médico existente.
- Respuesta exitosa : Código 204 sin contenido.
### Historial Médico de un Paciente
- URL : /patients/{patient_id}/medical-history/
- Método : GET
- Descripción : Obtiene todo el historial médico de un paciente específico.
- Parámetros de consulta :
  - page : Número de página (por defecto: 1)
  - page_size : Cantidad de registros por página (por defecto: 10)
- Respuesta exitosa :
  
  {
    "count": 100,
    "num_pages": 10,
    "current_page": 1,
    "results": [...]
  }
  
### Estadísticas de Diagnósticos
- URL : /diagnosis-statistics/
- Método : GET
- Descripción : Obtiene estadísticas generales sobre los diagnósticos registrados.
- Respuesta exitosa : Datos estadísticos sobre diagnósticos.
## Notas Adicionales
- Todos los endpoints que devuelven listas soportan paginación.
- La mayoría de los endpoints implementan soft delete para mantener la integridad referencial.
- Los endpoints de búsqueda permiten filtrar por diferentes criterios según el tipo de entidad.
- Todos los endpoints requieren autenticación y tienen permisos específicos configurados.

## API Endpoints

### Pacientes
- GET /api/patients/ - Lista pacientes
- POST /api/patients/ - Crea paciente
- GET /api/patients/<id>/ - Obtiene paciente
- PUT /api/patients/<id>/ - Actualiza paciente
- DELETE /api/patients/<id>/ - Elimina paciente
- GET /api/patients/search/ - Busca pacientes

### Diagnósticos
- GET /api/diagnoses/ - Lista diagnósticos
- POST /api/diagnoses/ - Crea diagnóstico
- GET /api/diagnoses/<id>/ - Obtiene diagnóstico
- PUT /api/diagnoses/<id>/ - Actualiza diagnóstico
- DELETE /api/diagnoses/<id>/ - Elimina diagnóstico
- GET /api/diagnoses/search/ - Busca diagnósticos

### Historiales Médicos
- GET /api/medical-records/ - Lista historiales
- POST /api/medical-records/ - Crea historial
- GET /api/medical-records/<id>/ - Obtiene historial
- PUT /api/medical-records/<id>/ - Actualiza historial
- DELETE /api/medical-records/<id>/ - Elimina historial
- GET /api/patients/<id>/medical-history/ - Historial de paciente
- GET /api/diagnosis-statistics/ - Estadísticas

## Características

- *Soft Delete*: Todos los modelos implementan eliminación lógica
- *Paginación*: Endpoints de lista incluyen paginación
- *Búsqueda*: Funcionalidad de búsqueda en todos los modelos
- *Filtros*: Filtros por diferentes criterios
- *Validaciones*: Validaciones personalizadas en serializers
- *Relaciones*: Relaciones bien definidas entre modelos
- *Auditoría*: Campos de auditoría automáticos

## Configuración

Para que la app funcione correctamente, asegúrate de que:

1. Las apps Reflexo y mi_app estén en INSTALLED_APPS
2. Las migraciones se hayan ejecutado
3. Los modelos de las otras apps tengan datos de ejemplo

## Uso

La app está diseñada para ser utilizada como un módulo completo de gestión médica, permitiendo:

- Registrar y gestionar pacientes
- Mantener un catálogo de diagnósticos
- Crear historiales médicos que relacionen pacientes con diagnósticos
- Consultar estadísticas y reportes
- Realizar búsquedas avanzadas.
