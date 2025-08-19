from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name  # Esto hará que se vea como "Perú"

class Region(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    def __str__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

class DocumentType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Patient(models.Model):
    document_number = models.CharField(max_length=20)
    paternal_lastname = models.CharField(max_length=100)
    maternal_lastname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    personal_reference = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField()
    sex = models.CharField(max_length=10)
    primary_phone = models.CharField(max_length=20)
    secondary_phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    ocupation = models.CharField(max_length=100, blank=True, null=True)
    health_condition = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255)
   
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    document_type = models.ForeignKey(DocumentType, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
   
    def __str__(self):
        return f"{self.name} {self.paternal_lastname}"
# Create your models here.