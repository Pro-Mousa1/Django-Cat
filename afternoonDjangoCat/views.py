from django.shortcuts import render, redirect
from .forms import UserRegForm
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def events(request):
    return render(request, 'events.html')


def trainers(request):
    return render(request, 'trainers.html')


def register(request):
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, f'Account created for {username}')
            return redirect('my-register')
    else:
        form = UserRegForm()
    return render(request, 'register.html', {'form': form})
