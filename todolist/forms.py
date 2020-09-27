from django import forms
from django.forms import ModelForm
from . models import *

class TodolistForm(forms.ModelForm):
    class Meta():
        model=Todolist;
        fields='__all__'
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'What to do today?'}),
        }
