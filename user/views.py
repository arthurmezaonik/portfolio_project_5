from django.shortcuts import render


def profile(request):
    """ Display the user's profile. """

    template = 'user/user_area.html'
    context = {}

    return render(request, template, context)
