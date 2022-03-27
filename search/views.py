from django.shortcuts import render
from blog.models import Post
from products.models import Product


def search(request):
    """Return searched publications"""
    if request.method == "GET":
        searched = request.GET['q']
        products = Product.objects.filter(
            title__icontains=searched) | Product.objects.filter(
                description__icontains=searched
            )
        posts = Post.objects.filter(
            title__icontains=searched) | Post.objects.filter(
                content__icontains=searched
            )

        context = {
            'products': products,
            'posts': posts,
            'searched': searched
        }

        return render(request, 'search/search.html', context)
    else:
        return render(request, 'search/search.html')
