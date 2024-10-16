from django import forms
from . import models

class loginForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password= forms.CharField(label='password', widget=forms.PasswordInput, max_length=50)

class registerForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    email = forms.EmailField(label='Email', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=50)

class SaveUserDetails(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['full_name', 'email', 'bio', 'location', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Enter your bio...'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email...'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name...'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }
# class createBookingForm(forms.ModelForm):
