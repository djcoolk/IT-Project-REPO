from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .utils import *
# global variables
logged_in_user = None
def login(request): # User enters username and password and is validated and logged in

    context = {}
    form = loginForm()
    context['form'] = form

    if request.method == 'POST':

        form_login = loginForm(request.POST)

        if form_login.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            if User.login(username, password) is not None:
                logged_in_user = User.login(username, password)
                context['logged_in_user'] = logged_in_user
                return render(request, 'myapp/home.html',context)
            else:
                return render(request, 'myapp/login.html',context)
        else:
            return render(request, 'myapp/login.html', context)

    else:
        return render(request, 'myapp/login.html',context)

def register(request): # user will create a new account if they dont have one

    context = {}
    form = registerForm()
    context['form'] = form

    if request.method == 'POST':
        form_register =registerForm(request.POST)
        if form_register.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            User.register(email,username, password)
            return render(request, 'myapp/home.html',context)
        else:
            return render(request, 'myapp/register.html', context)
    else:
        return render(request, 'myapp/register.html', context)

def user_details(request): # process data from the user and save to database

    form = SaveUserDetails()
    context ={}
    context['form'] = form

    return render(request, 'myapp/user_details.html', context)

def home(request):
    context = {}
    if logged_in_user is not None:
        context['logged_in_user'] = logged_in_user
    return render(request, 'myapp/home.html', context)

def professionals(request):
    return render(request, 'myapp/professionals.html')

def admin_home(request):
    return render(request, 'myapp/admin_home.html')

def admin_view_tables(request):
    return render(request, 'myapp/admin_view_tables.html')

def admin_edit_table(request):
    return render(request, 'myapp/admin_edit_table.html')

def chatbot(request):
    return render(request, 'myapp/chatbot.html')

def view_bookings(request):
    return render(request, 'myapp/view_bookings.html')


