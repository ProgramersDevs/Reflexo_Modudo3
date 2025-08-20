    
# Módulo 03 - Gestión de Pacientes y Diagnósticos 🏥

## **Responsabilidades**
Gestión completa de pacientes y sus diagnósticos médicos, incluyendo registro, actualización, búsqueda y manejo de información médica básica.

## **Meta: Lograr MVC con APIs para React**

## 1. Carpeta diagnoses/
Gestiona los diagnósticos médicos y contiene:

- Diagnosis.php : Modelo que representa los diagnósticos médicos con los siguientes atributos:
  
  - code : Código del diagnóstico
  - name : Nombre del diagnóstico
  - Implementa SoftDeletes para borrado lógico
- DiagnosisController.php : Controlador para gestionar las operaciones relacionadas con diagnósticos
## 2. Carpeta patients/
Gestiona la información de los pacientes y está organizada en subcarpetas:

### 2.1 01_Modelo_y_Recursos/
- Patient.php : Modelo principal que representa a los pacientes con atributos como:
  
  - Información personal (nombres, apellidos)
  - Datos de contacto (teléfonos, email)
  - Información médica (condición de salud)
  - Ubicación (región, provincia, distrito)
  - Documentación (tipo y número de documento)
- PatientCollection.php : Colección personalizada para pacientes
- PatientResource.php : Recurso para transformar datos de pacientes
### 2.2 02_Controlador/
- PatientController.php : Controlador que maneja las peticiones HTTP relacionadas con pacientes
### 2.3 03_Servicios/
- PatientService.php : Servicio que implementa la lógica de negocio para pacientes, incluyendo:
  - Obtención de todos los pacientes
  - Paginación de resultados
  - Búsqueda de pacientes por términos
  - Ordenamiento de resultados
### 2.4 04_Request_Validaciones/
Contiene las clases de validación para las solicitudes:

- SearchPatientsRequest.php : Validaciones para búsqueda de pacientes
- StorePatientRequest.php : Validaciones para crear nuevos pacientes, incluyendo:
  - Validación de documento único
  - Validación de correo electrónico único
  - Validación de campos requeridos y opcionales
- UpdatePatientRequest.php : Validaciones para actualizar pacientes existentes

### **Model (Modelo)**
- [ ] **Patient Model**: Modelo de paciente con información personal y médica
- [ ] **Diagnosis Model**: Sistema de diagnósticos médicos
- [ ] **PatientResource**: Transformación de datos para API
- [ ] **PatientCollection**: Colección personalizada de pacientes

### **View (Vista/API)**
- [ ] **Patient Controllers**: Registro, actualización, búsqueda de pacientes
- [ ] **Diagnosis Controllers**: Gestión de diagnósticos médicos
- [ ] **API Routes**: Configuración de rutas para pacientes y diagnósticos
- [ ] **Search Implementation**: Búsqueda avanzada de pacientes

### **Controller (Lógica de Negocio)**
- [ ] **Patient Services**: Lógica de gestión de pacientes
- [ ] **Diagnosis Services**: Lógica de gestión de diagnósticos
- [ ] **Search Services**: Servicios de búsqueda y filtrado
- [ ] **Validation Services**: Validación de datos de pacientes

## **Archivos Incluidos**
```
03_patients_diagnoses/
├── diagnoses/
│   ├── Diagnosis.php
│   └── DiagnosisController.php
└── patients/
    ├── 01_Modelo_y_Recursos/
    │   ├── Patient.php
    │   ├── PatientCollection.php
    │   └── PatientResource.php
    ├── 02_Controlador/
    │   └── PatientController.php
    ├── 03_Servicios/
    │   └── PatientService.php
    └── 04_Request_Validaciones/
        ├── SearchPatientsRequest.php
        ├── StorePatientRequest.php
        └── UpdatePatientRequest.php
```

## **APIs a Desarrollar para React**
- `GET /api/patients` - Obtener lista de pacientes
- `POST /api/patients` - Registrar nuevo paciente
- `PUT /api/patients/{id}` - Actualizar información de paciente
- `DELETE /api/patients/{id}` - Eliminar paciente
- `GET /api/patients/search` - Búsqueda avanzada de pacientes
- `GET /api/diagnoses` - Obtener lista de diagnósticos
- `POST /api/diagnoses` - Registrar nuevo diagnóstico

## **Tareas Específicas**
1. **Gestión de Pacientes**: Implementar CRUD completo
2. **Sistema de Diagnósticos**: Catalogación y gestión
3. **Búsqueda Avanzada**: Filtros y búsqueda por múltiples campos
4. **Validaciones**: Reglas de validación para datos de pacientes
5. **API Documentation**: Documentar todas las APIs
6. **Testing**: Tests unitarios y de integración

## **Dependencias**
- Laravel Eloquent para modelos
- Laravel Resource para transformación de datos
- Laravel Validation para requests
- Laravel Collections para manejo de datos

## **Entregables**
- [ ] CRUD de pacientes funcional
- [ ] Sistema de diagnósticos implementado
- [ ] Búsqueda avanzada funcionando
- [ ] Validaciones implementadas
- [ ] Documentación de APIs
- [ ] Tests completos
        