from django.apps import AppConfig

#___________________________________________________________  CLASS CARTCONFIG
class CartConfig(AppConfig):
    '''
    Configuration class for the cart app.
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
