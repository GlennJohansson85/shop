#_________________________________________________________________________  PRODUCTS/URLS.PY  -->
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<slug:category_slug>/', views.products, name='products_by_category'),
]



