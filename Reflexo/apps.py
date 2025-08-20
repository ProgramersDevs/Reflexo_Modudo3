from django.apps import AppConfig


class ReflexoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Reflexo'
    verbose_name = 'Reflexo Perú - Módulo de Ubigeo'
    
    def ready(self):
        """Método que se ejecuta cuando la aplicación está lista"""
        try:
            import Reflexo.signals  # noqa
        except ImportError:
            pass
