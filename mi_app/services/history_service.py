from ..models import History

def list_active():
    return History.active.all()

def create(**kwargs):
    return History.objects.create(**kwargs)

def update(instance: History, **kwargs):
    for k,v in kwargs.items():
        setattr(instance, k, v)
    instance.save()
    return instance

def soft_delete(instance: History):
    instance.soft_delete()
    return instance
