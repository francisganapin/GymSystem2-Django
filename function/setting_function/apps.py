from django.apps import AppConfig


class SettingFunctionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "function.setting_function"

    def ready(self):
        import function.setting_function.signals