from .models import Comment, Post
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


class PostForm(forms.ModelForm):
    """ Form to create a blog post """
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'content', 'featured_image', 'status')
