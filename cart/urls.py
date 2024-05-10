#_________________________________________________________________________  CART/URLS.PY  -->
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
]