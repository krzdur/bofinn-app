from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin

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


class OfferCreateView(LoginRequiredMixin, CreateView):
    model = Offer
    fields = ['name', 'beds_count', 'baths_count', 'area', 'price', 'image', 'description']
    template_name = 'offer_form.html'

    def form_valid(self, form):
        # Auto-generate slug from name
        form.instance.slug = slugify(form.instance.name)
        return super().form_valid(form)