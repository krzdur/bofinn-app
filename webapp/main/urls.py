# Plik do zarządzania ścieżkami w aplikacji. Zawiera listę ścieżek powiązanych z widokami.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('properties/', views.properties, name='properties'),  # Properties page
    path('about/', views.about, name='about')  # About page
]

