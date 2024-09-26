from django import forms
from .models import UserDetails

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['full_name', 'email', 'bio', 'location', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.TextInput(attrs={'class': 'form-control'}),
        }