from django.apps import AppConfig


class OrdersConfig(AppConfig):
    '''
    AppConfig class for the orders app.
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
