from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """ Form to comment a blog post """
    class Meta:
        model = Comment

        fields = ('body',)

        labels = {
            'body': '',
        }

        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'comment__box',
                'placeholder': 'Write your comment here:',
            }),
        }
