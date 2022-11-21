from .models import Blog
from django.forms import ModelForm, TextInput, Textarea


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter text'
            }),
        }
