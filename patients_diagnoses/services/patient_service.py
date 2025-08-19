from typing import Any, Dict, Optional, Tuple

from django.core.paginator import Paginator, EmptyPage
from django.db import transaction
from django.db.models import Q
from django.db.models.functions import Concat
from django.db.models import Value

from ..models.patient import Patient


class PatientService:
    """
    Servicio de pacientes inspirado en el PatientService de Laravel.

    Nota: Algunas capacidades del servicio original (soft delete, restore, history, appointments)
    no existen aún en los modelos actuales de Django. Este servicio implementa
    alternativas seguras con lo disponible ahora.
    """

    def get_all(self):
        return Patient.objects.all()

    def get_paginated(self, request):
        per_page_raw = request.GET.get("per_page", 20)
        page_raw = request.GET.get("page", 1)
        try:
            per_page = int(per_page_raw)
        except (TypeError, ValueError):
            per_page = 20
        try:
            page = int(page_raw)
        except (TypeError, ValueError):
            page = 1

        queryset = Patient.objects.all().order_by("-id")
        paginator = Paginator(queryset, per_page)
        try:
            page_obj = paginator.page(page)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        return page_obj

    def search_patients(self, params: Dict[str, Any]):
        per_page_raw = params.get("per_page", 30)
        search_term = (params.get("search") or params.get("q") or "").strip()

        try:
            per_page = int(per_page_raw)
        except (TypeError, ValueError):
            per_page = 30

        queryset = Patient.objects.all().order_by("-id")

        if search_term:
            # Búsqueda multi-campo similar a la de Laravel usando Q y concatenaciones
            queryset = queryset.annotate(
                paternal_name=Concat("paternal_lastname", Value(" "), "name"),
                full_name=Concat("name", Value(" "), "paternal_lastname", Value(" "), "maternal_lastname"),
                paternal_maternal_name=Concat(
                    "paternal_lastname", Value(" "), "maternal_lastname", Value(" "), "name"
                ),
            ).filter(
                Q(document_number__iexact=search_term)
                | Q(document_number__istartswith=search_term)
                | Q(name__istartswith=search_term)
                | Q(name__icontains=search_term)
                | Q(paternal_lastname__istartswith=search_term)
                | Q(paternal_lastname__icontains=search_term)
                | Q(maternal_lastname__istartswith=search_term)
                | Q(maternal_lastname__icontains=search_term)
                | Q(paternal_name__istartswith=search_term)
                | Q(full_name__istartswith=search_term)
                | Q(paternal_maternal_name__istartswith=search_term)
            )

        paginator = Paginator(queryset, per_page)
        page_obj = paginator.page(1)
        return page_obj

    @transaction.atomic
    def store_or_restore(self, data: Dict[str, Any]) -> Tuple[Patient, bool, bool]:
        """
        Crea un paciente si no existe. No hay soft-delete ni restore aún en el modelo,
        por lo que 'restored' siempre será False por ahora.

        Retorna (patient, created, restored)
        """
        # Intento de búsqueda por combinación de nombres como en Laravel
        existing = Patient.objects.filter(
            name=data.get("name"),
            paternal_lastname=data.get("paternal_lastname"),
            maternal_lastname=data.get("maternal_lastname"),
        ).first()

        if existing:
            return existing, False, False

        # Creación directa con los campos disponibles;
        # se asume que data ya viene validado por el serializer en la vista
        patient = Patient.objects.create(**data)
        return patient, True, False

    @transaction.atomic
    def update(self, patient: Patient, data: Dict[str, Any]) -> Patient:
        changed_fields = []
        for field, value in data.items():
            if not hasattr(patient, field):
                continue
            current = getattr(patient, field)
            if str(current) != str(value):
                setattr(patient, field, value)
                changed_fields.append(field)

        if changed_fields:
            patient.save(update_fields=changed_fields)
        return patient

    @transaction.atomic
    def destroy(self, patient: Patient) -> None:
        # Eliminación directa (no hay soft delete en el modelo Patient actual)
        patient.delete()



