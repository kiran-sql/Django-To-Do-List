from django import forms
from .models import ToDO


class TodoForm(forms.ModelForm):
    task = forms.CharField(max_length = 200, widget=forms.TextInput(
            attrs={
                "placeholder":"Enter a Task",
            }
    ))
    class Meta:
        model = ToDO
        fields= '__all__'