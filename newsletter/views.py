from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import SigneUpForm


def newsletter_sign_up(request):
    """ View that handle the sign up form """

    if request.method == 'POST':
        cust_email = request.POST['newsletter']
        subject = render_to_string(
            'confirmation_emails/confirmation_email_subject.txt',
        )
        body = render_to_string(
            'confirmation_emails/confirmation_email_body.txt',
            {'contact_email': settings.DEFAULT_FROM_EMAIL}
        )

        form_data = {
            'email': request.POST['newsletter']
        }

        signe_up_form = SigneUpForm(form_data)
        if signe_up_form.is_valid():
            email = signe_up_form.save(commit=False)
            email.save()
            messages.success(request, 'Thanks for submit to our newsletter.')
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
            )
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Error submitting your email. \
                Did you register before?')
            return redirect(reverse('home'))
