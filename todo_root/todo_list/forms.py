from django import forms
from .models import *


class TodoForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = ['name', 'content']#'__all__'
        widgets = {
                'name': forms.TextInput(attrs={'id': 'nametask', 'placeholder':'Name', 'name':'name'}),
                'content': forms.Textarea(attrs={'cols': 50, 'rows': 8, 'id': 'area', 'placeholder':'Content', 'name':'content'}),
            }