from django.shortcuts import render, redirect, get_object_or_404
from .models import UserDetails
from .forms import UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def user_details(request):
    return render(request, 'myapp/userDetails.html')

def home(request):
    return render(request, 'myapp/home.html')

def login(request):
    return render(request, 'myapp/login.html')

def professionals(request):
    return render(request, 'myapp/professionals.html')

def userDetails(request):
    return render(request, 'myapp/userDetails.html')

def admin_view_tables(request):
    return render(request, 'myapp/admin_view_tables.html')

def admin_edit_table(request):
    return render(request, 'myapp/admin_edit_table.html')
