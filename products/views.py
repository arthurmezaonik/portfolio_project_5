from django.shortcuts import render
from .models import Product


# Create your views here.
def all_products(request):
    """
    A view to render a list with all the products
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)