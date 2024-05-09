#_________________________________________________________________________  PRODUCTS/VIEWS.PY  -->
from django.shortcuts import render
from .models import Product


def products(request):
    products = Product.objects.all().filter(is_available=True)
    product_count = products.count() # Return no avavilable

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request,'products/products.html', context)
