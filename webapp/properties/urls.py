from django.urls import path
from . import views

urlpatterns = [
    path('', views.properties, name='properties'),
    path('<slug:slug>', views.OfferDetailView.as_view(), name='property_details'),
]