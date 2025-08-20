from ..models import DocumentType

def list_active():
    return DocumentType.objects.filter(deleted_at__isnull=True)

def create(**kwargs):
    return DocumentType.objects.create(**kwargs)

def update(instance: DocumentType, **kwargs):
    for k,v in kwargs.items():
        setattr(instance, k, v)
    instance.save()
    return instance

def soft_delete(instance: DocumentType):
    instance.soft_delete()
    return instance
