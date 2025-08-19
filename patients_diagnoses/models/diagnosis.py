from django.db import models

#from patients.models import Patient#


class Diagnosis(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    
    #patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='diagnoses')#
    #created_at = models.DateTimeField(auto_now_add=True)#
    
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def soft_delete(self):
        from django.utils import timezone
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.code} - {self.name}"