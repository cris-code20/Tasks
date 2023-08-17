from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields= ['title','descripcion']
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Write a title'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'Write a descripcion'})
        }
