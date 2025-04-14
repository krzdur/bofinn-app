# Plik do definiowania widoków, które są renderowane za pomocą szablonizatora Jinja oraz wyświetlane w przeglądarce

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def contact(request):
    return render(request, 'main/contact.html')

def properties(request):
    return render(request, 'main/properties.html')

def about(request):
    return render(request, 'main/about.html')
