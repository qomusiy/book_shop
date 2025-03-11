from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Get the User object
            user.set_password(form.cleaned_data['password'])  # Set the password
            user.save()  # Save the User object to the database
            login(request, user) #Log the user in.
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('about')
    else:
        form = LoginForm()
    return render(request, template_name='login.html', context={'form':form})

def logout_user(request):
     logout(request)
     return redirect('login')
