from django.shortcuts import render
from .models import UserDetails

def user_details(request):
    return render(request, 'myapp/userDetails.html')

def home(request):
    return render(request, 'myapp/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        # if username in UserDetails.username[1]:
        #     return render(request, 'myapp/home.html')
        # else:
        #     return render(request, 'myapp/login.html')
    else:
        return render(request, 'myapp/login.html')


def professionals(request):
    return render(request, 'myapp/professionals.html')

def userDetails(request):
    return render(request, 'myapp/userDetails.html')

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


