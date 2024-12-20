from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wanderly.accounts'

    def ready(self):
        import wanderly.accounts.signals
