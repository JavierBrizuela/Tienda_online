from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'users/login.html', {})