from django import forms
from .models import Testimony


class TestimonyForm(forms.ModelForm):

    class Meta:
        model = Testimony
        fields = ('full_name', 'phone_number', 'testimony_subject', 'email', 'testimony')
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'testimony_subject': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'email': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'testimony': forms.Textarea(attrs={
                'class': 'form-control',
                'maxlength': "700",
                'rows': "16"
            })
        }