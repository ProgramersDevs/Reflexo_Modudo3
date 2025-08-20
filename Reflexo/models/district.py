from django.db import models
from django.utils import timezone
from .province import Province  # <-- este import es clave


class District(models.Model):
    name = models.CharField(max_length=255, default="Sin nombre")
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name="districts"  # este es el nombre para acceder desde Province
    )
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    # Campos temporales que se agregarán después de la migración
    ubigeo_code = models.CharField(max_length=6, unique=True, null=True, blank=True, help_text="Código de ubigeo de 6 dígitos")
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
        verbose_name = "Distrito"
        verbose_name_plural = "Distritos"


class DistrictUser(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.name


class DistrictPatient(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='patients')

    def __str__(self):
        return self.name
    

class DistrictTherapist(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='therapists')

    def __str__(self):
        return self.name
