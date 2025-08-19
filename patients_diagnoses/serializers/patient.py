from rest_framework import serializers
from ..models.patient import Patient,Region, Province, District, Country, DocumentType
from django.core.validators import RegexValidator
from datetime import date

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name']

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ['id', 'name']


class PatientSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    province = ProvinceSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    country = CountrySerializer(read_only=True)
    document_type = DocumentTypeSerializer(read_only=True)

    # Para escritura (crear con IDs)
    region_id = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all(), source='region', write_only=True)
    province_id = serializers.PrimaryKeyRelatedField(queryset=Province.objects.all(), source='province', write_only=True)
    district_id = serializers.PrimaryKeyRelatedField(queryset=District.objects.all(), source='district', write_only=True)
    country_id = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), source='country', write_only=True)
    document_type_id = serializers.PrimaryKeyRelatedField(queryset=DocumentType.objects.all(), source='document_type', write_only=True)

    # Validaciones campo por campo
    document_number = serializers.CharField(
        max_length=20,
        required=True,
        validators=[RegexValidator(r'^\d+$', 'Solo se permiten números.')]
    )
    paternal_lastname = serializers.CharField(required=True, max_length=100)
    maternal_lastname = serializers.CharField(required=True, max_length=100)
    name = serializers.CharField(required=True, max_length=100)
    birth_date = serializers.DateField(required=True)
    sex = serializers.ChoiceField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], required=True)
    primary_phone = serializers.CharField(max_length=20, required=True)
    email = serializers.EmailField(required=True)
    address = serializers.CharField(max_length=255, required=True)
    
    class Meta:
        model = Patient
        fields = [
            'id',
            'document_number',
            'paternal_lastname',
            'maternal_lastname',
            'name',
            'personal_reference',
            'birth_date',
            'sex',
            'primary_phone',
            'secondary_phone',
            'email',
            'ocupation',
            'health_condition',
            'address',
            'region',
            'province',
            'district',
            'country',
            'document_type',
            'region_id',
            'province_id',
            'district_id',
            'country_id',
            'document_type_id',
        ]
    # ✅ VALIDACIONES PERSONALIZADAS ABAJO

    def validate_document_number(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("El número de documento debe tener al menos 8 dígitos.")
        if not value.isdigit():
          raise serializers.ValidationError("El número de documento debe contener solo números.")
    
        qs = Patient.objects.filter(document_number=value)
        if self.instance:
          qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
         raise serializers.ValidationError("El número de documento ya está registrado.")
        return value

    def validate_email(self, value):
        if value:
            qs = Patient.objects.filter(email=value)
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError("El correo electrónico ya está registrado.")
        return value

    def validate(self, data):# esto puede eliminarse ya q no se requiere
        # Validación de campos obligatorios
        required_fields = [
            'document_number',
            'paternal_lastname',
            'name',
            'sex',
            'document_type'
        ]
        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError({field: "Este campo es obligatorio."})
        return data
    
    def validate_birth_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("La fecha de nacimiento no puede ser futura.")
        return value
    
    def validate_primary_phone(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("El teléfono principal debe tener al menos 6 caracteres.")
        return value
    
    