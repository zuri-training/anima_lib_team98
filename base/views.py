from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import Signup
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request, 'Animation_lib/home.html')


def signupform(request):
    if request.method == 'POST':
        form = Signup(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            password = form.cleaned_data.get('password2')

            if password != raw_password:
                messages.error(request, 'password do not match')
            
            else:
                form.save()
                new_user = authenticate(username = username, password = raw_password)
                if new_user is not None:
                    
                    login(request, new_user)
                    return redirect('home')
                else:
                    messages.error(request, 'Service TimedOut')
        else:
            messages.error(request, 'Check Your Details Carefully')
    else:
        form = Signup()
    context = {'form' : form}
    return render(request, 'Animation_lib/signup.html', context)

# @login_required(login_url='signup')
def signinform(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = User.objects.get(email = email.lower()).username

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'user is not recognised')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong Password')
    
    context = {} 
    return render(request, 'Animation_lib/signin.html', context)


def logoutUser(request):
    logout(request)
    return redirect('signin')
