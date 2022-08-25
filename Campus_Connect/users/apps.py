from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Users'

class BaseConfig(AppConfig):
    name='Users'
    def ready(self):
        import Users.signals