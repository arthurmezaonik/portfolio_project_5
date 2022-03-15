from django.shortcuts import render, get_object_or_404
from .models import Product, Collection

# Create your views here.
def all_products(request):
    """A view to render a list with all the products"""

    products = Product.objects.all()
    collection = None

    if request.GET:
        if "collection" in request.GET:
            requested_collection = request.GET["collection"]
            products = products.filter(collections__name=requested_collection)
            collection = Collection.objects.filter(name=requested_collection)[0]

    context = {
        'products': products,
        'collection': collection,
    }

    return render(request, 'products/products.html', context)


def specific_product(request, product_id):
    """A view to render a specific product"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/specific_product.html', context)
