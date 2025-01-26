from django import forms
from .models import Trainer

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'example@domain.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+1234567890'})
        }