from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name= 'login'),
    path('professionals/', views.professionals, name= 'professionals'),
    path('details/', views.userDetails, name= 'userDetails'),
    path('admin_edit_table/', views.admin_edit_table, name= 'admin_edit_table'),
    path('admin_view_tables/', views.admin_view_tables, name= 'admin_view_tables')
]