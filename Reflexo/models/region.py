###
from django.db import models
from django.utils import timezone

class Region(models.Model):
    name = models.CharField(max_length=255)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    # Campos temporales que se agregarán después de la migración
    ubigeo_code = models.CharField(max_length=2, unique=True, null=True, blank=True, help_text="Código de ubigeo de 2 dígitos")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        """Soft delete."""
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """Restaura un registro eliminado."""
        self.deleted_at = None
        self.save()

    def __str__(self):
        if self.ubigeo_code:
            return f"{self.ubigeo_code} - {self.name}"
        return self.name

    class Meta:
        db_table = "region"
        verbose_name = "Región"
        verbose_name_plural = "Regiones"


class RegionUser(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='users')
    # otros campos...


class RegionPatient(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='patients')
    # otros campos...


class RegionTherapist(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='therapists')
    # otros campos...
