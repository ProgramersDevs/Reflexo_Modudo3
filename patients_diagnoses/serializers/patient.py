from rest_framework import serializers
from ..models.patient import Patient
from Reflexo.serializers.region_serializer import RegionSerializer
from Reflexo.serializers.province_serializer import ProvinceSerializer
from Reflexo.serializers.district_serializer import DistrictSerializer
from Reflexo.serializers.country_serializer import CountrySerializer
from mi_app.serializers.document_type import DocumentTypeSerializer
from django.core.validators import RegexValidator
from datetime import date
import re




class PatientSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    province = ProvinceSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    country = CountrySerializer(read_only=True)
    document_type = DocumentTypeSerializer(read_only=True)

    # Para escritura (crear con IDs)
    region_id = serializers.PrimaryKeyRelatedField(queryset=RegionSerializer.Meta.model.objects.all(), source='region', write_only=True)
    province_id = serializers.PrimaryKeyRelatedField(queryset=ProvinceSerializer.Meta.model.objects.all(), source='province', write_only=True)
    district_id = serializers.PrimaryKeyRelatedField(queryset=DistrictSerializer.Meta.model.objects.all(), source='district', write_only=True)
    country_id = serializers.PrimaryKeyRelatedField(queryset=CountrySerializer.Meta.model.objects.all(), source='country', write_only=True)
    document_type_id = serializers.PrimaryKeyRelatedField(queryset=DocumentTypeSerializer.Meta.model.objects.all(), source='document_type', write_only=True)

    # Validaciones campo por campo
    document_number = serializers.CharField(max_length=20, required=True)
    paternal_lastname = serializers.CharField(required=True, max_length=100)
    maternal_lastname = serializers.CharField(required=True, max_length=100)
    name = serializers.CharField(required=True, max_length=100)
    birth_date = serializers.DateField(required=True)
    sex = serializers.ChoiceField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], required=True)
    primary_phone = serializers.CharField(max_length=15, required=True)
    secondary_phone = serializers.CharField(max_length=15, required=False, allow_blank=True, allow_null=True)
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
        # Mensajes de error personalizados en español
        extra_kwargs = {
            'document_number': {
                'error_messages': {
                    'required': 'El número de documento es obligatorio.',
                    'max_length': 'El número de documento no debe exceder los 20 caracteres.',
                    'blank': 'El número de documento no puede estar vacío.'
                }
            },
            'paternal_lastname': {
                'error_messages': {
                    'required': 'El apellido paterno es obligatorio.',
                    'max_length': 'El apellido paterno no debe exceder los 100 caracteres.',
                    'blank': 'El apellido paterno no puede estar vacío.'
                }
            },
            'maternal_lastname': {
                'error_messages': {
                    'required': 'El apellido materno es obligatorio.',
                    'max_length': 'El apellido materno no debe exceder los 100 caracteres.',
                    'blank': 'El apellido materno no puede estar vacío.'
                }
            },
            'name': {
                'error_messages': {
                    'required': 'El nombre es obligatorio.',
                    'max_length': 'El nombre no debe exceder los 100 caracteres.',
                    'blank': 'El nombre no puede estar vacío.'
                }
            },
            'birth_date': {
                'error_messages': {
                    'required': 'La fecha de nacimiento es obligatoria.',
                    'invalid': 'La fecha de nacimiento debe tener un formato válido (YYYY-MM-DD).'
                }
            },
            'sex': {
                'error_messages': {
                    'required': 'El sexo es obligatorio.',
                    'invalid_choice': 'Seleccione una opción válida. Las opciones son Masculino o Femenino.'
                }
            },
            'primary_phone': {
                'error_messages': {
                    'required': 'El teléfono principal es obligatorio.',
                    'max_length': 'El teléfono principal no debe exceder los 15 caracteres.',
                    'blank': 'El teléfono principal no puede estar vacío.'
                }
            },
            'secondary_phone': {
                'error_messages': {
                    'max_length': 'El teléfono secundario no debe exceder los 15 caracteres.'
                }
            },
            'email': {
                'error_messages': {
                    'required': 'El correo electrónico es obligatorio.',
                    'invalid': 'Ingrese un correo electrónico válido.',
                    'blank': 'El correo electrónico no puede estar vacío.'
                }
            },
            'address': {
                'error_messages': {
                    'required': 'La dirección es obligatoria.',
                    'max_length': 'La dirección no debe exceder los 255 caracteres.',
                    'blank': 'La dirección no puede estar vacía.'
                }
            },
            'region_id': {
                'error_messages': {
                    'required': 'La región es obligatoria.',
                    'does_not_exist': 'La región seleccionada no existe.',
                    'null': 'Debe seleccionar una región.'
                }
            },
            'province_id': {
                'error_messages': {
                    'required': 'La provincia es obligatoria.',
                    'does_not_exist': 'La provincia seleccionada no existe.',
                    'null': 'Debe seleccionar una provincia.'
                }
            },
            'district_id': {
                'error_messages': {
                    'required': 'El distrito es obligatorio.',
                    'does_not_exist': 'El distrito seleccionado no existe.',
                    'null': 'Debe seleccionar un distrito.'
                }
            },
            'country_id': {
                'error_messages': {
                    'required': 'El país es obligatorio.',
                    'does_not_exist': 'El país seleccionado no existe.',
                    'null': 'Debe seleccionar un país.'
                }
            },
            'document_type_id': {
                'error_messages': {
                    'required': 'El tipo de documento es obligatorio.',
                    'does_not_exist': 'El tipo de documento seleccionado no existe.',
                    'null': 'Debe seleccionar un tipo de documento.'
                }
            }
        }

    # ✅ VALIDACIONES PERSONALIZADAS ABAJO

    def validate_document_number(self, value):
        document_type = self.initial_data.get('document_type_id')
        if not document_type:
            # Si no hay document_type_id en los datos iniciales, intentamos obtenerlo del contexto
            if self.instance and hasattr(self.instance, 'document_type'):
                document_type = self.instance.document_type.id
        
        if document_type:
            # Validaciones específicas según el tipo de documento
            document_type_name = None
            try:
                # Intentamos obtener el nombre del tipo de documento
                from mi_app.models import DocumentType
                document_type_obj = DocumentType.objects.get(id=document_type)
                document_type_name = document_type_obj.name
            except Exception:
                pass
            
            # DNI: 8 dígitos numéricos
            if document_type_name == 'DNI':
                if not re.match(r'^\d{8}$', value):
                    raise serializers.ValidationError("El DNI debe tener exactamente 8 dígitos numéricos.")
            
            # Pasaporte: 6-12 caracteres alfanuméricos
            elif document_type_name == 'PASAPORTE':
                if not re.match(r'^[a-zA-Z0-9]{6,12}$', value):
                    raise serializers.ValidationError("El Pasaporte debe tener entre 6 y 12 caracteres alfanuméricos.")
            
            # Carnet de Extranjería: 9-12 caracteres alfanuméricos
            elif document_type_name == 'CE':
                if not re.match(r'^[a-zA-Z0-9]{9,12}$', value):
                    raise serializers.ValidationError("El Carnet de Extranjería debe tener entre 9 y 12 caracteres alfanuméricos.")
            
            # RUC: 11 dígitos numéricos
            elif document_type_name == 'RUC':
                if not re.match(r'^\d{11}$', value):
                    raise serializers.ValidationError("El RUC debe tener exactamente 11 dígitos numéricos.")
            
            # Carnet de Salud: 10 dígitos numéricos
            elif document_type_name == 'CARNET DE SALUD':
                if not re.match(r'^\d{10}$', value):
                    raise serializers.ValidationError("El Carnet de Salud debe tener exactamente 10 dígitos numéricos.")
        
        # Verificar unicidad
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

    def validate(self, data):
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
        if len(value) > 15:
            raise serializers.ValidationError("El teléfono principal no debe exceder los 15 caracteres.")
        return value
    
    def validate_secondary_phone(self, value):
        if value and len(value) < 6:
            raise serializers.ValidationError("El teléfono secundario debe tener al menos 6 caracteres.")
        if value and len(value) > 15:
            raise serializers.ValidationError("El teléfono secundario no debe exceder los 15 caracteres.")
        return value


class PatientListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listar pacientes."""
    
    full_name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    region_name = serializers.CharField(source='region.name', read_only=True)
    document_type_name = serializers.CharField(source='document_type.name', read_only=True)
    
    class Meta:
        model = Patient
        fields = [
            'id', 'document_number', 'full_name', 'age', 'sex',
            'primary_phone', 'email', 'region_name', 'document_type_name',
            'created_at'
        ]
    
    def get_full_name(self, obj):
        return obj.get_full_name()
    
    def get_age(self, obj):
        from datetime import date
        today = date.today()
        return today.year - obj.birth_date.year - ((today.month, today.day) < (obj.birth_date.month, obj.birth_date.day))