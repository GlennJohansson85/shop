#_________________________________________________________________________  ORDERS/APPS.PY
from django.apps import AppConfig


#___________________________________________________________  CLASS ORDERSCONFIG
class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
