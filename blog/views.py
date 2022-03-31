from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models.functions import Lower
from .models import Post, Comment
from .forms import CommentForm, PostForm


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


def specific_post(request, post_id):
    """A view to render a specific blog post"""
    post = get_object_or_404(Post, pk=post_id)
    commented = False
    comments = Comment.objects.filter(post=post.id)

    if request.method == 'POST':
        try:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment_form.instance.email = request.user.email
                comment_form.instance.name = request.user.username
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()

                messages.success(request, 'Comment submitted')
                return HttpResponseRedirect(
                    f'{post_id}?commented=True'
                )
        except Exception as e:
            messages.error(request, f'Error submitting your comment: {e}')
            return HttpResponse(status=500)

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


def create_post(request):
    """Create a new post"""

    if request.user.is_staff or request.user.is_superuser:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request, 'Post created successfully!')
                return redirect(reverse('create_post'))
        else:
            form = PostForm()

        context = {
            'form': form,
        }
        return render(request, 'blog/create_post.html', context)

    else:
        messages.error(request, "You are not allowed in this area.")
        return redirect(reverse('home'))


def edit_post(request, post_id):
    """Edit a post"""

    if request.user.is_staff or request.user.is_superuser:

        post = get_object_or_404(Post, pk=post_id)

        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                messages.success(request, 'Post edited successfully!')
                return redirect(reverse('post', args=[post.id]))
            else:
                messages.error(request, 'Failed to update the post.')

        else:
            form = PostForm(instance=post)

        context = {
            'form': form,
            'post': post
        }
        return render(request, 'blog/edit_post.html', context)

    else:
        messages.error(request, "You are not allowed in this area.")
        return redirect(reverse('home'))


def delete_post(request, post_id):
    """ Delete a post from the store """

    if request.user.is_staff or request.user.is_superuser:
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        messages.success(request, 'Post deleted!')
        return redirect(reverse('blog'))

    else:
        messages.error(request, "You are not allowed in this area.")
        return redirect(reverse('home'))
