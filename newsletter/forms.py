from .models import SigneUp
from django import forms


class SigneUpForm(forms.ModelForm):
    """ Form to sign up for the newsletter """
    class Meta:
        model = SigneUp

        fields = ('email',)
