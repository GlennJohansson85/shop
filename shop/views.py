from django.shortcuts import render
from products.models import Product


def home(request):
      '''
      Renders the home page with a list of available products.
      Retrieves all products that are currently available and passes them 
      to the template for rendering.
      '''
      products = Product.objects.all().filter(is_available=True)

      context = {
            'products': products, 
      }
      return render(request, 'home.html', context)