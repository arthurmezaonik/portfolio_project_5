from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404 # noqa
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view that renders the bag page """

    return render(request, 'bag/bag.html')


def add_bag(request, item_id):
    """ Add a quantity of the product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request,
            f'Updated {product.title} quantity to {bag[item_id]}'
        )
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.title} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of an item on the bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated {product.title} quantity to {bag[item_id]}'
        )
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.title} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove an item from the bag """
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {product.title} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)