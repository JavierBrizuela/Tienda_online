from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .form import RegisterForm

# Create your views here.

def login_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('index')
        else:
            messages.warning(request, 'su usuario o contraseña no coinciden')
    return render(request, 'users/login.html', {})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login')

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        firstname = form.cleaned_data.get('firstname')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password)
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado correctamente')
            return redirect('index')

    return render(request, 'users/register.html', {'form':form})