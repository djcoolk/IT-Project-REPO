from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from datetime import time, timedelta
from .models import *

User = get_user_model()

class login_form(forms.Form):
    email = forms.EmailField(label='Email', max_length=50)
    password= forms.CharField(label='password', widget=forms.PasswordInput, max_length=50)

class register_form(forms.Form):
    email = forms.EmailField(label='Email', max_length=50)
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        max_length=50
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput,
        max_length=50
    )
    role = forms.BooleanField(
        required=False,
        label="Register as a Counsellor",
        help_text="Select this if you are a counselor."
    )

    def clean_password2(self):
        # Get both password fields from cleaned_data
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        # Check if passwords match
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2



class user_details_form(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)

class register_counsellor_form(forms.Form):
    specialization = forms.CharField(label='Specialization', max_length=50)
    qualification = forms.CharField(label='Qualification', max_length=50)
    experience_years = forms.IntegerField(label='Years of experience', initial=0, max_value=50)
    bio = forms.CharField(label='Tell us more about you', widget=forms.Textarea, required=False)

class extra_details_form(forms.Form):
    profile_picture = forms.ImageField(required=False)
    location = forms.CharField(label='Location', max_length=50,required=False)
    bio = forms.CharField(label='Bio', max_length=500,required=False)

class counsellor_availability_form(forms.ModelForm):
    class Meta:
        model = CounsellorAvailability
        fields = ['date', 'start_time', 'duration']

    TIME_CHOICES = [
        ('09:00', "09:00"),
        ('12:00', "12:00"),
        ('15:00', "15:00"),
        ('18:00', "18:00"),
    ]
    DURATION_CHOICES = [
        ('00:30:00', "30 minutes"),
        ('01:00:00', "1 hour"),
        ('01:30:00', "1 hour 30 minutes"),
        ('02:00:00', "2 hours"),
        ('02:30:00', "2 hours 30 minutes"),
        ('03:00:00', "3 hours"),
    ]

    start_time = forms.ChoiceField(choices=TIME_CHOICES)
    duration = forms.TypedChoiceField(
        choices=DURATION_CHOICES,
        coerce=lambda x: timedelta(
            hours=int(x.split(':')[0]),
            minutes=int(x.split(':')[1]),
            seconds=int(x.split(':')[2])
        )
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Date"
    )

class SaveUserDetails(forms.ModelForm):
    class Meta:
        model = User
        model = User
        fields = ['first_name', 'last_name', 'email', 'bio', 'location', 'profile_picture']  # Use the correct field names
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'bio': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Enter your bio...'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email...'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

