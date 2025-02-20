from django.apps import AppConfig


class SaleFunctionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "function.sale_function"

    def ready(self):
        import function.sale_function.signals