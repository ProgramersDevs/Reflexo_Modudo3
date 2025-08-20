from django.db import models
from django.utils import timezone

class Diagnosis(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    # Campos de auditoría
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'diagnoses'
        verbose_name = 'Diagnóstico'
        verbose_name_plural = 'Diagnósticos'
        ordering = ['code']
    
    def soft_delete(self):
        """Soft delete del diagnóstico."""
        self.deleted_at = timezone.now()
        self.save()
    
    def restore(self):
        """Restaura un diagnóstico eliminado."""
        self.deleted_at = None
        self.save()

    def __str__(self):
        return f"{self.code} - {self.name}"