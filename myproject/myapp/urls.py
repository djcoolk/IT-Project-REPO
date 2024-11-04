from django.urls import path
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
    path('chatbot/', views.chatbot, name= 'chatbot'),
    path('video/', views.video_call, name= 'video_call')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)