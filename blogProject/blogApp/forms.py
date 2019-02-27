from django import forms
from .models import Blog

# Model Form
class NewBlog(forms.ModelForm):
    class Meta():
        model = Blog
        fields = ['title', 'text']