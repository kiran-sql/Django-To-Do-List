from django import forms
from .models import ToDO


class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDO
        fields="__all__"