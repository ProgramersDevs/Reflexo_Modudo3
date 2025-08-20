from django.db import models
from django.utils import timezone
from .document_type import DocumentType

class ActiveHistoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class History(models.Model):
    document_type = models.ForeignKey(DocumentType, on_delete=models.PROTECT, related_name="histories")
    document_number = models.CharField(max_length=50)

    testimony = models.TextField(blank=True, null=True)
    private_observation = models.TextField(blank=True, null=True)
    observation = models.TextField(blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    last_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()
    active = ActiveHistoryManager()

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save(update_fields=["deleted_at"])

    def restore(self):
        self.deleted_at = None
        self.save(update_fields=["deleted_at"])

    def __str__(self):
        return f"History for {self.document_type_id}-{self.document_number}"

    class Meta:
        db_table = "histories"
        constraints = [
            models.UniqueConstraint(
                fields=['document_type', 'document_number'],
                condition=models.Q(deleted_at__isnull=True),
                name='unique_active_history_by_document'
            )
        ]
