Módulo 03 – Gestión de Pacientes y Diagnósticos (Django)

Objetivo General
Gestionar de forma completa los pacientes y sus diagnósticos médicos, incluyendo registro, actualización, búsqueda avanzada y manejo de información médica básica, utilizando Django y Django REST Framework.

Meta: Implementar arquitectura MVC adaptada a Django + APIs REST para React

Diagnosticos (diagnoses/)
Propósito: Gestión de los diagnósticos médicos disponibles en el sistema.

diagnosis.py (modelo)
-Atributos principales:
- code: Código único del diagnóstico.
- name: Nombre del diagnóstico.
-Características adicionales:
- Implementa borrado lógico mediante un campo deleted_at (equivalente a SoftDeletes en Laravel).
diagnosis_view.py (vista/controlador)
-Gestiona todas las operaciones relacionadas con diagnósticos:
- Listado de diagnósticos
- Registro de nuevos diagnósticos
- Eliminación lógica

Pacientes (patients/)
Propósito: Administración de información personal, médica y de contacto de pacientes.

1. 01_Modelo_y_Recursos/
patient.py (modelo)
Atributos:

- Información personal: nombres, apellidos
- Contacto: teléfonos, correo electrónico
- Salud: condición médica
- Ubicación: región, provincia, distrito
- Documentación: tipo y número de documento

patient_serializer.py
- Serializador de pacientes (equivalente a PatientResource en Laravel)
- Se encarga de transformar los datos de paciente para ser consumidos por la API.

patient_serializer.py (colección personalizada)
- Django no necesita una colección como PatientCollection, pero se utiliza paginación personalizada con PageNumberPagination.

2. 02_Controlador/
patient_view.py
-Vista tipo ModelViewSet que gestiona:

- Registro de nuevos pacientes
- Actualización y eliminación
- Listado paginado de pacientes
- Búsqueda avanzada de pacientes (/search/)

3. 03_Servicios/
patient_service.py
-Implementa la lógica de negocio desacoplada del controlador, incluyendo:
- Obtención de todos los pacientes
- Paginación
- Búsqueda por múltiples términos
- Ordenamiento

4. 04_Request_Validaciones/
Propósito: Encapsular reglas de validación de datos, equivalente a Laravel Form Requests.

store_patient_validator.py
-Validaciones al registrar un nuevo paciente:

- Documento único
- Correo electrónico único
- Campos requeridos y opcionales

update_patient_validator.py
-Validaciones para actualizar un paciente:
- Reglas similares al registro, pero sin conflictos con el paciente actual

search_patients_validator.py
-Validaciones para búsqueda avanzada:
- Revisión de términos de búsqueda y filtros


Model (Modelo)
Patient Model: Modelo de paciente con información personal y médica (patient.py)
Diagnosis Model: Sistema de diagnósticos médicos (diagnosis.py)
PatientResource: Transformación de datos para API (patient_serializer.py)
PatientCollection: Colección personalizada de pacientes (pagination.py)

View (Vista/API)
Patient Controllers: Registro, actualización, búsqueda de pacientes (patient_view.py)
Diagnosis Controllers: Gestión de diagnósticos médicos (diagnosis_view.py)
API Routes: Configuración de rutas para pacientes y diagnósticos (urls/api_urls.py)
Search Implementation: Búsqueda avanzada de pacientes (patient_view.py + patient_service.py)

Controller (Lógica de Negocio)
Patient Services: Lógica de gestión de pacientes (patient_service.py)
Diagnosis Services: Lógica de gestión de diagnósticos (opcional, si se requiere lógica adicional)
Search Services: Servicios de búsqueda y filtrado (patient_service.py)
Validation Services: Validación de datos de pacientes (validators/)

core/
├── models/                              # Modelos de base de datos
│   ├── patient.py                       # Modelo de Paciente
│   └── diagnosis.py                     # Modelo de Diagnóstico
├── serializers/                         # Serializadores (equivalentes a recursos y colecciones)
│   ├── patient_serializer.py            # Transforma pacientes para la API (PatientResource)
│   └── diagnosis_serializer.py          # Transforma diagnósticos para la API
├── views/                               # Vistas API tipo ViewSet (equivalentes a controladores Laravel)
│   ├── patient_view.py                  # Gestión de endpoints de pacientes
│   └── diagnosis_view.py                # Gestión de endpoints de diagnósticos
├── services/                            # Lógica de negocio desacoplada (como servicios Laravel)
│   └── patient_service.py               # Lógica avanzada para búsquedas y filtrados
├── validators/                          # Validaciones de entrada personalizadas (como Form Requests)
│   ├── search_patients_validator.py     # Validaciones para búsquedas
│   ├── store_patient_validator.py       # Validaciones para registro de pacientes
│   └── update_patient_validator.py      # Validaciones para edición de pacientes
├── pagination/                          # Configuraciones de paginación para colecciones de la API
│   └── custom_pagination.py             # Equivalente a PatientCollection
├── urls/                                # Definición de rutas del API
│   └── api_urls.py                      # Enrutamiento para pacientes y diagnósticos

APIs a Desarrollar para React
Pacientes:
- GET /api/patients/ → Obtener lista de pacientes (paginada)
- POST /api/patients/ → Registrar nuevo paciente
- PUT /api/patients/{id}/ → Actualizar información de paciente
- DELETE /api/patients/{id}/ → Eliminar paciente
- GET /api/patients/search/ → Búsqueda avanzada con filtros

 Diagnósticos:
- GET /api/diagnoses/ → Listar todos los diagnósticos
- POST /api/diagnoses/ → Registrar nuevo diagnóstico

Tareas Específicas
1-Gestión de Pacientes:
- CRUD completo con validaciones y recursos personalizados
2-Sistema de Diagnósticos:
- Catálogo de diagnósticos con gestión básica
3-Búsqueda Avanzada:
- Filtros por nombres, apellidos, documento, condición médica, etc.
4-Validaciones:
- Reglas estrictas de unicidad y campos obligatorios
5-Documentación de APIs:
- Swagger o DRF-YASG para generar documentación interactiva
6-Testing:
- Pruebas unitarias para modelos, vistas y servicios

 Dependencias Clave
- Django ORM → Modelos y persistencia
- Django REST Framework → Serializadores, ViewSets, routers
- DRF Pagination → Listado paginado de pacientes
- Custom Services → Encapsular lógica de negocio
- Validators/Serializers → Validación de datos entrantes
- Soft Deletes (manual) → Campo deleted_at en modelos

Entregables Esperados
- CRUD completo de pacientes funcional y documentado
- Sistema de diagnóstico médico implementado
 -Búsqueda avanzada por múltiples criterios
- Validaciones robustas integradas
- Rutas y APIs bien documentadas
- Tests unitarios e integración
