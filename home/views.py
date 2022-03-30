from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'index.html')


def error_404(request, exception):
    return render(request, '404.html')