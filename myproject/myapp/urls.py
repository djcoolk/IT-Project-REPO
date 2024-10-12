from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name= 'login'),
    path('register/', views.register, name= 'register'),
    path('professionals/', views.professionals, name= 'professionals'),
    path('details/', views.user_details, name= 'user_details'),
    path('admin_edit_table/', views.admin_edit_table, name= 'admin_edit_table'),
    path('admin_view_tables/', views.admin_view_tables, name= 'admin_view_tables'),
    path('admin_home/', views.admin_home, name= 'admin_home'),
    path('view_bookings/', views.view_bookings, name= 'view_bookings'),
    path('chatbot/', views.chatbot, name= 'chatbot'),
]