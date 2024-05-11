#_________________________________________________________________________  PRODUCTS/VIEWS.PY  -->
from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from cart.models import CartItem
from django.db.models import Q

from django.http import HttpResponse

from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def products(request, category_slug=None):
    categories          = None
    products            = None

    if category_slug    != None:
        categories      = get_object_or_404(Category,slug=category_slug)
        products        = Product.objects.filter(category=categories, is_available=True)
        paginator       = Paginator(products, 3)
        page            = request.GET.get('page')
        paged_products  = paginator.get_page(page)
        product_count   = products.count()
    else: 
        products        = Product.objects.all().filter(is_available=True).order_by('id')
        paginator       = Paginator(products, 3)
        page            = request.GET.get('page')
        paged_products  = paginator.get_page(page)
        product_count   = products.count()

    context = {
        'products'      : paged_products,
        'product_count' : product_count,
    }
    return render(request,'products/products.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product  = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart         = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
        'in_cart'       : in_cart,
    }
    return render(request, 'products/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET: # If keyword = True
        keyword = request.GET['keyword'] # Store it in keyword variable 
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': products.count,
    }
    return render(request, 'products/products.html', context)