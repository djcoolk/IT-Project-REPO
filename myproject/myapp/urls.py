from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import logout_view

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name= 'login'),
    path('register/', views.register, name= 'register'),
    path('logout/', logout_view, name='logout'),
    path('professionals/', views.professionals, name= 'professionals'),
    path('book-session/<int:counsellor_id>/', views.book_session, name= 'book_session'),
    path('set-availability/', views.set_availability, name= 'set_availability'),
    path('details/', views.user_details, name= 'user_details'),
    path('view-bookings/', views.view_bookings, name= 'view_bookings'),
    path('rebook/<int:counsellor_id>/', views.rebook, name='rebook'),
    path('chatbot/', views.chatbot_page, name='chatbot_page'),
    path('chatbot_response/', views.chatbot_response, name='chatbot_response'),
    path('video/', views.video_call, name= 'video_call'),
    path('counsellor-home/', views.counsellor_home, name= 'counsellor_home'),
    path('edit_availability/<int:availability_id>/', views.edit_availability, name='edit_availability'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)