from ..models import PredeterminedPrice

def list_all():
    return PredeterminedPrice.objects.all()

def create(**kwargs):
    return PredeterminedPrice.objects.create(**kwargs)

def update(instance: PredeterminedPrice, **kwargs):
    for k,v in kwargs.items():
        setattr(instance, k, v)
    instance.save()
    return instance
