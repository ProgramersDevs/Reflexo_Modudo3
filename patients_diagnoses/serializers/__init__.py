from .patient import PatientSerializer, PatientListSerializer
from .diagnosis import DiagnosisSerializer, DiagnosisListSerializer
from .medical_record import MedicalRecordSerializer, MedicalRecordListSerializer

__all__ = [
    'PatientSerializer', 'PatientListSerializer',
    'DiagnosisSerializer', 'DiagnosisListSerializer',
    'MedicalRecordSerializer', 'MedicalRecordListSerializer'
]
