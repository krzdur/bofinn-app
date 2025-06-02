# Plik do zarządzania ścieżkami w aplikacji. Zawiera listę ścieżek powiązanych z widokami.

from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page (example)
    path('about/', views.about, name='about'),
    path('interior/', views.interior, name='interior'),
    path('register/', views.register, name='register_user'),
    path('login/', auth_views.LoginView.as_view(template_name='main/registration/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', include('django.contrib.auth.urls'))
]