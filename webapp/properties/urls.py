from django.urls import path
from . import views

urlpatterns = [
    path('', views.properties, name='properties'),
    path('add', views.OfferCreateView.as_view(), name='offer_add'),
    path('<slug:slug>', views.OfferDetailView.as_view(), name='property_details')
]