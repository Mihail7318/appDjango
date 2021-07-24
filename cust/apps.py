from django.apps import AppConfig


class CustConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cust'
    verbose_name = 'Настройка'
    verbose_name_plural = 'Настройки'