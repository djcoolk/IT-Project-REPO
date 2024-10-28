from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import loginForm, SaveUserDetails, registerForm

User = get_user_model()

def home(request):
    if request.user.is_authenticated:
        context = {
            'logged_in_user': request.user,  # Use the logged-in user from the request
        }
        return render(request, 'home.html', context)
    else:
        return redirect('login')

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)  # Log the user in
                messages.success(request, 'log in succesfull.')
                return redirect('home')  # Redirect to home after successful login
            else:
                # error message
                form.add_error(None, 'Invalid username or password')
    else:
        form = loginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered.')
                return redirect('register')
            else:
                user = User.objects.create_user(email=email, password=password)
                auth_login(request, user) # Log the user in after registration
                if role == False: # Check if user is therapist
                    default_role = role.objects.get(id=1)
                    user.role = default_role
                else:
                    therapist_role = role.objects.get(id=2) #assign therapist role
                    user.role = therapist_role
                messages.success(request, 'Registration successful.')
                return redirect('home')  # Redirect to home after successful registration
    else:
        form = registerForm()
    return render(request, 'register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def user_details(request):
    form = SaveUserDetails(instance=request.user)  # Pass the logged-in user's instance

    if request.method == 'POST':
        form = SaveUserDetails(request.POST, request.FILES, instance=request.user)  # Update the instance
        if form.is_valid():
            form.save()  # Save the updated user details
            return redirect('home')  # Redirect after saving

    context = {
        'form': form
    }
    return render(request, 'user_details.html', context)

@login_required
def video_call(request):
    return render(request, 'video_call.html')

@login_required
def professionals(request):
    return render(request, 'professionals.html')

@login_required
def admin_home(request):
    return render(request, 'admin_home.html')

@login_required
def admin_view_tables(request):
    return render(request, 'admin_view_tables.html')

@login_required
def admin_edit_table(request):
    return render(request, 'admin_edit_table.html')

@login_required
def chatbot(request):
    return render(request, 'chatbot.html')

@login_required
def view_bookings(request):
    return render(request, 'view_bookings.html')
