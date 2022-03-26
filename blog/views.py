from django.shortcuts import render
from .models import Post


def blog(request):
    """A view to render a list with all the blog posts"""
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'blog/all_posts.html', context)
