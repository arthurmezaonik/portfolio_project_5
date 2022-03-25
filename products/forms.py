from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """ Form to review a product """
    class Meta:
        model = Review

        fields = ('body',)

        labels = {
            'body': '',
        }

        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'review__box',
                'placeholder': 'Write your review here:',
            }),
        }
