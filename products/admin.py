from django.contrib import admin
from .models import Product, Variation

#___________________________________________________________  ProductAdmin
class ProductAdmin(admin.ModelAdmin):
      '''
      Admin configuration for the Product model.
      '''
      list_display            = ('product_name',
                                 'price',
                                 'stock',
                                 'category',
                                 'modified_date',
                                 'is_available'
                                 )
      prepopulated_fields     = {'slug': ('product_name',)}


#___________________________________________________________  VariationAdmin
class VariationAdmin(admin.ModelAdmin):
      '''
      Admin configuration for the Variation model.
      '''
      list_display            = ('product',
                                 'variation_category',
                                 'variation_value',
                                 'is_active'
                                 )
      list_editable           = ('is_active',)
      list_filter             = ('product',
                                 'variation_category',
                                 'variation_value'
                                 )


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)