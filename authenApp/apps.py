from django.apps import AppConfig


#class AuthenappConfig(AppConfig):
#    default_auto_field = 'django.db.models.BigAutoField'
#    name = 'authenApp'


class MyAppConfig(AppConfig):
    name = 'authenApp'

    def ready(self):
        # Code to run when the app is ready goes here
        # This could include importing signals or other things
        import authenApp.signals
