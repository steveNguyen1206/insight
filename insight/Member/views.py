from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.

def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)
            print(username, password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Community:home')
                else:
                    return redirect('Member:signin')
            else :
                return render(request, 'Member/signin.html', {})
        else:
            return render(request, 'Member/signin.html')
    else:
        return redirect('Community:home')

def signup(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            username = request.GET.get('username', None)
            password = request.GET.get('password', None)
            password2 = request.GET.get('password2', None)
            metamarskID = request.GET.get('metamarsk-id')

            if password != password2:
                return render(request, 'Member/signup.html')
            
            new_user = User()
            print(new_user)
            new_user.username = username
            new_user.set_password(password)
            new_user.date_joined = datetime.now()
            new_user.is_active = True
            new_user.save()


            login(request, new_user)
            return redirect('Community:home')
        else:
            return render(request, 'Member/signup.html')  
    else:
        return render(request, 'Community/home.html')  

def signout(request):
    logout(request)
    return redirect('Member:signin')

def profile(request):
    render(request, 'Member/profile.html')