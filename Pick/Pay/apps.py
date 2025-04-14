from django.apps import AppConfig


class PayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Pay'

    def ready(self):
        import Pay.signals
