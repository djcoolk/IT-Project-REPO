from django import forms
from .models import *

class loginForm(forms.Form):
    user_name = forms.CharField(label='username', max_length=50)
    pass_hash = forms.CharField(label='password', widget=forms.PasswordInput, max_length=50)

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = user_details
        fields = ['full_name', 'email', 'bio', 'location', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }