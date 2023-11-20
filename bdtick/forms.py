from .models import Products
from django.forms import ModelForm, TextInput, Textarea


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['title', 'names', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название продукта'
            }),
            'names': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название наименования'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация'
            })
        }
