from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models.functions import Lower
from .models import Product, Collection, Review
from .forms import ReviewForm, ProductForm


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
        try:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review_form.instance.email = request.user.email
                review_form.instance.name = request.user.username
                review = review_form.save(commit=False)
                review.product = product
                review.save()

                messages.success(request, 'Review submitted')
                return HttpResponseRedirect(
                    f'{product_id}?reviewed=True'
                )
        except Exception as e:
            messages.error(request, f'Error submitting your review: {e}')
            return HttpResponse(status=500)

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


def create_product(request):
    """Create a new product"""

    if request.user.is_staff or request.user.is_superuser:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.save()
                messages.success(request, 'Product created successfully!')
                return redirect(reverse('create_product'))
        else:
            form = ProductForm()

        context = {
            'form': form,
        }
        return render(request, 'products/create_product.html', context)

    else:
        messages.error(request, "You are not allowed in this area.")
        return redirect(reverse('home'))


def edit_product(request, product_id):
    """Edit a product"""

    if request.user.is_staff or request.user.is_superuser:

        product = get_object_or_404(Product, pk=product_id)

        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                product = form.save(commit=False)
                product.save()
                messages.success(request, 'Product edited successfully!')
                return redirect(reverse('specific_product', args=[product.id]))
            else:
                messages.error(request, 'Failed to update the product.')

        else:
            form = ProductForm(instance=product)

        context = {
            'form': form,
            'product': product
        }
        return render(request, 'products/edit_product.html', context)

    else:
        messages.error(request, "You are not allowed in this area.")
        return redirect(reverse('home'))


def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
