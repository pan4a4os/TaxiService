from django.apps import AppConfig


class HomeConfig(AppConfig):
    """Перевизначає модель AppConfig для представлення програми Django та її конфігурації."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "source.apps.home"
    verbose_name = "Home"
