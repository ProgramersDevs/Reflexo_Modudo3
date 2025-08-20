from django.db import models
from django.utils import timezone

class DocumentType(models.Model):
    name = models.CharField(
        max_length=255,
        error_messages={'max_length': 'El nombre no debe superar los 255 caracteres.'}
    )
    description = models.TextField(
        blank=True, null=True,
        error_messages={'max_length': 'La descripción no debe superar los 1000 caracteres.'}
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save(update_fields=["deleted_at"])

    def restore(self):
        self.deleted_at = None
        self.save(update_fields=["deleted_at"])

    def __str__(self):
        return self.name

    class Meta:
        db_table = "document_types"
