from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Lower
from .models import Post


def blog(request):
    """A view to render a list with all the blog posts"""
    posts = Post.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_name'
                posts = posts.annotate(lower_name=Lower('title'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            posts = posts.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'posts': posts,
        'current_sorting': current_sorting,
    }

    return render(request, 'blog/all_posts.html', context)


def specific_post(request, slug):
    """A view to render a specific blog post"""
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post
    }

    return render(request, 'blog/specific_post.html', context)
