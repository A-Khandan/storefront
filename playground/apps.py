from django.apps import AppConfig

# Should have been called config ;)

class PlaygroundConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "playground"
