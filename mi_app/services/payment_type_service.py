from ..models import PaymentType

def list_active():
    return PaymentType.objects.filter(deleted_at__isnull=True)

def create(**kwargs):
    return PaymentType.objects.create(**kwargs)

def update(instance: PaymentType, **kwargs):
    for k,v in kwargs.items():
        setattr(instance, k, v)
    instance.save()
    return instance

def soft_delete(instance: PaymentType):
    instance.soft_delete()
    return instance
