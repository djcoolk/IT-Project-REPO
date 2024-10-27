from django import forms
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()

class loginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50)
    password= forms.CharField(label='password', widget=forms.PasswordInput, max_length=50)

class registerForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=50)

class SaveUserDetails(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'bio', 'location', 'profile_picture', 'is_verified']
        widgets = {
            'First Name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'bio': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Enter your bio...'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email...'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'user_id': forms.TextInput(attrs={'class': 'form-control'}),
            'role_id': forms.TextInput(attrs={'class': 'form-control'}),
            'last_login': forms.TextInput(attrs={'class': 'form-control'}),
            'is_verified': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
# class createBookingForm(forms.ModelForm):
