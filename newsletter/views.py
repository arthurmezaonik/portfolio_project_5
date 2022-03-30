from django.shortcuts import render, redirect, reverse, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import SigneUpForm


def newsletter_sign_up(request):
    """ View that handle the sign up form """

    if request.method == 'POST':
        form_data = {
            'email': request.POST['newsletter']
        }

        signe_up_form = SigneUpForm(form_data)
        if signe_up_form.is_valid():
            email = signe_up_form.save(commit=False)
            email.save()
            messages.success(request, 'Thanks for submit to our newsletter.')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Error submitting your email. \
                Did you register before?')
            return redirect(reverse('home'))
