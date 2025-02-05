from django.apps import AppConfig



class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

#registering the signals created, for creating profile
#overriding builtin ready method.
    def ready(self):
        import users.signals