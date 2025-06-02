# Plik do definiowania widoków, które są renderowane za pomocą szablonizatora Jinja oraz wyświetlane w przeglądarce

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def interior(request):
    return render(request, 'main/interior.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')  # Redirect logged-in registration

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully!')
            login(request, user)  # Auto-login after registration
            return redirect('/')  # Redirect to home or dashboard
    else:
        form = UserCreationForm()

    return render(request, 'main/registration/register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/')