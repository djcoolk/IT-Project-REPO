from django.urls import path
from . import views
from .views import moodquiz, submit_mood_entry

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('homescreen/', views.homescreen, name='homescreen'),
    path('moodquiz/', views.moodquiz, name='moodquiz'),
    path('submit_mood_entry/', submit_mood_entry, name='submit_mood_entry'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('professionals/', views.professionals, name='professionals'),
    path('details/', views.user_details, name='user_details'),
    path('admin_edit_table/', views.admin_edit_table, name='admin_edit_table'),
    path('admin_view_tables/', views.admin_view_tables, name='admin_view_tables'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('view_bookings/', views.view_bookings, name='view_bookings'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('video/', views.video_call, name='video_call')]