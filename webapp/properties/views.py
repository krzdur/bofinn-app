from django.shortcuts import render
from django.views.generic import DetailView

from .models import Offer

def properties(request):
    offers = Offer.objects.all().order_by('created_at')
    return render(request,
                  'properties.html',
                  {'properties': offers})

class OfferDetailView(DetailView):
    model = Offer
    template_name = 'property_details.html'
    context_object_name = 'property'