from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from products.models import Product
from blog.models import Post


def management_area(request):
    """ A view to return the management page """

    if request.user.is_staff or request.user.is_superuser:
        products = Product.objects.all()
        posts = Post.objects.all()

        context = {
            'products': products,
            'posts': posts
        }

        return render(request, 'management/management_area.html', context)

    else:
        messages.error(request, "You are not allowed in this area.")
        return redirect(reverse('home'))
