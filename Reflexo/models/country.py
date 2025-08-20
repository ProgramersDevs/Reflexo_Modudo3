from django.db import models
from django.utils import timezone

class Country(models.Model):
    name = models.CharField(max_length=100)
    ubigeo_code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, using=None, keep_parents=False):
        """Soft delete."""
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """Restaura un registro eliminado."""
        self.deleted_at = None
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'Reflexo'
        verbose_name = "País"
        verbose_name_plural = "Países"


class CountryUser(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='users')

    class Meta:
        app_label = 'Reflexo'


class CountryPatient(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='patients')

    class Meta:
        app_label = 'Reflexo'


class CountryTherapist(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='therapists')

    class Meta:
        app_label = 'Reflexo'
