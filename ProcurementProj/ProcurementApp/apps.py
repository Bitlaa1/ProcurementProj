from django.apps import AppConfig


class ProcurementappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ProcurementApp'


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ProcurementApp'

    def ready(self):
        import ProcurementApp.signals
