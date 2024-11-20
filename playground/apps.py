from django.apps import AppConfig

# Should have been called config ;)
# configurations for this specific app

class PlaygroundConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "playground"
