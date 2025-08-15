# **Módulo 03 – Gestión de Pacientes y Diagnósticos (Django)**

## **Objetivo General**
Gestionar de forma completa los pacientes y sus diagnósticos médicos, incluyendo registro, actualización, búsqueda avanzada y manejo de información médica básica, utilizando Django y Django REST Framework.

## **Meta**
Implementar arquitectura MVC adaptada a Django + APIs REST para React.

---

## **Diagnósticos (diagnoses/)**

**Propósito:** Gestión de los diagnósticos médicos disponibles en el sistema.

### **diagnosis.py (modelo)**
**Atributos principales:**
- **code:** Código único del diagnóstico.
- **name:** Nombre del diagnóstico.

**Características adicionales:**
- Implementa borrado lógico mediante un campo `deleted_at` (equivalente a SoftDeletes en Laravel).

### **diagnosis_view.py (vista/controlador)**
**Responsabilidades:**
- Listado de diagnósticos.
- Registro de nuevos diagnósticos.
- Eliminación lógica.

---

## **Pacientes (patients/)**

**Propósito:** Administración de información personal, médica y de contacto de pacientes.

### **01_Modelo_y_Recursos/**

#### **patient.py (modelo)**
**Atributos:**
- **Información personal:** nombres, apellidos.
- **Contacto:** teléfonos, correo electrónico.
- **Salud:** condición médica.
- **Ubicación:** región, provincia, distrito.
- **Documentación:** tipo y número de documento.

#### **patient_serializer.py**
- Serializador de pacientes (equivalente a `PatientResource` en Laravel).
- Transforma los datos de paciente para ser consumidos por la API.

#### **patient_serializer.py (colección personalizada)**
- Django no necesita una colección como `PatientCollection`, pero se utiliza paginación personalizada con `PageNumberPagination`.

---

### **02_Controlador/**

#### **patient_view.py**
**Responsabilidades:**
- Registro de nuevos pacientes.
- Actualización y eliminación.
- Listado paginado de pacientes.
- Búsqueda avanzada de pacientes (`/search/`).

---

### **03_Servicios/**

#### **patient_service.py**
**Lógica de negocio:**
- Obtención de todos los pacientes.
- Paginación.
- Búsqueda por múltiples términos.
- Ordenamiento.

---

### **04_Request_Validaciones/**
**Propósito:** Encapsular reglas de validación de datos (equivalente a Laravel Form Requests).

#### **store_patient_validator.py**
**Validaciones al registrar un nuevo paciente:**
- Documento único.
- Correo electrónico único.
- Campos requeridos y opcionales.

#### **update_patient_validator.py**
**Validaciones para actualizar un paciente:**
- Reglas similares al registro, pero sin conflictos con el paciente actual.

#### **search_patients_validator.py**
**Validaciones para búsqueda avanzada:**
- Revisión de términos de búsqueda y filtros.

---

## **Model (Modelo)**
- **Patient Model:** Modelo de paciente con información personal y médica (`patient.py`).
- **Diagnosis Model:** Sistema de diagnósticos médicos (`diagnosis.py`).
- **PatientResource:** Transformación de datos para API (`patient_serializer.py`).
- **PatientCollection:** Colección personalizada de pacientes (`pagination.py`).

---

## **View (Vista/API)**
- **Patient Controllers:** Registro, actualización, búsqueda de pacientes (`patient_view.py`).
- **Diagnosis Controllers:** Gestión de diagnósticos médicos (`diagnosis_view.py`).
- **API Routes:** Configuración de rutas para pacientes y diagnósticos (`urls/api_urls.py`).
- **Search Implementation:** Búsqueda avanzada de pacientes (`patient_view.py` + `patient_service.py`).

---

## **Controller (Lógica de Negocio)**
- **Patient Services:** Lógica de gestión de pacientes (`patient_service.py`).
- **Diagnosis Services:** Lógica de gestión de diagnósticos (opcional).
- **Search Services:** Servicios de búsqueda y filtrado (`patient_service.py`).
- **Validation Services:** Validación de datos de pacientes (`validators/`).

---

Estructura de carpetas propuesta

core/
├── models/                              
│   ├── patient.py                      
│   └── diagnosis.py                     
├── serializers/                         
│   ├── patient_serializer.py            
│   └── diagnosis_serializer.py          
├── views/                               
│   ├── patient_view.py                  
│   └── diagnosis_view.py                
├── services/                           
│   └── patient_service.py               
├── validators/                          
│   ├── search_patients_validator.py     
│   ├── store_patient_validator.py       
│   └── update_patient_validator.py      
├── pagination/                          
│   └── custom_pagination.py             
├── urls/                                
│   └── api_urls.py                     


---

## **APIs a Desarrollar para React**

### **Pacientes**
- **GET** `/api/patients/` → Obtener lista de pacientes (paginada).
- **POST** `/api/patients/` → Registrar nuevo paciente.
- **PUT** `/api/patients/{id}/` → Actualizar información de paciente.
- **DELETE** `/api/patients/{id}/` → Eliminar paciente.
- **GET** `/api/patients/search/` → Búsqueda avanzada con filtros.

### **Diagnósticos**
- **GET** `/api/diagnoses/` → Listar todos los diagnósticos.
- **POST** `/api/diagnoses/` → Registrar nuevo diagnóstico.
- **PUT** `/api/diagnoses/{id}/` → Actualizar información de diagnostico.
- **DELETE** `/api/diagnoses/{id}/` → Eliminar diagnostico.
- **GET** `/api/diagnoses/search/` → Búsqueda avanzada con filtros.

---

## **Tareas Específicas**
- Gestión de Pacientes: CRUD completo con validaciones y recursos personalizados.
- Sistema de Diagnósticos: Catálogo de diagnósticos con gestión básica.
- Búsqueda Avanzada: Filtros por nombres, apellidos, documento, condición médica, etc.
- Validaciones: Reglas estrictas de unicidad y campos obligatorios.
- Documentación de APIs: Swagger o DRF-YASG.
- Testing: Pruebas unitarias para modelos, vistas y servicios.

---

## **Dependencias Clave**
- Django ORM.
- Django REST Framework.
- DRF Pagination.
- Custom Services.
- Validators/Serializers.
- Soft Deletes (manual).

---
## **Instalacion y Uso
Sigue estos pasos para levantar el proyecto en tu entorno local.

### 1️⃣ Clonar el repositorio
git clone https://github.com/usuario/tu-proyecto.git
cd tu-proyecto
## **Crear entorno Virtual
python -m venv venv
venv\Scripts\activate
## **Instalar Dependencias necesarias
pip install -r requirements.txt

## **Levantar Servidor
python manage.py runserver

## **Entregables Esperados**
- CRUD completo de pacientes funcional y documentado.
- Sistema de diagnóstico médico implementado.
- Búsqueda avanzada por múltiples criterios.
- Validaciones robustas integradas.

- Rutas y APIs bien documentadas.
- Tests unitarios e integración.
