from django.shortcuts import render, redirect
from .forms import Signin
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import User

# Create your views here.


def home(request):
    return render(request, 'animax_lib/home.html')

def register(request):
    if request.method == 'POST':
        form = Signin(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = Signin()
    context = {'form' : form}
    return render(request, 'animax_lib/signup.html', context)


def loginform(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email = email)
        except:
            messages.error(request, 'user is not recognised')
        user = authenticate(request, email = email, password= password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong Password')

    context = {}
    return render(request, 'animax_lib/signin.html', context)