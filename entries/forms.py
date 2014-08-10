from django import forms
from models import Entry


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        exclude = ['user', ]
        widgets = {
            'title': forms.TextInput(attrs={'autofocus':'autofocus', 'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'autofocus':'autofocus', 'class': 'form-control'}),
            'body': forms.Textarea(attrs={'autofocus':'autofocus', 'class': 'form-control'}),
        }
