from django.db import models
from django.utils import timezone
from .region import Region

class Province(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, related_name='provinces', on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    # Campos temporales que se agregarán después de la migración
    ubigeo_code = models.CharField(max_length=4, unique=True, null=True, blank=True, help_text="Código de ubigeo de 4 dígitos")
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
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"


class ProvinceUser(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='users')
    # otros campos...


class ProvincePatient(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='patients')
    # otros campos...


class ProvinceTherapist(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='therapists')
    # otros campos...


class ProvinceDistrict(models.Model):
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name="province_districts"  # nombre distinto
    )