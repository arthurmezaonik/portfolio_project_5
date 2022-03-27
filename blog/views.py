from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models.functions import Lower
from .models import Post, Comment
from .forms import CommentForm


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
    commented = False
    comments = Comment.objects.filter(post=post.id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(
                f'{slug}?commented=True'
            )
    else:
        comment_form = CommentForm()
        if "commented" in request.GET:
            commented = True

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'commented': commented
    }

    return render(request, 'blog/specific_post.html', context)
