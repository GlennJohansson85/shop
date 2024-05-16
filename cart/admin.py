from django.contrib import admin
from .models import Cart, CartItem


#___________________________________________________________  CartAdmin
class CartAdmin(admin.ModelAdmin):
    '''
    Custom admin configuration for the Cart model.
    '''
    list_display = ('cart_id', 'date_added')


#___________________________________________________________  CartItemAdmin
class CartItemAdmin(admin.ModelAdmin):
    '''
    Custom admin configuration for the CartItem model.
    '''
    list_display = ('product', 'cart', 'quantity', 'is_active')


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
