from django.contrib import admin
from .models import Payment, Order, OrderProduct


#___________________________________________________________  OrderProductInline
class OrderProductInline(admin.TabularInline):
    '''
    Inline admin class for displaying order product details.
    '''
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered')
    extra = 0


#___________________________________________________________  OrderAdmin
class OrderAdmin(admin.ModelAdmin):
    '''
    Admin class for managing orders in the Django admin interface.
    '''
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]


admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
