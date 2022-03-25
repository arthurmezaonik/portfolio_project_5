from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Product, Collection, Review
from .forms import ReviewForm
from django.db.models.functions import Lower


# Create your views here.
def all_products(request):
    """A view to render a list with all the products"""

    products = Product.objects.all()
    collection = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('title'))
            if sortkey == 'collection':
                sortkey = 'collection__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if "collection" in request.GET:
            requested_collection = request.GET["collection"]
            products = products.filter(collection__name=requested_collection)
            collection = Collection.objects.filter(
                name=requested_collection
            )[0]

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'collection': collection,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def specific_product(request, product_id):
    """A view to render a specific product"""

    product = get_object_or_404(Product, pk=product_id)
    reviewed = False
    reviews = Review.objects.filter(product=product_id)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.product = product
            review.save()

            return HttpResponseRedirect(
                f'{product_id}?reviewed=True'
            )
    else:
        review_form = ReviewForm()
        if "reviewed" in request.GET:
            reviewed = True

    context = {
        'product': product,
        'reviews': reviews,
        'review_form': review_form,
        'reviewed': reviewed
    }

    return render(request, 'products/specific_product.html', context)
