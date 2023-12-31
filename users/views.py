from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from users.models import User
from django.contrib import messages
from .form import RegisterForm
from django.http import HttpResponseRedirect

# Create your views here.

def login_view(request):
    
    if request.user.is_authenticated:
        return redirect('product:index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])
            
            return redirect('product:index')
        
        else:
            messages.warning(request, 'su usuario o contraseña no coinciden')
    
    return render(request, 'users/login.html', {})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login')

def register(request):
    
    if request.user.is_authenticated:
        return redirect('product:index')
    
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado correctamente')
            return redirect('product:index')

    return render(request, 'users/register.html', {'form':form})