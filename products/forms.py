from .models import Review, Product, Collection
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


class ProductForm(forms.ModelForm):
    """ Form to create a product """
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        collections = Collection.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in collections]

        self.fields['collection'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
