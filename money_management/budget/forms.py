from django import forms
from .models import UserCategory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = UserCategory
        fields = ['category', 'user']


