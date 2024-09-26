from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name= 'login'),
    path('professionals/', views.professionals, name= 'professionals'),
    path('details/', views.userDetails, name= 'userDetails')
]