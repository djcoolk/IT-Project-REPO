from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .utils import *
# process data from the user and interact with database
def user_details(request):
    context = {}
    form = UserDetailsForm()
    context['form'] = form
    return render(request, 'myapp/user_details.html', context)

def home(request):
    return render(request, 'myapp/home.html')

def login(request): # User enters username and password and is validated and logged in
    context = {}
    form = loginForm()
    context['form'] = form
    if request.method == 'POST':
        form_login =loginForm(request.POST)
        if form_login.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user(username, password)
            return render(request, 'myapp/home.html',context)
        else:
            return render(request, 'myapp/login.html',context)
    else:
        return render(request, 'myapp/login.html',context)


def register(request): # user will create a new account if they dont have one
        return render(request, 'myapp/register.html')


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


