# Plik do zarządzania ścieżkami w aplikacji. Zawiera listę ścieżek powiązanych z widokami.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page (example)
    path('contact/', views.contact, name='contact'),  # Contact page
<<<<<<< HEAD
    path('properties/', views.properties, name='properties')
  # Properties page
]


=======
    path('properties/', views.properties, name='properties'),  # Properties page
    path('about/', views.about, name='about')
]
>>>>>>> b27142df4413c2b3d9b571ebc44c26e4fe660733
