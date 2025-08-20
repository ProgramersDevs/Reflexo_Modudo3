from django.db import models
from django.utils import timezone

class MedicalRecord(models.Model):
    """Historial médico que relaciona pacientes con diagnósticos."""
    
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='medical_records')
    diagnosis = models.ForeignKey('Diagnosis', on_delete=models.CASCADE, related_name='medical_records')
    
    # Información del diagnóstico
    diagnosis_date = models.DateField()
    symptoms = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    
    # Estado del diagnóstico
    STATUS_CHOICES = [
        ('active', 'Activo'),
        ('resolved', 'Resuelto'),
        ('chronic', 'Crónico'),
        ('monitoring', 'En Monitoreo'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    
    # Campos de auditoría
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'medical_records'
        verbose_name = 'Historial Médico'
        verbose_name_plural = 'Historiales Médicos'
        ordering = ['-diagnosis_date', '-created_at']
        unique_together = ['patient', 'diagnosis', 'diagnosis_date']
    
    def soft_delete(self):
        """Soft delete del historial médico."""
        self.deleted_at = timezone.now()
        self.save()
    
    def restore(self):
        """Restaura un historial médico eliminado."""
        self.deleted_at = None
        self.save()
    
    def __str__(self):
        return f"{self.patient} - {self.diagnosis} ({self.diagnosis_date})"
