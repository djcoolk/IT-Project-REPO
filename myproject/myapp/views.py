from django.shortcuts import render, redirect, get_object_or_404
from .models import UserDetails
from .forms import UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def user_details(request):
    user_details = get_object_or_404(UserDetails, username=request.user.username)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_details)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('userDetails')
    else:
        form = UserProfileForm(instance=user_details)

    return render(request, 'myapp/userDetails.html', {'form': form, 'profile': user_details})


def home(request):
    return render(request, 'myapp/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

    return render(request, 'myapp/login.html')

def professionals(request):
    return render(request, 'myapp/professionals.html')

def userDetails(request):
    return render(request, 'myapp/userDetails.html')