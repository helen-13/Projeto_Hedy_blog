from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

class UsersConfig(AppConfig):
    name = 'users'
    def ready(self):
        import users.signals