from django.apps import AppConfig


class MemberFunctionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "function.member_function"

    def ready(self):
        import function.member_function.signals