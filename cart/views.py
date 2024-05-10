#_________________________________________________________________________  CART/VIEWS.PY  -->
from django.shortcuts import render


def cart(request):
    return render(request, 'products/cart.html')
